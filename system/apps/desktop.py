# -*- coding: utf-8 -*-

from . import Window
from ..utils import *


class Desktop(Window):
    def __init__(self, screen):
        Window.__init__(
            self,
            screen,
            titre="Desktop",
            version=1.0,
            size=screen.get_size(),
            movable=False,
            fullscreen=True
        )
        # self._bg = pygame.Surface(self.screen.get_size())
        # self._create_background()
        self._bg = pygame.image.load("system/resx/background.png").convert_alpha()
        self._bg = pygame.transform.scale(self._bg, (self.screen.get_width(), int(self._bg.get_width() / self.screen.get_width() * self._bg.get_height())))

    def _create_background(self):
        for i in range(self._bg.get_width() // 32 + 1):
            for j in range(self._bg.get_height() // 32 + 1):
                pygame.draw.rect(self._bg, GREY if (i + j) % 2 else WHITE, (i * 32, j * 32, 32, 32))

    def draw_content(self):
        self._content.blit(self._bg, (0, 0))

    def trigger_user(self, event):
        pass
