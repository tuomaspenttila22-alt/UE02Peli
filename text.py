import object


class TextObject(object.GameObject):
    def __init__(
        self,
        name,
        text,
        font,
        color,
        position=(0, 0),
        antialias=False
    ):
        self.text = text
        self.font = font
        self.color = color
        self.antialias = antialias

        surface = self._render_text()
        super().__init__(name, surface, position)
    
    def _render_text(self):
        return self.font.render(
            self.text,
            self.antialias,
            self.color
        )
    def set_text(self, new_text):
        if new_text != self.text:
            self.text = new_text
            self.original_surface = self._render_text()
            self._apply_transform()
            
    def set_color(self, color):
        self.color = color
        self.original_surface = self._render_text()
        self._apply_transform()

    def set_font(self, font):
        self.font = font
        self.original_surface = self._render_text()
        self._apply_transform()
    
    def set_alpha(self, alpha):
        self.set_opacity(alpha)

    def set_scale(self, factor):
        super().set_scale(factor)

    def set_rotation(self, degrees):
        super().set_rotation(degrees)
    
    