import pygame

WIDTH = 600
HEIGHT = 500

pygame.init()

running = True

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')
font = pygame.font.SysFont('Arial', 30)

FPS = 30
clock = pygame.time.Clock()


while running:
	mil = clock.tick(FPS)
	screen.fill((165, 206, 216))
	pygame.draw.rect(screen, [255,255,255], [0, 0, 100, 130])
	pygame.display.flip()