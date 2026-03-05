from code.Const import WINDOW_WIDTH
from code.Enemy import Enemy
from code.EnemyProjectile import EnemyProjectile
from code.Entity import Entity
from code.Player import Player
from code.PlayerProjectile import PlayerProjectile


class EntityMediator:

    @staticmethod
    def __verify_collision_window(entity: Entity):
        if isinstance(entity, Enemy):
            if entity.rect.right <= 0:
                entity.health = 0
        if isinstance(entity, PlayerProjectile):
            if entity.rect.left >= WINDOW_WIDTH:
                entity.health = 0
        if isinstance(entity, EnemyProjectile):
            if entity.rect.right <= 0:
                entity.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for entity in entity_list:
            EntityMediator.__verify_collision_window(entity)

            if isinstance(entity,(Player, Enemy, PlayerProjectile, EnemyProjectile)) and entity.health <= 0:
                entity_list.remove(entity)