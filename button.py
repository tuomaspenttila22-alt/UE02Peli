import object
import pygame

class Button(object.GameObject):
    def __init__(
        self,
        name,
        surface,
        position,
        on_click,
        hover_surface=None,
        pressed_surface=None
    ):
        super().__init__(name, surface, position)

        self.on_click = on_click

        # Visual states
        self.default_surface = surface
        self.hover_surface = hover_surface or surface
        self.pressed_surface = pressed_surface or surface

        self.is_hovered = False
        self.is_pressed = False
        
    def update(self, dt):
        mouse_pos = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()

        self.is_hovered = self.rect.collidepoint(mouse_pos)
        self.is_pressed = self.is_hovered and mouse_buttons[0]

        if self.is_pressed:
            self.surface = self.pressed_surface
        elif self.is_hovered:
            self.surface = self.hover_surface
        else:
            self.surface = self.default_surface
            
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.on_click()