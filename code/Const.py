import pygame

COLOR_TEXT_MENU = (174, 32, 18)
COLOR_TEXT_OPTION_MENU = (0, 0, 0)
COLOR_TEXT_SELECTED_OPTION_MENU = (255, 255, 255)

ENTITY_SPEED = {
    'backgroundLevel1Layer0': 2,
    'backgroundLevel1Layer1': 1,
    'backgroundLevel1Layer2': 1.2,
    'backgroundLevel1Layer3': 1.4,
    'backgroundLevel1Layer4': 1.6,
    'backgroundLevel1Layer5': 1.8
}
ENTITY_HEALTH = {
    'player': 3,
    'enemy_0': 1,
    'enemy_1': 1,
    'player_projectile': 1,
    'enemy_projectile': 1
}
ENEMY_PROJECTILE_SPEED = 3
ENEMY_PROJECTILE_DELAY = 50
ENEMY_SPAWN_TIME = 8000
EVENT_ENEMY = pygame.USEREVENT + 1

PLAY_SHOT_DELAY = 20
PLAY_PROJECTILE_SPEED = 5

MENU_OPTIONS = (
    "PLAY",
    "OPTIONS",
    "QUIT"
)

WINDOW_WIDTH = 526
WINDOW_HEIGHT = 324