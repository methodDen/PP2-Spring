import random
import pygame
from Utils import WIDTH, HEIGHT

class Food:
    def __init__(self):
        self.x = random.randint(100, WIDTH - 70)
        self.y = random.randint(100, HEIGHT - 70)
        self.image = pygame.image.load('images/egg.png')

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))