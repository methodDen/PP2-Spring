import pygame
import random
from Utils import WIDTH, HEIGHT, BRICK_COL


class Brick:
    def __init__(self):
        self.width = random.randint(20, 70)
        self.height = random.randint(10, 40)
        self.x = random.randint(100, WIDTH - 70)
        self.y = random.randint(100, HEIGHT - 70)

    def draw(self, screen):
        pygame.draw.rect(screen, BRICK_COL, (self.x, self.y, self.width, self.height))