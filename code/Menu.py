import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Constants import *


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/backgroundMenu.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pygame.mixer.music.load('./assets/musica_menu.wav')
        pygame.mixer.music.play(-1)

    def run(self):
        menu_option = 0

        while True:
            scaled_window = pygame.transform.scale(self.surf, self.window.get_size())
            self.window.blit(scaled_window, (0, 0))
            self.menu_text(50, "Boss".upper(), COLOR_TEXT_MENU, ((scaled_window.get_width() / 2), 30))
            self.menu_text(50, "Hunter".upper(), COLOR_TEXT_MENU, ((scaled_window.get_width() / 2), 60))

            for i in range(len(MENU_OPTIONS)):
                if i == menu_option:
                    self.menu_text(40, MENU_OPTIONS[i], COLOR_TEXT_SELECTED_OPTION_MENU, ((scaled_window.get_width() / 2), 200 + 50 * i))
                else:
                    self.menu_text(40, MENU_OPTIONS[i], COLOR_TEXT_OPTION_MENU, ((scaled_window.get_width() / 2), 200 + 50 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTIONS) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTIONS) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTIONS[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont("Lucida", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)
