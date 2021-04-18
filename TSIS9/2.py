import pygame


BLUE = (0, 0, 255)

pygame.init()

width = 350
height = 400
screen = pygame.display.set_mode((width, height))

isPressed = False
prevPoint = (0, 0)
curPoint = (0, 0)


currentTool = 0
toolCount = 2

def drawRectangle(screen, x, y, w, h):
	pygame.draw.rect(screen, BLUE, (x, y, w, h), 5)

def drawCircle(screen, x, y):
	pygame.draw.circle(screen, BLUE, (x, y), 1)

def drawLine(screen, startPos, endPos):
	pygame.draw.line(screen, BLUE, startPos, endPos, 2)


while True:
	for event in pygame.event.get():

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_n:
				currentTool = (currentTool + 1)	% toolCount
		if event.type == pygame.MOUSEBUTTONDOWN:
			isPressed = True
			prevPoint = pygame.mouse.get_pos()
		elif event.type == pygame.MOUSEBUTTONUP:
			isPressed = False

		elif event.type == pygame.MOUSEMOTION and isPressed == True:
			prevPoint = curPoint
			curPoint = pygame.mouse.get_pos()
			
	if currentTool == 0:
		drawLine(screen, prevPoint, curPoint)
	elif currentTool == 1:
		drawRectangle(screen, curPoint[0], curPoint[1], 10, 10)
	pygame.display.flip()