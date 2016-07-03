from . import Window
from ..utils import *
import re


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
        self.texts = {
            "content": [],
            "cli_datas": {"line": 0, "char": 0},
            "cli": font.render("_", 1, RED),
            "a": font.render("a", 1, BLACK)
        }
        self.text = ""
        self.curseur = 0

    def draw_content(self):
        # fond
        pygame.draw.rect(self._content, self.couleur, (0, 0) + self.size)
        y = 25
        # barre menu
        pygame.draw.rect(self._content, LIGHT_GREY, (0, 0, self.size[0], y))
        # texte
        for li, line in enumerate(self.texts["content"]):
            if li == self.texts["cli_datas"]["line"]:
                self._content.blit(self.texts["cli"], (self.texts["cli_datas"]["char"] * self.texts["a"].get_width(), y + 2))
            self._content.blit(line, (0, y))
            y += line.get_height() + 2

    def trigger_user(self, event):
        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                self.text = self.text[:self.curseur] + self.text[self.curseur + 1:]
                self.curseur -= 1
            elif event.key in (K_RETURN, K_KP_ENTER):
                self.text += "\n"
                self.curseur += 1
            elif event.key == K_TAB:
                self.text += " " * 4
                self.curseur += 4
            elif event.key == K_LEFT:
                self.curseur -= 1
            elif event.key == K_RIGHT:
                self.curseur += 1
            else:
                self.text += event.unicode
                self.curseur += 1

    # TODO: ne générer que la partie visible du texte
    def update(self):
        text = self.text.split('\n')
        self.texts['content'] = []
        tot = 0
        for li, line in enumerate(text):
            for ch, char in enumerate(line):
                if tot == self.curseur - 1:
                    self.texts["cli_datas"]["line"] = li
                    self.texts["cli_datas"]["char"] = ch
                    break
                tot += 1
            self.texts['content'].append(font.render(line, 1, BLACK))
