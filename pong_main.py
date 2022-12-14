from curses import KEY_DOWN
import pygame, sys
from pygame.locals import QUIT

pygame.init()
clock = pygame.time.Clock()

screen_width = 1000
screen_height = 800
rect_width = 10
rect_height = 140
ball_radius = 30
screen = pygame.display.set_mode((screen_width, screen_height))

bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, ball_radius, ball_radius)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, rect_width, rect_height)
opponent = pygame.Rect(10, screen_height/2 - 70, rect_width, rect_height)

ball_speed_x = 10
ball_speed_y = 18

pygame.display.set_caption('Pong!')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1
    if ball.colliderect(player):
        place_hit = (ball.y + ball_radius/2) - (player.y + rect_height/2)
        print(place_hit)
        ball_speed_x *= -1

        ball_speed_y = 20*(place_hit/75)

    
    
    

    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()
