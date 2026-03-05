from abc import ABC, abstractmethod

import pygame

from code.Constants import ENTITY_HEALTH, ENTITY_DAMAGE


class Entity(ABC):
    def __init__(self, name: str, position: tuple, is_sprite: bool=False):
        self.name = name
        self.speed = 0
        if not name.startswith('backgroundLevel1'):
            self.health = ENTITY_HEALTH[name]
            self.damage = ENTITY_DAMAGE[name]
        if not is_sprite:
            self.surf = pygame.image.load('./assets/' + name + '.png').convert_alpha()
            self.rect = self.surf.get_rect(left=position[0], top=position[1])

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def update(self):
        pass