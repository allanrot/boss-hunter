import pygame

from code.Const import WINDOW_WIDTH, WINDOW_HEIGHT, MENU_OPTIONS
from code.Level import Level
from code.Menu import Menu

class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SCALED)
        pygame.init()

    def run(self):
        while True:
            menu = Menu(self.window).run()

            if menu == MENU_OPTIONS[0]:
                level = Level(self.window, 'Level 1').run()
            if menu == MENU_OPTIONS[1]:
                pass
            if menu == MENU_OPTIONS[2]:
                pygame.quit()
                quit()
            else:
                pass