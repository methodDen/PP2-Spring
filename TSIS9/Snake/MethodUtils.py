import pygame
import random
from Utils import WIDTH, HEIGHT
from Utils import ANNOUNCE_FONT, OPTION_FONT, SCORE_FONT


def show_score(x, y, score, screen):
    show = SCORE_FONT.render(f'Score: {score}', True, (50, 28, 217))
    screen.blit(show, (x, y))


def show_level(x, y, level, screen):
    level = SCORE_FONT.render(f'Level: {level}', True, (50, 28, 217))
    screen.blit(level, (x, y))


def collision(food, snake):
    if (food.x in range(snake.elements[0][0] - 16, snake.elements[0][0])) and ( # change
            food.y in range(snake.elements[0][1] - 16, snake.elements[0][1])):
        snake.is_add = True
        food.x = random.randint(50, WIDTH - 70)
        food.y = random.randint(50, HEIGHT - 70)


def collisionSec(food, snakeSec):
    if (food.x in range(snakeSec.elements[0][0] - 16, snakeSec.elements[0][0])) and (
            food.y in range(snakeSec.elements[0][1] - 16, snakeSec.elements[0][1])):
        snakeSec.is_add = True
        food.x = random.randint(50, WIDTH - 70)
        food.y = random.randint(50, HEIGHT - 70)


# def game_over(screen, snake):
#     # pygame.display.flip()
#     screen.fill((255, 0, 0))
#     txt = font.render('GAME OVER!', True, (255, 255, 255))
#     my_score = font.render('Total score: ' + str(snake.score), True, (255, 255, 255))
#     screen.blit(txt, (200, 200))
#     screen.blit(my_score, (200, 300))
#     pygame.display.flip()
#     time.sleep(3)
#     pygame.quit()


def is_in_walls(snake):
    return snake.elements[0][0] > WIDTH - 25 or snake.elements[0][0] < 30


def has_snakes_collided(snake, snakeSec):
    for i in range(snake.size):
        for j in range(snakeSec.size):
            if (snake.elements[i][0] in range(snakeSec.elements[j][0] - 10, snakeSec.elements[j][0])
                    and snake.elements[i][1] in range(snakeSec.elements[j][1] - 10, snakeSec.elements[j][1])):
                return True


def brick_snake_collision(snake, brick_list):
    for i in range(snake.size):
        for brick in brick_list:
            if (snake.elements[i][0] in range(brick.x, brick.x + brick.width) and snake.elements[i][1]
                    in range(brick.y, brick.y + brick.height)):
                return True


def wall_snake_collision(snake, wall):
    for i in range(snake.size):
        if (snake.elements[i][0] in range(wall.x, wall.x + wall.width) and
        snake.elements[i][1] in range(wall.y, wall.y + wall.height)):
            return True


def welcome(screen, color, msg_color):
    screen.fill(color)
    mesg = ANNOUNCE_FONT.render("Snake v 1.0 by Dan Abs", True, msg_color)
    cont = OPTION_FONT.render("""Continue (press c) """, True, msg_color)
    new_game = OPTION_FONT.render("""New Game (press n)""", True, msg_color)
    multiplayer = OPTION_FONT.render("""Multiplayer (press m) """, True, msg_color)
    quit = OPTION_FONT.render("Quit (press q)", True, msg_color)
    screen.blit(mesg, (WIDTH / 2 - 150, HEIGHT / 2 - 125))
    screen.blit(cont, (WIDTH / 2 - 125, HEIGHT / 2 - 75))
    screen.blit(new_game, (WIDTH / 2 - 125, HEIGHT / 2 - 25))
    screen.blit(multiplayer, (WIDTH / 2 - 125, HEIGHT / 2 + 25))
    screen.blit(quit, (WIDTH / 2 - 125, HEIGHT / 2 + 75))



def game_over(screen, color, msg_color, snake):
    screen.fill(color)
    mesg = ANNOUNCE_FONT.render("GAME OVER!", True, msg_color)
    back = OPTION_FONT.render("""Back to Main Menu (press esc)""", True, msg_color)
    quit = OPTION_FONT.render("""Quit game (press q)""", True, msg_color)
    score = OPTION_FONT.render(f'Final Score: {snake.score}', True, msg_color)
    level = OPTION_FONT.render(f'Level: {snake.level}', True, msg_color)
    screen.blit(mesg, (WIDTH / 2 - 150, HEIGHT / 2 - 125))
    screen.blit(score, (WIDTH / 2 - 125, HEIGHT / 2 - 75))

    screen.blit(level, (WIDTH / 2 - 125, HEIGHT / 2 - 25))
    screen.blit(back, (WIDTH / 2 - 125, HEIGHT / 2 + 25))
    screen.blit(quit, (WIDTH / 2 - 125, HEIGHT / 2 + 75))


def game_over_multiplayer(screen, color, msg_color, snake, snake_sec):
    screen.fill(color)
    mesg = ANNOUNCE_FONT.render("GAME OVER!", True, msg_color)
    back = OPTION_FONT.render("""Back to Main Menu (press esc)""", True, msg_color)
    quit = OPTION_FONT.render("""Quit game (press q)""", True, msg_color)
    score = OPTION_FONT.render(f'Player 1 final score: {snake.score}', True, msg_color)
    sec_score = OPTION_FONT.render(f'Player 2 final score: {snake_sec.score}', True, msg_color)
    screen.blit(mesg, (WIDTH / 2 - 150, HEIGHT / 2 - 125))
    screen.blit(score, (WIDTH / 2 - 125, HEIGHT / 2 - 75))

    screen.blit(sec_score, (WIDTH / 2 - 125, HEIGHT / 2 - 25))
    screen.blit(back, (WIDTH / 2 - 125, HEIGHT / 2 + 25))
    screen.blit(quit, (WIDTH / 2 - 125, HEIGHT / 2 + 75))



