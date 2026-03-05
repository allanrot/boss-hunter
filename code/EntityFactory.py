from code.Background import Background
from code.Constants import WINDOW_WIDTH
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'backgroundLevel1':
                list_bg = []
                for i in range(6):
                    list_bg.append(Background(f'{entity_name}Layer{i}', position))
                    list_bg.append(Background(f'{entity_name}Layer{i}', (WINDOW_WIDTH, 0)))
                return list_bg
            case 'player':
                return Player('player', position)
            case 'enemy1':
                return Enemy('enemy_0', position)
            case 'enemy2':
                return Enemy('enemy_1', position)