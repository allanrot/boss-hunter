import sys
import random

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from code import Entity
from code.Constants import WINDOW_WIDTH, WINDOW_HEIGHT, ENEMY_SPAWN_TIME, EVENT_ENEMY
from code.Enemy import Enemy
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.game_ended = False
        self.entity_list: list[Entity] = []
        self.background = EntityFactory.get_entity('backgroundLevel1')
        self.gameOver = EntityFactory.get_entity('gameOver')
        self.entity_list.append(EntityFactory.get_entity('player', (50, 200)))
        self.entity_list.append(EntityFactory.get_entity('enemy2', (500, 200)))
        self.game_over_start_time = None
        self.last_enemy = ''
        pygame.time.set_timer(EVENT_ENEMY, ENEMY_SPAWN_TIME)

    def run(self):
        pygame.mixer.music.load('./assets/musica_level_1.wav')
        pygame.mixer.music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)

            if not self.game_ended:
                if pygame.key.get_pressed()[pygame.K_BACKSPACE]:
                    return

                for background in self.background:
                    self.window.blit(source=background.surf, dest=background.rect)
                    background.move()

                for entity in self.entity_list:
                    self.window.blit(source=entity.surf, dest=entity.rect)
                    if isinstance(entity, Enemy):
                        self.window.blit(entity.text_surf, entity.text_rect)
                    entity.move()
                    entity.update()
                    if isinstance(entity, (Player, Enemy)):
                        shoot = entity.shoot()
                        if shoot is not None:
                            self.entity_list.append(shoot)
                    if entity.name == 'player':
                        self.level_text(self, 20, f"Lifes {entity.health}", (255, 255, 255), (25, 10))
                        self.level_text(self, 20, f"Score {entity.score}", (255, 255, 255), (25, 30))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == EVENT_ENEMY:
                        if self.last_enemy == 'enemy1':
                            next_enemy = 'enemy2'
                        else:
                            next_enemy = 'enemy1'
                        self.entity_list.append(EntityFactory.get_entity(next_enemy, (500, 200)))
                        self.last_enemy = next_enemy

                self.level_text(self, 20, f"FPS {clock.get_fps() :.0f}", (255, 255, 255), (WINDOW_WIDTH - 30, 10))
                self.level_text(self, 20, f"Entities {len(self.entity_list)}", (255, 255, 255), (WINDOW_WIDTH - 40, 30))

                EntityMediator.verify_collision(self.entity_list)
                EntityMediator.verify_health(self, self.entity_list)
            else:
                if self.game_over_start_time is None:
                    self.game_over_start_time = pygame.time.get_ticks()
                    self.background = []
                    self.entity_list = []

                self.window.blit(source=self.gameOver.surf, dest=self.gameOver.rect)
                self.gameOver.move()
                self.level_text(self, 50, "Game Over".upper(), (255, 255, 255), (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

                if pygame.time.get_ticks() - self.game_over_start_time >= 2000:
                    return

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()
    @staticmethod
    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont("Lucida", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)

    @staticmethod
    def game_over(self):
        self.game_ended = True

