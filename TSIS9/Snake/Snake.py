import pygame
from Utils import SNAKE_COL
class Snake:
    def __init__(self):
        self.size = 3
        self.thickness = 10
        self.dx = 5
        self.dy = 0
        self.elements = [[100, 100], [120, 100],
                         [140, 100]]  # coordinates, нулевой элемент - голова, остальные должны поспевать за ней
        self.score = 0
        self.is_add = False
        self.cnt = 0
        self.visible = False
        self.level = 1

    def draw(self, screen):
        if self.visible == True:
            for element in self.elements:
                # print(element)
                pygame.draw.rect(screen, SNAKE_COL, (element[0], element[1], self.thickness, self.thickness))

    def add_snake(self):  # test methods below
        self.size += 1
        self.score += 1
        if self.score % 5 == 0:
            self.level += 1
        self.elements.append([0, 0])
        self.is_add = False

    def move(self):
        if self.is_add:
            self.add_snake()

        for i in range(self.size - 1, 0, -1):  # Накладка кубиков друг на друга
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]

        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy

