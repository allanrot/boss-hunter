from code.Constants import WINDOW_WIDTH
from code.Enemy import Enemy
from code.EnemyProjectile import EnemyProjectile
from code.Entity import Entity
from code.Player import Player
from code.PlayerProjectile import PlayerProjectile


class EntityMediator:

    @staticmethod
    def __verify_collision_window(entity: Entity):
        if isinstance(entity, (Enemy, EnemyProjectile)):
            if entity.rect.right <= 0:
                entity.health = 0
        if isinstance(entity, PlayerProjectile):
            if entity.rect.left >= WINDOW_WIDTH:
                entity.health = 0

    @staticmethod
    def __verify_entity_collision(first_entity: Entity, second_entity: Entity):
        valid_interaction = False

        if isinstance(first_entity, Enemy) and isinstance(second_entity, PlayerProjectile):
            valid_interaction = True
        elif isinstance(first_entity, Player) and isinstance(second_entity, EnemyProjectile):
            valid_interaction = True

        if valid_interaction:
            if (
                first_entity.rect.right >= second_entity.rect.left and
                first_entity.rect.left <= second_entity.rect.right and
                first_entity.rect.bottom >= second_entity.rect.top and
                first_entity.rect.top <= second_entity.rect.bottom
            ):
                first_entity.health -= second_entity.damage
                second_entity.health -= first_entity.damage

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for first_entity in entity_list:
            EntityMediator.__verify_collision_window(first_entity)

            for second_entity in entity_list:
                if first_entity != second_entity:
                    EntityMediator.__verify_entity_collision(first_entity, second_entity)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for entity in entity_list:
            if isinstance(entity,(Player, Enemy, PlayerProjectile, EnemyProjectile)) and entity.health <= 0:
                entity_list.remove(entity)
