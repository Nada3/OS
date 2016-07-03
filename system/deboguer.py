import time
import traceback
from .utils import *

method = None


def info(kind, value, tb):
    output = traceback.format_exception(kind, value, tb).split('\n')
    screen = pygame.display.get_surface()
    text = [font.render(o, 1, BLACK) for o in output]
    logo = pygame.image.load("system/resx/logo.png").convert_alpha()
    y = logo.get_height() + 50
    x = 50
    TIMER = time.time() + 5

    while time.time() <= TIMER:
        screen.fill(BLUE)
        screen.blit(logo, (screen.get_width() // 2 - logo.get_width() // 2, 0))
        for i, o in enumerate(text):
            screen.blit(o, (x, y))
            y += i * 25
        y += 50
        screen.blit(font.render("Le système va redémarrer dans %2.2f secondes" % (TIMER - time.time())))
        pygame.display.flip()
    if method:
        method()
