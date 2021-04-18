import json

import pygame, sys
from Utils import SNAKE_COL, WIDTH, HEIGHT, collision_screen, FPS, DEFAULT_SNAKE_PARAMS
from Snake import Snake
from Food import Food
from Brick import Brick
from MethodUtils import collision, collisionSec, has_snakes_collided, welcome, game_over, show_score, show_level, brick_snake_collision, wall_snake_collision, game_over_multiplayer

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()


def game_loop():

    left_wall = Brick()
    left_wall.x = 0
    left_wall.y = 0
    left_wall.width = 10
    left_wall.height = HEIGHT

    right_wall = Brick()
    right_wall.x = WIDTH - 10
    right_wall.y = 0
    right_wall.width = 10
    right_wall.height = HEIGHT

    upper_wall = Brick()
    upper_wall.y = 0
    upper_wall.x = 0
    upper_wall.height = 10
    upper_wall.width = WIDTH

    bottom_wall = Brick()
    bottom_wall.y = HEIGHT - 10
    bottom_wall.x = 0
    bottom_wall.height = 10
    bottom_wall.width = WIDTH

    brick_li = []
    bri_js_li = []
    is_multiplayer = False
    running = True
    start_screen = True

    # Create snakes
    snake = Snake()
    snake_sec = Snake()
    snake_sec.dx = -5
    snake_sec.elements = [[300, 400], [320, 400], [340, 400]]

    # Create food
    food = Food()

    while running:
        mil = clock.tick(FPS)
        while start_screen:
            welcome(screen, (0, 0, 0), (255, 255, 255))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()


                    if event.key == pygame.K_n:

                        # second Snake
                        snake_sec.visible = False

                        snake = Snake()
                        brick_li.clear()

                        bri_js_li.clear()
                        st = json.dumps(brick_li)
                        with open(r'brickcache.txt', 'w') as file:
                            file.write(st)
                        start_screen = False
                        snake.visible = True

                    if event.key == pygame.K_m:
                        is_fir_score_assigned = False
                        is_sec_score_assigned = False
                        x_score_sec = 510
                        y_score_sec = 470


                        snake = Snake()
                        snake_sec = Snake()
                        # brick_li.clear()
                        # reinitializing second snake
                        snake_sec.dx = -5
                        snake_sec.elements = [[300, 400], [320, 400], [340, 400]]
                        start_screen = False
                        snake.visible = True
                        snake_sec.visible = True
                    if event.key == pygame.K_c:
                        # second Snake
                        snake_sec.visible = False
                        # is_multiplayer = False
                        brick_li.clear()
                        snake = Snake()
                        with open(r'cache.txt', 'r') as file:
                            st = file.read()

                        data = json.loads(st)
                        snake.score = int(data["score"])
                        snake.visible = data["visible"]
                        snake.is_add = data["is_add"]
                        snake.dx = data["dx"]
                        snake.dy = data["dy"]
                        snake.size = data["size"]
                        snake.thickness = data["thickness"]
                        snake.level = int(data["level"])
                        snake.elements = data["elements"]

                        with open(r'brickcache.txt', 'r') as bri_file:
                            st = bri_file.read()
                        bri_li_file = json.loads(st)

                        for bri in bri_li_file:
                            b = Brick()
                            b.x = bri["x"]
                            b.y = bri["y"]
                            b.width = bri["width"]
                            b.height = bri["height"]
                            brick_li.append(b)

                        start_screen = False
                        snake.visible = True



                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if snake.visible:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        snake.dx = 5
                        snake.dy = 0
                    if event.key == pygame.K_LEFT:
                        snake.dx = -5
                        snake.dy = 0
                    if event.key == pygame.K_UP:
                        snake.dx = 0
                        snake.dy = -5
                    if event.key == pygame.K_DOWN:
                        snake.dx = 0
                        snake.dy = 5

            if snake_sec.visible:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        snake_sec.dx = 5
                        snake_sec.dy = 0
                    if event.key == pygame.K_a:
                        snake_sec.dx = -5
                        snake_sec.dy = 0
                    if event.key == pygame.K_w:
                        snake_sec.dx = 0
                        snake_sec.dy = -5
                    if event.key == pygame.K_s:
                        snake_sec.dx = 0
                        snake_sec.dy = 5

        collision(food, snake)
        if snake_sec.visible:
            collisionSec(food, snake_sec)

        if snake_sec.visible:
            if has_snakes_collided(snake, snake_sec):
                while collision_screen:
                    game_over(screen, (0, 0, 0), (255, 255, 255))
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                game_loop()

                            if event.key == pygame.K_q:
                                pygame.quit()
                                sys.exit()



        screen.fill((165, 206, 216))
        left_wall.draw(screen)
        right_wall.draw(screen)
        upper_wall.draw(screen)
        bottom_wall.draw(screen)

        snake.move()
        snake.draw(screen)
        if snake_sec.visible:
            is_out = "OUT"
            snake_sec.move()
            snake_sec.draw(screen)
            show_score(x_score_sec, y_score_sec, snake_sec.score, screen)

            if wall_snake_collision(snake_sec, right_wall) or wall_snake_collision(snake_sec, left_wall) \
                    or wall_snake_collision(snake_sec, bottom_wall) or wall_snake_collision(snake_sec, upper_wall):
                if not is_fir_score_assigned:
                    fir_score = snake.score
                    is_fir_score_assigned = True
                snake_sec.score = is_out
                x_score_sec = 480
                y_score_sec = 470
                snake_sec.thickness = 0

            if wall_snake_collision(snake, right_wall) or wall_snake_collision(snake, left_wall) \
                    or wall_snake_collision(snake, bottom_wall) or wall_snake_collision(snake, upper_wall):
                if not is_sec_score_assigned:
                    sec_score = snake_sec.score
                    is_sec_score_assigned = True
                snake.score = is_out
                snake.thickness = 0

            if snake_sec.score == is_out and snake.score == is_out:
                copy_snake = snake
                copy_snake_sec = snake_sec
                copy_snake.score = fir_score
                copy_snake_sec.score = sec_score
                while collision_screen:
                    game_over_multiplayer(screen, (0, 0, 0), (255, 255, 255), copy_snake, copy_snake_sec)
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                game_loop()

                            if event.key == pygame.K_q:
                                pygame.quit()
                                sys.exit()

        food.draw(screen)
        show_score(10, 15, snake.score, screen)
        if not snake_sec.visible:
            show_level(10, 45, snake.level, screen)

        if not snake_sec.visible:
            while len(brick_li) < snake.level - 1:
                b = Brick()
                if b not in brick_li:
                    brick_li.append(b)
                print(brick_li)
        if not snake_sec.visible:
            for brick in brick_li:
                brick.draw(screen)

        if not snake_sec.visible:
            # Ооох, спагетти...
            if wall_snake_collision(snake, right_wall) or wall_snake_collision(snake, left_wall) \
                    or wall_snake_collision(snake, bottom_wall) or wall_snake_collision(snake, upper_wall):

                copy_snake = snake
                snake = Snake()
                brick_li.clear()
                bri_js_li.clear()
                st = json.dumps(brick_li)
                with open(r'brickcache.txt', 'w') as file:
                    file.write(st)
                with open(r'cache.txt', 'w') as cache_file:
                    cache_file.write(DEFAULT_SNAKE_PARAMS)

                while collision_screen:
                    game_over(screen, (0, 0, 0), (255, 255, 255), copy_snake)
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                game_loop()

                            if event.key == pygame.K_q:
                                pygame.quit()
                                sys.exit()


        if not snake_sec.visible:
            if brick_snake_collision(snake, brick_li):
                copy_snake = snake
                snake = Snake()
                brick_li.clear()
                bri_js_li.clear()
                st = json.dumps(brick_li)
                with open(r'brickcache.txt', 'w') as file:
                    file.write(st)
                with open(r'cache.txt', 'w') as cache_file:
                    cache_file.write(DEFAULT_SNAKE_PARAMS)

                while collision_screen:
                    game_over(screen, (0, 0, 0), (255, 255, 255), copy_snake)
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                game_loop()

                            if event.key == pygame.K_q:
                                pygame.quit()
                                sys.exit()


        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            start_screen = True
            if not snake_sec.visible:
                cache = {}
                cache["size"] = snake.size
                cache["thickness"] = snake.thickness
                cache["dx"] = snake.dx
                cache["dy"] = snake.dy
                cache["is_add"] = snake.is_add
                cache["visible"] = snake.visible
                cache["score"] = snake.score
                cache["level"] = snake.level
                cache["elements"] = snake.elements

                for brick in brick_li:
                    bri = {}
                    bri["width"] = brick.width
                    bri["height"] = brick.height
                    bri["x"] = brick.x
                    bri["y"] = brick.y
                    if bri not in bri_js_li:
                        bri_js_li.append(bri)


                jstring = json.dumps(cache)
                j_bri_string = json.dumps(bri_js_li)
                with open(r'cache.txt', 'w') as file:
                    file.write(jstring)

                with open(r'brickcache.txt', 'w') as bri_file:
                    bri_file.write(j_bri_string)

        pygame.display.flip()

game_loop()
