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
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
done = False

def player_animation():
    player.y += player_speed

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
ball_speed_x = 7
ball_speed_y = 7
player_speed = 0


##################################################################################

##################################################################################

##################################################################################



while True:
    success, img = cap.read()

    rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    

    results = hands.process(rgb_img)
    # print(results.multi_hand_landmarks)

    hand_landmark = results.multi_hand_landmarks

    if hand_landmark:

        for hand_lm in hand_landmark:

            for id, lm in enumerate(hand_lm.landmark):

                height, width, channels = img.shape
                centre_x, centre_y = int(lm.x * width), int(lm.y * height)

                print(id, ':', centre_x, centre_y)

                cv.circle(img, (centre_x, centre_y), 25, (255, 0, 255))

            mp_draw.draw_landmarks(img, hand_lm, mp_hands.HAND_CONNECTIONS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed -= 7
            if event.key == pygame.K_DOWN:
                player_speed += 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed += 7
            if event.key == pygame.K_DOWN:
                player_speed -= 7

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
    # screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0),(screen_width / 2, screen_height))

    #convert image so it can be displayed in OpenCV

    #  convert from (width, height, channel) to (height, width, channel)
    view = view.transpose([1, 0, 2])

    #  convert from rgb to bgr
    img_bgr = cv.cvtColor(view, cv.COLOR_RGB2BGR)

    #Display image, clear cell every 0.5 seconds
    cv.imshow("Pong!", img_bgr)


    curr_time = time.time()
    fps = 1/(curr_time - prev_time)
    prev_time = curr_time

    cv.putText(
        img,
        text = str(int(fps)),
        org = (10, 70),
        fontFace = cv.FONT_HERSHEY_COMPLEX,
        fontScale = 3,
        color = (150, 150, 150),
        thickness = 3)



    cv.imshow("Image", img)
    cv.waitKey(1)