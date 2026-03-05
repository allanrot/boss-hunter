from code.Constants import ENEMY_PROJECTILE_SPEED
from code.Entity import Entity


class EnemyProjectile(Entity):
    
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENEMY_PROJECTILE_SPEED

    def update(self):
        pass