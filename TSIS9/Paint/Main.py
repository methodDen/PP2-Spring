import pygame
from Indicator import Indicator
from MethodUtils import show_tool, show_color, show_radius, drawLine_for_circle


def main():
    screen = pygame.display.set_mode((800, 600))
    screen.fill((255, 255, 255))
    mode = 'red'

    tool = 'pencil'
    draw_on = False
    last_pos = (0, 0)
    color = (255, 128, 0)
    radius = 10
    ind = Indicator()
    colors = {
        'red': (255, 0, 0),
        'orange': (255, 128, 0),
        'yellow': (255, 255, 0),
        'green': (0, 255, 0),
        'light_blue': (0, 255, 255),
        'blue': (0, 0, 255),
        'violet': (76, 0, 153),
        'white': (255, 255, 255)

    }
    pygame.display.update()
    while True:

        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_1:
                    tool = 'pencil'
                if event.key == pygame.K_2:
                    tool = 'erasor'
                    mode = 'white'
                if event.key == pygame.K_3:
                    tool = 'rectangle'
                if event.key == pygame.K_4:
                    tool = 'circle'
                if event.key == pygame.K_r:
                    mode = 'red'
                if event.key == pygame.K_b:
                    mode = 'blue'
                if event.key == pygame.K_g:
                    mode = 'green'
                if event.key == pygame.K_y:
                    mode = 'yellow'
                if event.key == pygame.K_v:
                    mode = 'violet'
                if event.key == pygame.K_o:
                    mode = 'orange'
                if event.key == pygame.K_a:
                    mode = 'light_blue'

                if event.key == pygame.K_s:
                    rect = pygame.Rect(0, 100, 800, 500)
                    sub = screen.subsurface(rect)
                    pygame.image.save(sub, 'pic.png')



                if event.key == pygame.K_UP:
                    radius += 1
                if event.key == pygame.K_DOWN:
                    radius -= 1


            if event.type == pygame.MOUSEBUTTONDOWN:
                color = colors[mode]
                if tool == 'circle':
                    pygame.draw.circle(screen, color, event.pos, radius)
                if tool == 'rectangle':
                    pygame.draw.rect(screen, color, (event.pos[0], event.pos[1], radius * 2, radius * 2))
                draw_on = True
            if event.type == pygame.MOUSEBUTTONUP:
                draw_on = False
            if event.type == pygame.MOUSEMOTION:
                if draw_on:
                    if tool == 'pencil':
                        pygame.draw.line(screen, color, last_pos, event.pos, radius)
                    if tool == 'erasor':
                        pygame.draw.rect(screen, color, (event.pos[0], event.pos[1], radius * 2, radius * 2))
                    if tool == 'circle':
                        drawLine_for_circle(screen, last_pos, event.pos, radius, color)
                    if tool == 'rectangle':
                        pygame.draw.rect(screen, color, (event.pos[0], event.pos[1], radius * 2, radius * 2))
                last_pos = event.pos
        screen.fill((255, 255, 255), (0, 0, 800, 100))
        ind.draw(screen, colors[mode])
        show_tool(100, 25, tool, screen)
        if tool == 'erasor':
            show_color(100, 50, '-', screen)
        else:
            show_color(100, 50, mode, screen)
        if radius <= 0:
            radius = 0
        show_radius(100, 75, radius, screen)
        pygame.display.flip()
    pygame.quit()

main()

