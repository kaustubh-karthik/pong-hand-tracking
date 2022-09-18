
import cv2 as cv
import mediapipe as mp
import time, pygame, sys

cap = cv.VideoCapture(1)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

mp_draw = mp.solutions.drawing_utils

prev_time = 0

##################################################################################

##################################################################################

##################################################################################



pygame.init()
screen_width = 1080
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
done = False

def player_animation():
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height
    


# General setup
#clock = pygame.time.Clock()

# Main Window
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')

# Colors
light_grey = (200,200,200)
bg_color = pygame.Color('grey12')

# Game Rectangles
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10,140)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10,140)

# Game Variables
ball_speed_x = 13
ball_speed_y = 13
opponent_speed = 15

##################################################################################

##################################################################################

##################################################################################



while True:
    success, img = cap.read()

    rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    screen.fill(bg_color)


    results = hands.process(rgb_img)
    # print(results.multi_hand_landmarks)

    hand_landmark = results.multi_hand_landmarks

    if hand_landmark:

        for hand_lm in hand_landmark:

            for id, lm in enumerate(hand_lm.landmark):

                centre_x, centre_y = int(lm.x * screen_width), int(lm.y * screen_height)

                # print(id, ':', centre_x, centre_y)

                pygame.draw.circle(screen, (255, 0, 255), (centre_x, centre_y), 5)

            index_finger = hand_lm.landmark[8]
            player.y = index_finger.y * screen_height


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # Game Logic

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1

    if ball.colliderect(player):
        place_hit = ball.y - (player.y + 70)
        ball_speed_y = 20*(place_hit/75)
        ball_speed_x *= -1
        
    player_animation()

    # Visuals
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0),(screen_width / 2, screen_height))


    pygame.display.flip()

