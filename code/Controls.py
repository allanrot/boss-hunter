import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Constants import COLOR_TEXT_MENU, CONTROLS_KEYBOARD, COLOR_TEXT_SELECTED_OPTION_MENU, CONTROLS_GAME, \
    WINDOW_WIDTH


class Controls:
    def __init__(self, window, name):
        self.name = name
        self.window = window
        self.surf = pygame.image.load('./assets/backgroundMenu.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        while True:
            scaled_window = pygame.transform.scale(self.surf, self.window.get_size())
            self.window.blit(scaled_window, (0, 0))
            self.menu_text(50, "Controls".upper(), COLOR_TEXT_MENU, ((scaled_window.get_width() / 2), 30))

            for i in range(len(CONTROLS_KEYBOARD)):
                self.menu_text(40, CONTROLS_KEYBOARD[i], COLOR_TEXT_SELECTED_OPTION_MENU,
                               (WINDOW_WIDTH / 4, 100 + 35 * i))
                self.menu_text(40, CONTROLS_GAME[i], COLOR_TEXT_SELECTED_OPTION_MENU,
                               (WINDOW_WIDTH - WINDOW_WIDTH / 4, 100 + 35 * i))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            if pygame.key.get_pressed()[pygame.K_BACKSPACE]:
                return

            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont("Lucida", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)