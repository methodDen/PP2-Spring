import pygame, sys
from pygame.locals import *
import random, time

pygame.init()
FPS = 60
FramePerSec = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# randomly changing speed from 1 to 5
SCORE = 0
COLLECTED_COINS = 0
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
background = pygame.image.load("AnimatedStreet.png")
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
COIN_CNT = 0

class Enemy(pygame.sprite.Sprite):

	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("Enemy.png")
		self.surf = pygame.Surface((42, 70))
		self.rect = self.surf.get_rect(center = (random.randint(40, SCREEN_WIDTH - 40), 0))

	def move(self):
		global SCORE
		SPEED = random.randint(1, 10)
		self.rect.move_ip(0, SPEED)
		if (self.rect.top > 600):
			SCORE += 1
			self.rect.top = 0
			self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("Player.png")
		self.surf = pygame.Surface((40, 75))
		self.rect = self.surf.get_rect(center = (160, 520))




	def move(self):
		pressed_keys = pygame.key.get_pressed()

		if pressed_keys[K_UP]:
			self.rect.move_ip(0, -5)
		if pressed_keys[K_DOWN]:
			self.rect.move_ip(0, 5)

		if self.rect.left > 0:
			if pressed_keys[K_LEFT]:
				self.rect.move_ip(-5, 0)
		if self.rect.right < SCREEN_WIDTH:
			if pressed_keys[K_RIGHT]:
				self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("dollar.png")
		self.surf = pygame.Surface((32, 32))
		self.rect = self.surf.get_rect(center = (random.randint(32, SCREEN_WIDTH - 32), random.randint(32, SCREEN_HEIGHT - 32)))
		self.last = pygame.time.get_ticks()
		self.cooldown = 4000

	def move(self):
		pass

	def show(self):
		now = pygame.time.get_ticks()
		if now - self.last >= self.cooldown:
			self.last = now
			self.rect = self.surf.get_rect(center = (random.randint(32, SCREEN_WIDTH - 32), random.randint(32, SCREEN_HEIGHT - 32)))
	def show_after_collision(self):
		global COLLECTED_COINS
		COLLECTED_COINS += 1
		self.rect = self.surf.get_rect(center = (random.randint(32, SCREEN_WIDTH - 32), random.randint(32, SCREEN_HEIGHT - 32)))

P1 = Player()
E1 = Enemy()
P2 = Player()
C1 = Coin()
C2 = Coin()
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
coins.add(C2)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
COIN_CNT += 1
all_sprites.add(C2)
COIN_CNT += 1
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
SPAWN_ENEMY = pygame.USEREVENT + 2
pygame.time.set_timer(SPAWN_ENEMY, 5000)

while True:
	for event in pygame.event.get():
		# if event.type == INC_SPEED:
		# 	SPEED += 2

		if event.type == QUIT:
			pygame.quit()
			sys.exit()

		if event.type == SPAWN_ENEMY:
			e = Enemy()
			enemies.add(e)
			all_sprites.add(e)

	DISPLAYSURF.blit(background, (0, 0))
	scores = font_small.render(str(SCORE), True, BLACK)
	coins_collected = font_small.render(f"Coins: {COLLECTED_COINS // COIN_CNT}$", True, BLACK)
	DISPLAYSURF.blit(scores, (10, 10))
	DISPLAYSURF.blit(coins_collected, (290, 10))

	for entity in all_sprites:
		DISPLAYSURF.blit(entity.image, entity.rect)
		entity.move()

	if pygame.sprite.spritecollideany(P1, enemies):
		pygame.mixer.Sound('crash.wav').play()
		time.sleep(0.5)
		DISPLAYSURF.fill(RED)
		DISPLAYSURF.blit(game_over, (30, 250))
		pygame.display.update()
		for entity in all_sprites:
			entity.kill()
		time.sleep(2)
		pygame.quit()
		sys.exit()

	for coin in coins:
		coin.show()

	if pygame.sprite.spritecollideany(P1, coins):
		for coin in coins:
			coin.show_after_collision()

	pygame.display.update()
	FramePerSec.tick(FPS)
