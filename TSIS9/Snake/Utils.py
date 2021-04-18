import pygame
pygame.font.init()
SNAKE_COL = (42, 47, 178)
BRICK_COL = (0, 255, 0)
WIDTH = 600
HEIGHT = 500
DEFAULT_SNAKE_PARAMS = """{"size": 3, "thickness": 10, "dx": 5, "dy": 0, "is_add": false, "visible": true, "score": 0, "level": 1, "elements": [[100, 100], [120, 100], [140, 100]]}"""
running = True
start_screen = True
collision_screen = True

FPS = 30


ANNOUNCE_FONT = pygame.font.SysFont("papyrusttc", 42)
OPTION_FONT = pygame.font.SysFont("papyrusttc", 36)
SCORE_FONT = pygame.font.SysFont("papyrusttc", 30)

