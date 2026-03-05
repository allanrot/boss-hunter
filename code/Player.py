from pygame import K_SPACE

from code.Constants import WINDOW_WIDTH, PLAY_SHOT_DELAY, GRAVITY
from code.Entity import Entity
import pygame

from code.PlayerProjectile import PlayerProjectile


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position, True)

        self.walk_sheet = pygame.image.load('./assets/player_walk.png').convert_alpha()
        self.jump_sheet = pygame.image.load('./assets/player_jump.png').convert_alpha()
        self.shoot_sheet = pygame.image.load('./assets/player_shoot_walking.png').convert_alpha()
        self.bow_sheet = pygame.image.load('./assets/player_bow.png').convert_alpha()

        self.score = 0

        self.walk_frames = []
        for i in range(6):
            frame = self.walk_sheet.subsurface(pygame.Rect(i * 42, 0, 42, 42))
            frame_rect = frame.get_bounding_rect()
            cropped_frame = frame.subsurface(frame_rect)
            self.walk_frames.append(cropped_frame)

        self.jump_frames = []
        for i in range(6):
            frame = self.jump_sheet.subsurface(pygame.Rect(i * 42, 0, 42, 42))
            frame_rect = frame.get_bounding_rect()
            cropped_frame = frame.subsurface(frame_rect)
            self.jump_frames.append(cropped_frame)

        self.shoot_frames = []
        for i in range(6):
            frame = self.shoot_sheet.subsurface(pygame.Rect(i * 42, 0, 42, 42))
            frame_rect = frame.get_bounding_rect()
            cropped_frame = frame.subsurface(frame_rect)
            self.shoot_frames.append(cropped_frame)

        self.bow_frames = []
        for i in range(6):
            frame = self.bow_sheet.subsurface(pygame.Rect(i * 42, 0, 42, 42))
            self.bow_frames.append(frame)

        self.current_frame = 0
        self.animation_timer = 0
        self.is_jumping = False
        self.is_walking = True
        self.is_shooting = False
        self.shoot_timer = 0
        self.shot_delay = PLAY_SHOT_DELAY

        self.ground_y = 300
        self.left_wall = 0
        self.right_wall = WINDOW_WIDTH

        self.original_height = 42

        position = (position[0], self.ground_y - self.original_height)

        self.surf = self.walk_frames[0]
        self.rect = self.surf.get_rect(topleft=position)

        self.speed = 3
        self.vertical_speed = 0
        self.on_ground = True
        self.space_pressed = False

    def update(self):
        if self.is_shooting:
            frames = self.shoot_frames
        elif self.is_jumping:
            frames = self.jump_frames
        elif self.is_walking:
            frames = self.walk_frames
        else:
            self.current_frame = 0
            self.surf = self.walk_frames[0].copy()
            return

        self.animation_timer += 1
        if self.animation_timer >= 10:
            self.animation_timer = 0
            self.current_frame = (self.current_frame + 1) % len(frames)

        self.surf = frames[self.current_frame].copy()

        if self.is_shooting:
            bow_x = (self.surf.get_width() - self.bow_frames[self.current_frame].get_width()) + 15
            bow_y = (self.surf.get_height() - self.bow_frames[self.current_frame].get_height())
            self.surf.blit(self.bow_frames[self.current_frame], (bow_x, bow_y))
            self.shoot_timer += 1
            if self.shoot_timer >= 6:
                self.is_shooting = False
                self.shoot_timer = 0
                self.current_frame = 0

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            if self.rect.right < self.right_wall:
                self.animation_timer += 2
                self.rect.x += self.speed
                self.is_walking = True
        if keys[pygame.K_LEFT]:
            if self.rect.left > self.left_wall:
                self.animation_timer -= 0.6
                self.rect.x -= self.speed
                self.is_walking = True
        if keys[pygame.K_UP] and self.on_ground:
            self.vertical_speed = -12
            self.on_ground = False
            self.is_jumping = True
            self.current_frame = 0

        self.vertical_speed += GRAVITY
        self.rect.y += self.vertical_speed

        if self.rect.bottom >= self.ground_y:
            self.rect.bottom = self.ground_y
            self.vertical_speed = 0
            self.on_ground = True
            self.is_jumping = False
        else:
            self.on_ground = False

    def shoot(self):
        keys = pygame.key.get_pressed()

        if keys[K_SPACE] and not self.space_pressed:
            self.space_pressed = True
            self.shot_delay = PLAY_SHOT_DELAY
            self.is_shooting = True
            self.current_frame = 0
            self.shoot_timer = 0
            return PlayerProjectile('player_projectile', (self.rect.centerx, self.rect.centery))
        elif not keys[K_SPACE]:
            self.space_pressed = False

        return None