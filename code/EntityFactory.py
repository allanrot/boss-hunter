from code.Background import Background
from code.Boss import Boss
from code.Constants import WINDOW_WIDTH
from code.Enemy import Enemy
from code.GameOver import GameOver
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
            case 'backgroundGameOver':
                return GameOver(entity_name, position)
            case 'player':
                return Player(entity_name, position)
            case 'enemy_0':
                return Enemy(entity_name, position)
            case 'enemy_1':
                return Enemy(entity_name, position)
            case 'first_boss':
                return Boss(entity_name, position)