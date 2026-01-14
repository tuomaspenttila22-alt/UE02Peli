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

        self.alive = True
        
    def update(self, dt):
        """
        Update object state.
        Override in subclasses.
        """
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
    
    def move(self, dx=0, dy=0):
        self.rect.x += dx
        self.rect.y += dy

    def set_position(self, x, y):
        self.rect.topleft = (x, y)

    def collides_with(self, other):
        return self.rect.colliderect(other.rect)
    
    def resize(self, width, height):
        """
        Resize the object's surface to a new size.
        Keeps the object centered.
        """
        center = self.rect.center

        self.surface = pygame.transform.scale(self.original_surface, (width, height))
        self.rect = self.surface.get_rect(center=center)
        
    def scale(self, factor):
        """
        Scale the object by a multiplier.
        Example: factor = 2.0 doubles the size.
        """
        new_width = int(self.rect.width * factor)
        new_height = int(self.rect.height * factor)
        self.resize(new_width, new_height)

    
    
    
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