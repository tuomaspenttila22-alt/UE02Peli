import itertools
import pygame

class GameObject:
    _id_counter = itertools.count()

    def __init__(self, name, surface, position=(0, 0)):
        self.id = next(GameObject._id_counter)
        self.name = name

        self.original_surface = surface
        self.surface = surface

        self.rect = self.surface.get_rect(topleft=position)

        self.visible = True
        self.alive = True

        # Transform state
        self.rotation = 0          # degrees
        self.scale_factor = 1.0
        self.opacity = 255         # 0–255
        
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
    
    def update(self, dt):
        
        pass

    def draw(self, target_surface):
        """
        Draw object to the screen (or another surface).
        """
        target_surface.blit(self.surface, self.rect)

    def destroy(self):
        """
        Mark object for removal.
        """
        self.alive = False

    def show(self):
        self.visible = True

    def hide(self):
        self.visible = False
    
    
    def set_opacity(self, alpha):
        self.opacity = max(0, min(255, int(alpha)))
        self._apply_transform()
    
    def move(self, dx=0, dy=0):
        self.rect.x += dx
        self.rect.y += dy

    def set_position(self, x, y):
        self.rect.topleft = (x, y)

    def collides_with(self, other):
        return self.rect.colliderect(other.rect)
    
    def set_scale(self, factor):
        self.scale_factor = max(0.01, factor)
        self._apply_transform()

    def scale(self, delta):
        self.set_scale(self.scale_factor * delta)
        
    def set_rotation(self, degrees):
        self.rotation = degrees % 360
        self._apply_transform()

    def rotate(self, delta_degrees):
        self.set_rotation(self.rotation + delta_degrees)

    
    
    
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