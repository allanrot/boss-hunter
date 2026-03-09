import pygame

from code.Constants import ENEMY_PROJECTILE_SPEED
from code.Entity import Entity


class EnemyProjectile(Entity):
    
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.angle = 0

    def move(self):
        self.rect.centerx -= ENEMY_PROJECTILE_SPEED

    def update(self):
        pygame.transform.rotate(self.surf, (self.angle + 1) % 360)