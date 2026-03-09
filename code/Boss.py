import random

from code.Constants import ENEMY_PROJECTILE_DELAY, GRAVITY, GROUND_Y
from code.EnemyProjectile import EnemyProjectile
from code.Entity import Entity
import pygame


class Boss(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position, True)

        self.walk_sheet = pygame.image.load(f'./assets/{name}_walk.png').convert_alpha()
        self.attack_sheet = pygame.image.load(f'./assets/{name}_attack.png').convert_alpha()

        self.walk_frames = []
        for i in range(6):
            frame = self.walk_sheet.subsurface(pygame.Rect(i * 96, 0, 96, 96))
            frame_rect = frame.get_bounding_rect()
            cropped_frame = frame.subsurface(frame_rect)
            self.walk_frames.append(cropped_frame)

        self.attack_frames = []
        for i in range(6):
            frame = self.attack_sheet.subsurface(pygame.Rect(i * 96, 0, 96, 96))
            frame_rect = frame.get_bounding_rect()
            cropped_frame = frame.subsurface(frame_rect)
            self.attack_frames.append(cropped_frame)

        self.surf = self.walk_frames[0]
        position = (position[0], GROUND_Y - self.surf.get_height())
        self.rect = self.surf.get_rect(topleft=position)

        self.current_frame = 0
        self.animation_timer = 0
        self.killed = False
        self.vertical_speed = 0
        self.on_ground = True
        self.speed = 0.6
        self.is_attacking = False
        self.shot_delay = ENEMY_PROJECTILE_DELAY

        self.font = pygame.font.Font(None, 24)
        self.text_surf = self.font.render(str(self.health), True, (255, 0, 0))
        self.text_rect = self.text_surf.get_rect(center=(self.rect.centerx, self.rect.top - 10))

        self.jump_timer = 0
        self.jump_cooldown = random.randint(60, 180)

    def update(self):
        self.vertical_speed += GRAVITY
        self.rect.y += self.vertical_speed

        if self.rect.bottom >= GROUND_Y:
            self.rect.bottom = GROUND_Y
            self.vertical_speed = 0
            self.on_ground = True
        else:
            self.on_ground = False

        self.text_surf = self.font.render(str(self.health), True, (255, 0, 0))
        self.text_rect.center = (self.rect.centerx + 5, self.rect.top - 10)

        if self.is_attacking:
            frames = self.attack_frames
        else:
            frames = self.walk_frames

        self.animation_timer += 1
        if self.animation_timer >= 10:
            self.animation_timer = 0
            self.current_frame = (self.current_frame + 1) % len(frames)
            self.surf = frames[self.current_frame]

        self.jump_timer += 1
        if self.jump_timer >= self.jump_cooldown and self.on_ground:
            self.vertical_speed = -10
            self.on_ground = False
            self.jump_timer = 0
            self.jump_cooldown = random.randint(60, 180)

    def move(self):
        self.rect.x -= self.speed
        self.text_rect.center = (self.rect.centerx, self.rect.top - 10)

    def shoot(self):
        self.is_attacking = True
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENEMY_PROJECTILE_DELAY
            shot_axis_x = self.rect.left
            shot_axis_y = self.rect.centery
            return EnemyProjectile('first_boss_projectile', (shot_axis_x, shot_axis_y))
