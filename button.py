import object
import pygame
import presets
import math
class Button(object.GameObject):
    def __init__(
        self,
        name,
        surface,
        position,
        on_click,
        base_scale = 1.0,
        hover_surface=None,
        pressed_surface=None
    ):
        super().__init__(name, surface, position)

        self.on_click = on_click

        # Visual states
        self.default_surface = surface
        self.hover_surface = hover_surface or surface
        self.pressed_surface = pressed_surface or surface

        self.state_surface = self.default_surface
        self.original_surface = self.state_surface

        self.is_hovered = False
        self.is_pressed = False
        
        self.hover_time = 0.0
        self.base_scale = base_scale
        
        
    def update(self, dt):
        super().update(dt)
        mouse_pos = presets.get_mouse_pos_virtual(pygame.display.get_surface())
        mouse_buttons = pygame.mouse.get_pressed()

        hovered = self.rect.collidepoint(mouse_pos)
        pressed = hovered and mouse_buttons[0]
        self.is_hovered = False
        if pressed:
            new_state = self.pressed_surface
        elif hovered:
            new_state = self.hover_surface
            self.set_scale(self.base_scale * (1.05+0.05*math.sin(self.hover_time*0.002)))
            self.is_hovered = True
            self.hover_time += dt
            
        else:
            new_state = self.default_surface
            self.set_scale(self.base_scale)
            self.hover_time = 0.0

        if new_state is not self.state_surface:
            self.state_surface = new_state
            self.original_surface = self.state_surface
            self._apply_transform()
            
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = presets.get_mouse_pos_virtual(pygame.display.get_surface())
            if self.rect.collidepoint(mouse_pos):
                self.on_click(self)

                