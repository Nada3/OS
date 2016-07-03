import pygame
import system
import apps
import sys


def main():
    pygame.init()
    pygame.key.set_repeat(200, 100)

    win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    win_manager = system.wm.DesktopManager(win)
    system.process_manager.ProcessManager()

    system.process_manager.ProcessManager.add_windows(*[_ for _ in apps.app_list + system.app_list])
    win_manager.run()

    pygame.quit()


if __name__ == '__main__':
    sys.excepthook = system.deboguer.info
    system.deboguer.method = main
    main()
