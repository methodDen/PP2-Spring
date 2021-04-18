import pygame

class Indicator:
    def __init__(self):
        self.thickness = 50
        self.color = (255, 255, 255)

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, (25, 25, self.thickness, self.thickness))