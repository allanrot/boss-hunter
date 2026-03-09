import sys

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from code import Entity
from code.Boss import Boss
from code.Constants import WINDOW_WIDTH, WINDOW_HEIGHT, ENEMY_SPAWN_TIME, EVENT_ENEMY, SCORE_TO_UNLOCK_BOSS, EVENT_BOSS
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
        self.backgroundLevel1 = EntityFactory.get_entity('backgroundLevel1')
        self.backgroundGameOver = EntityFactory.get_entity('backgroundGameOver')
        self.entity_list.append(EntityFactory.get_entity('player', (50, 200)))
        self.entity_list.append(EntityFactory.get_entity('enemy_1', (550, 200)))
        self.game_over_start_time = None
        self.first_boss_start_time = None
        self.last_enemy = ''
        self.player_score = 0
        self.first_boss_released = False
        pygame.time.set_timer(EVENT_ENEMY, ENEMY_SPAWN_TIME)
        pygame.time.set_timer(EVENT_BOSS, ENEMY_SPAWN_TIME)

    def run(self):
        pygame.mixer.music.load('./assets/musica_level_1.wav')
        pygame.mixer.music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)

            if pygame.key.get_pressed()[pygame.K_BACKSPACE]:
                return

            for background in self.backgroundLevel1:
                self.window.blit(source=background.surf, dest=background.rect)
                background.move()

            if self.player_score >= SCORE_TO_UNLOCK_BOSS and not self.first_boss_released:
                if self.first_boss_start_time is None:
                    self.first_boss_start_time = pygame.time.get_ticks()

                if pygame.time.get_ticks() - self.first_boss_start_time >= 2000:
                    self.entity_list.append(EntityFactory.get_entity('first_boss', (600, 200)))
                    self.first_boss_released = True

            for entity in self.entity_list:
                self.window.blit(source=entity.surf, dest=entity.rect)
                if isinstance(entity, (Enemy, Boss)):
                    self.window.blit(entity.text_surf, entity.text_rect)
                entity.move()
                entity.update()

                if isinstance(entity, (Player, Enemy, Boss)):
                    shoot = entity.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)

                if entity.name == 'player':
                    self.level_text(self, 20, f"Lifes {0 if entity.health < 0 else entity.health}", (255, 255, 255), (25, 10))
                    self.level_text(self, 20, f"Score {entity.score}", (255, 255, 255), (25, 30))
                    self.player_score = entity.score
                    if entity.is_dying:
                        self.game_ended = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY and self.player_score < SCORE_TO_UNLOCK_BOSS:
                    if self.last_enemy == 'enemy_0':
                        next_enemy = 'enemy_1'
                    else:
                        next_enemy = 'enemy_0'
                    self.entity_list.append(EntityFactory.get_entity(next_enemy, (600, 200)))
                    self.last_enemy = next_enemy

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            EntityMediator.verify_collision(self.entity_list)
            EntityMediator.verify_health(self.entity_list)

            self.level_text(self, 20, f"FPS {clock.get_fps() :.0f}", (255, 255, 255), (WINDOW_WIDTH - 30, 10))
            self.level_text(self, 20, f"Entities {len(self.entity_list)}", (255, 255, 255), (WINDOW_WIDTH - 40, 30))

            if self.game_ended:
                if self.game_over_start_time is None:
                    self.game_over_start_time = pygame.time.get_ticks()

                if pygame.time.get_ticks() - self.game_over_start_time >= 600:
                    self.backgroundLevel1 = []
                    self.entity_list = []
                    self.window.blit(source=self.backgroundGameOver.surf, dest=self.backgroundGameOver.rect)
                    self.backgroundGameOver.move()
                    self.level_text(self, 50, "Game Over".upper(), (255, 255, 255), (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
                if pygame.time.get_ticks() - self.game_over_start_time >= 4000:
                    return

            pygame.display.flip()

    @staticmethod
    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont("Lucida", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)