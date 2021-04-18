import pygame
from Utils import FONT


def show_tool(x, y, tool_name, screen):
    show = FONT.render(f'Tool: {tool_name}', True, (0, 0, 0))
    screen.blit(show, (x, y))

def show_color(x, y, color_name, screen):
    show = FONT.render(f'Color: {color_name}', True, (0, 0, 0))
    screen.blit(show, (x, y))

def show_radius(x, y, radius, screen):
    show = FONT.render(f'Radius/Thickness: {radius}', True, (0, 0, 0))
    screen.blit(show, (x, y))

def drawLine_for_circle(screen, start, end, width, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(screen, color, (x, y), width)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, color, (x, y), width)