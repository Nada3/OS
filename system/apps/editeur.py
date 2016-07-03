from . import Window
from ..utils import *


class EditeurTexte(Window):
    def __init__(self, screen):
        Window.__init__(
            self,
            screen,
            titre="Text Editor",
            version=1.0,
            pos=(0, 0),
            size=screen.get_size(),
            couleur=WHITE
        )
        self.texts = {}
        self.text = ""

    def draw_content(self):
        # fond
        pygame.draw.rect(self._content, self.couleur, (0, 0) + self.size)

    def trigger_user(self, event):
        if event.type == KEYDOWN:
            pass

    def update(self):
        pass
