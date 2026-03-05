from code.Constants import ENEMY_PROJECTILE_DELAY
from code.EnemyProjectile import EnemyProjectile
from code.Entity import Entity
import pygame


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position, True)

        self.walk_sheet = pygame.image.load(f'./assets/{name}_walk.png').convert_alpha()
        self.attack_sheet = pygame.image.load(f'./assets/{name}_attack.png').convert_alpha()

        self.walk_frames = []
        for i in range(6):
            frame = self.walk_sheet.subsurface(pygame.Rect(i * 96, 0, 96, 96))
            self.walk_frames.append(frame)

        self.attack_frames = []
        for i in range(6):
            frame = self.attack_sheet.subsurface(pygame.Rect(i * 96, 0, 96, 96))
            self.attack_frames.append(frame)

        self.current_frame = 0
        self.animation_timer = 0
        self.surf = self.walk_frames[0]

        self.ground_y = 300
        position = (position[0], self.ground_y - 96)
        self.rect = self.surf.get_rect(topleft=position)

        self.vertical_speed = 0
        self.gravity = 0.5
        self.on_ground = True
        self.speed = 1
        self.is_attacking = False
        self.shot_delay = ENEMY_PROJECTILE_DELAY

    def update(self):
        if self.is_attacking:
            frames = self.attack_frames
        else:
            frames = self.walk_frames

        self.animation_timer += 1
        if self.animation_timer >= 10:
            self.animation_timer = 0
            self.current_frame = (self.current_frame + 1) % len(frames)
            self.surf = frames[self.current_frame]

        self.vertical_speed += self.gravity
        self.rect.y += self.vertical_speed

        if self.rect.bottom >= self.ground_y:
            self.rect.bottom = self.ground_y
            self.vertical_speed = 0
            self.on_ground = True
        else:
            self.on_ground = False

    def move(self):
        self.rect.x -= self.speed

    def shoot(self):
        self.is_attacking = True
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENEMY_PROJECTILE_DELAY
            shot_axis_x = self.rect.centerx + 10 if self.name == 'enemy_0' else self.rect.centerx + 15
            shot_axis_y = self.rect.centery - 5 if self.name == 'enemy_0' else self.rect.centery + 20
            return EnemyProjectile('enemy_projectile', (shot_axis_x, shot_axis_y))
