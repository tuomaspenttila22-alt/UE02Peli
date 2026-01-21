import itertools
import pygame
import presets
class GameObject:
    _id_counter = itertools.count()

    def __init__(self, name, surface, position=(0, 0), updateLoop = None):
        self.id = next(GameObject._id_counter)
        self.name = name

        
        self.updateLoop = updateLoop
        self.time_alive = 0
        
        self.base_surface = surface
        self.original_surface = surface
        self.surface = surface

        self.rect = self.surface.get_rect(topleft=position)

        self.visible = True
        self.alive = True

        # Transform state
        self.rotation = 0          # degrees
        self.scale_factor = 1.0
        self.opacity = 255         # 0–255
        
        #Parent/Child
        self.parent = None
        self.children = []

        self.local_pos = pygame.Vector2(0, 0)
        self.local_scale_factor = 1.0
        
        #Mask
        self.mask = pygame.mask.from_surface(self.surface)
        
    def add_child(self, child, offset=(0, 0)):
        child.parent = self
        child.local_pos = pygame.Vector2(offset)
        self.children.append(child)

        child._update_world_position()   
        
    def _update_world_position(self):
        if self.parent:
            self.rect.topleft = (
                self.parent.rect.topleft + self.local_pos
            )
            self.scale_factor = self.parent.scale_factor * self.local_scale_factor
            self._apply_transform()
            
    def getChildByName(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None     
             
    def remove_child(self, child):
        if child in self.children:
            self.children.remove(child)
            child.parent = None
    
    def create_rect(self):
        self.rect = self.surface.get_rect(topleft=position)
    
    def _apply_transform(self):
        center = self.rect.center

        surf = self.original_surface

        # Scale
        if self.scale_factor != 1.0:
            w = int(surf.get_width() * self.scale_factor)
            h = int(surf.get_height() * self.scale_factor)
            surf = pygame.transform.scale(surf, (w, h))

        # Rotate
        if self.rotation != 0:
            surf = pygame.transform.rotate(surf, self.rotation)

        # Opacity
        surf = surf.copy()
        surf.set_alpha(self.opacity)

        self.surface = surf
        self.rect = self.surface.get_rect(center=center)
        
        self.mask = pygame.mask.from_surface(self.surface)
    
    def update(self, dt):
        self.time_alive += dt
        if self.updateLoop:
            self.updateLoop(self, dt)
        
        self._update_world_position()
        for child in self.children:
            child.update(dt)
    

    def draw(self, target_surface):
        if not self.visible:
            return

        target_surface.blit(self.surface, self.rect)

        for child in self.children:
            child.draw(target_surface)

    def destroy(self):
        """
        Mark object for removal.
        """
        self.alive = False
        for child in self.children:
            child.destroy()

    def show(self):
        self.visible = True

    def hide(self):
        self.visible = False
    
    
    def set_opacity(self, alpha):
        self.opacity = max(0, min(255, int(alpha)))
        self._apply_transform()
    
    def move(self, dx=0, dy=0):
        self.local_pos.x += dx
        self.local_pos.y += dy
        self.rect.x += dx
        self.rect.y += dy

        for child in self.children:
            child._update_world_position()

    def set_position(self, x, y):
        self.rect.topleft = (x, y)

        for child in self.children:
            child._update_world_position()

    def collides_with(self, other):
        return self.rect.colliderect(other.rect)
    
    def collides_with_mask(self, other):
        """
        Pixel-perfect collision check using masks.
        Returns True if this object overlaps another on opaque pixels.
        """
        # Quick reject
        if not self.rect.colliderect(other.rect):
            return False

        # Both objects must have masks
        if not hasattr(self, "mask") or not hasattr(other, "mask"):
            return False

        # Offset between the two masks
        offset_x = other.rect.x - self.rect.x
        offset_y = other.rect.y - self.rect.y

        overlap = self.mask.overlap(other.mask, (offset_x, offset_y))
        return overlap is not None
    
    def set_scale(self, factor):
        self.scale_factor = max(0.01, factor)
        self.local_scale_factor = max(0.01, factor)
        self._apply_transform()

    def scale(self, delta):
        self.set_scale(self.scale_factor * delta)
        
    def set_rotation(self, degrees):
        self.rotation = degrees % 360
        self._apply_transform()

    def rotate(self, delta_degrees):
        self.set_rotation(self.rotation + delta_degrees)
        
    def center(self,screen_size=presets.VIRTUAL_SCREEN_RECT):
        """
        Centers the object.
        - If the object has a parent: center within the parent.
        - If no parent: center on the virtual screen.
        """
        if self.parent:
            parent_center = self.parent.rect.center
            self.rect.center = parent_center

            # Update local offset relative to parent
            self.local_pos = (
                pygame.Vector2(self.rect.topleft)
                - pygame.Vector2(self.parent.rect.topleft)
            )

        else:
            if screen_size is None:
                raise ValueError(
                    "screen_size must be provided when centering a root object"
                )

            self.rect.center = (
                screen_size[0] // 2,
                screen_size[1] // 2
            )
    def to_top_left(self, screen_size=presets.VIRTUAL_SCREEN_RECT):
        """
        Moves the object to the top-left corner.
        - If the object has a parent: top-left of the parent.
        - If no parent: top-left of the screen.
        """
        if self.parent:
            self.rect.topleft = self.parent.rect.topleft

            # Update local offset
            self.local_pos = (
                pygame.Vector2(self.rect.topleft)
                - pygame.Vector2(self.parent.rect.topleft)
            )

        else:
            # Screen top-left is always (0, 0)
            self.rect.topleft = (0, 0)
            
    def set_hue(self, hue_shift):
        """
        Shifts the hue of the object's surface.
        hue_shift: 0–360 degrees
        """
        surf = self.base_surface.copy()
        surf.lock()

        width, height = surf.get_size()

        for x in range(width):
            for y in range(height):
                r, g, b, a = surf.get_at((x, y))

                if a == 0:
                    continue

                color = pygame.Color(r, g, b)
                h, s, v, _ = color.hsva

                h = (h + hue_shift) % 360

                color.hsva = (h, s, v, a * 100 / 255)
                color.a = a  # restore full alpha precision

                surf.set_at((x, y), color)

        surf.unlock()

        self.original_surface = surf
        self._apply_transform()
    
    
    
    
class ObjectManager:
    def __init__(self):
        self.objects = []

    def add(self, obj):
        self.objects.append(obj)

    def update(self, dt):
        for obj in self.objects:
            obj.update(dt)

        self.objects = [o for o in self.objects if o.alive]

    def draw(self, screen):
        for obj in self.objects:
            obj.draw(screen)
            
    def getObjectByName(self, name):
        for obj in self.objects:
            if obj.name == name:
                return obj
        return None
    def getObjectsListByName(self, name):
        list = []
        for obj in self.objects:
            if name in obj.name :
                list.append(obj)
        return list
    
    def hasObjectByName(self, name):
        for obj in self.objects:
            if obj.name == name:
                return True
        return False
    
    def clearObjects(self):
        self.objects = []
            
objectManager = ObjectManager()