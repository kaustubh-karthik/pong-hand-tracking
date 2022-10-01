import cv2 as cv
import mediapipe as mp
import time, pygame, sys


cap = cv.VideoCapture(1)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

mp_draw = mp.solutions.drawing_utils

# Variables
screen_width = 1080
screen_height = 800

def get_hand_landmarks():
    success, img = cap.read()

    rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)


    results = hands.process(rgb_img)
    # print(results.multi_hand_landmarks)

    raw_hand_landmark = results.multi_hand_landmarks
    hand_landmarks = []

    if raw_hand_landmark:
        for hand_lm in raw_hand_landmark:
            for id, lm in enumerate(hand_lm.landmark):
                hand_landmarks.append((int(lm.x * screen_width), int(lm.y * screen_height)))

    return hand_landmarks
