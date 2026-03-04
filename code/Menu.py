import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WINDOW_WIDTH, COLOR_TEXT_MENU, MENU_OPTIONS, COLOR_TEXT_OPTION_MENU


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/orig.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer.music.load('./assets/menu.wav')
        pygame.mixer.music.play(-1)

        while True:
            scaled_window = pygame.transform.scale(self.surf, self.window.get_size())
            self.window.blit(scaled_window, (0, 0))
            self.menu_text(50, "Boss", COLOR_TEXT_MENU, ((WINDOW_WIDTH / 2), 20))
            self.menu_text(50, "Hunter", COLOR_TEXT_MENU, ((WINDOW_WIDTH / 2), 60))

            for i in range(len(MENU_OPTIONS)):
                self.menu_text(50, MENU_OPTIONS[i], COLOR_TEXT_OPTION_MENU, ((WINDOW_WIDTH / 2), 200 + 50 * i))


            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont("Lucida", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)
