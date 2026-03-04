import pygame

from code.Const import WINDOW_WIDTH, WINDOW_HEIGHT
from code.Menu import Menu

class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
        pygame.init()

    def run(self):
        while True:
            Menu(self.window).run()