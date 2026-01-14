import object
import pygame
import presets

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
        
        self.base_scale = base_scale
        
    def update(self, dt):
        mouse_pos = presets.get_mouse_pos_virtual(pygame.display.get_surface())
        mouse_buttons = pygame.mouse.get_pressed()

        hovered = self.rect.collidepoint(mouse_pos)
        pressed = hovered and mouse_buttons[0]

        if pressed:
            new_state = self.pressed_surface
        elif hovered:
            new_state = self.hover_surface
            self.set_scale(self.base_scale * 1.2)
        else:
            new_state = self.default_surface
            self.set_scale(self.base_scale)

        if new_state is not self.state_surface:
            self.state_surface = new_state
            self.original_surface = self.state_surface
            self._apply_transform()
            
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = presets.get_mouse_pos_virtual(pygame.display.get_surface())
            if self.rect.collidepoint(mouse_pos):
                self.on_click()

                