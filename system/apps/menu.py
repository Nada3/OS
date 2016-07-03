# -*- coding: utf-8 -*-

from . import Window
from ..utils import *
from ..process_manager import ProcessManager


class Menu(Window):
    def __init__(self, screen):
        Window.__init__(
            self,
            screen,
            titre="Menu",
            version=1.0,
            size=(250, 375),
            movable=False,
            fullscreen=True
        )
        self.state = WStates.UNACTIVE

    def draw_content(self):
        pygame.draw.rect(self._content, PURPLE, (0, 0) + self.size)

        pygame.draw.rect(self.screen, RED, self.escape_btn)

    def trigger_user(self, event):
        if event.type == MOUSEBUTTONUP:
            self.clic_on_barre = False
            x, y = event.pos
            if self.escape_btn[0] <= x <= self.escape_btn[0] + self.escape_btn[2] \
                    and self.escape_btn[1] <= y <= self.escape_btn[1] + self.escape_btn[3]:
                pygame.draw.rect(self.screen, BLACK, (0, 0) + self.screen.get_size())
                ProcessManager.remove_process(0)
