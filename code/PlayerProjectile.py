from code.Const import PLAY_PROJECTILE_SPEED
from code.Entity import Entity


class PlayerProjectile(Entity):
    
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx += PLAY_PROJECTILE_SPEED

    def update(self):
        pass