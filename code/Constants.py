import pygame

BACKGROUND_PARALLAX_SPEED = {
    'backgroundLevel1Layer0': 2,
    'backgroundLevel1Layer1': 1,
    'backgroundLevel1Layer2': 1.2,
    'backgroundLevel1Layer3': 1.4,
    'backgroundLevel1Layer4': 1.6,
    'backgroundLevel1Layer5': 1.8
}

COLOR_TEXT_MENU = (174, 32, 18)
COLOR_TEXT_OPTION_MENU = (0, 0, 0)
COLOR_TEXT_SELECTED_OPTION_MENU = (255, 255, 255)
CONTROLS_KEYBOARD = (
    "Space",
    "Left arrow",
    "Right arrow",
    "Backspace"
)
CONTROLS_GAME = (
    "Shoot",
    "Move back",
    "Move forward",
    "Back"
)

ENTITY_HEALTH = {
    'player': 5,
    'enemy_0': 20,
    'enemy_1': 10,
    'first_boss': 30,
    'player_projectile': 1,
    'enemy_projectile': 1,
    'first_boss_projectile': 1
}
ENTITY_DAMAGE = {
    'player': 1,
    'enemy_0': 1,
    'enemy_1': 1,
    'first_boss': 1,
    'player_projectile': 1,
    'enemy_projectile': 1,
    'first_boss_projectile': 1
}
ENEMY_PROJECTILE_SPEED = 3
ENEMY_PROJECTILE_DELAY = 57
ENEMY_SPAWN_TIME: int = 5000
BOSS_SPAWN_TIME: int = 10000
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_BOSS = pygame.USEREVENT + 2

GRAVITY = 0.5
GROUND_Y = 300

PLAY_SHOT_DELAY = 40
PLAY_PROJECTILE_SPEED = 5

SCORE_TO_UNLOCK_BOSS = 1

MENU_OPTIONS = (
    "PLAY",
    "CONTROLS",
    "QUIT"
)

WINDOW_WIDTH = 526
WINDOW_HEIGHT = 324