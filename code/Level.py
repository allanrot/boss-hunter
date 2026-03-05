import sys
import random

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from code import Entity
from code.Constants import WINDOW_WIDTH, WINDOW_HEIGHT, ENEMY_SPAWN_TIME, EVENT_ENEMY, ENTITY_HEALTH
from code.Enemy import Enemy
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.background = EntityFactory.get_entity('backgroundLevel1')
        self.entity_list.append(EntityFactory.get_entity('player', (50, 200)))
        self.entity_list.append(EntityFactory.get_entity('enemy2', (500, 200)))
        pygame.time.set_timer(EVENT_ENEMY, ENEMY_SPAWN_TIME)

    def run(self):
        # pygame.mixer.music.load('./assets/musica_level_1.wav')
        # pygame.mixer.music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)

            for background in self.background:
                self.window.blit(source=background.surf, dest=background.rect)
                background.move()

            for entity in self.entity_list:
                self.window.blit(source=entity.surf, dest=entity.rect)
                entity.move()
                entity.update()
                if isinstance(entity, (Player, Enemy)):
                    shoot = entity.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if entity.name == 'player':
                    self.level_text(self, 20, f"Vidas {entity.health}", (255, 255, 255), (25, 10))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('enemy1', 'enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice, (500, 200)))

            self.level_text(self, 20, f"FPS {clock.get_fps() :.0f}", (255, 255, 255), (WINDOW_WIDTH - 30, 10))
            self.level_text(self, 20, f"Entidades {len(self.entity_list)}", (255, 255, 255), (WINDOW_WIDTH - 50, 30))

            pygame.display.flip()
            EntityMediator.verify_collision(self.entity_list)
            EntityMediator.verify_health(self.entity_list)

    @staticmethod
    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont("Lucida", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)
