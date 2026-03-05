from code.Const import ENEMY_PROJECTILE_DELAY
from code.EnemyProjectile import EnemyProjectile
from code.Entity import Entity
import pygame


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position, True)

        self.walk_sheet = pygame.image.load(f'./assets/{name}_walk.png').convert_alpha()

        sheet_width = self.walk_sheet.get_width()
        sheet_height = self.walk_sheet.get_height()
        frame_width = sheet_width // 6
        frame_height = sheet_height

        self.walk_frames = []
        for i in range(6):
            frame = self.walk_sheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
            scaled_frame = pygame.transform.scale(frame, (frame_width * 2, frame_height * 2))
            self.walk_frames.append(scaled_frame)

        self.current_frame = 0
        self.animation_timer = 0
        self.surf = self.walk_frames[0]

        self.ground_y = 300
        position = (position[0], self.ground_y - (frame_height * 2))
        self.rect = self.surf.get_rect(topleft=position)

        self.vertical_speed = 0
        self.gravity = 0.5
        self.on_ground = True
        self.speed = 1
        self.shot_delay = ENEMY_PROJECTILE_DELAY

    def update(self):
        self.animation_timer += 1
        if self.animation_timer >= 10:
            self.animation_timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.walk_frames)
            self.surf = self.walk_frames[self.current_frame]

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
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENEMY_PROJECTILE_DELAY
            print(self.name)
            shot_axis_y = self.rect.centery + 42 if self.name == 'enemy_1' else self.rect.centery
            return EnemyProjectile('enemy_projectile', (self.rect.centerx, shot_axis_y))