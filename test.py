import pygame
import cv2, time

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
x = 30
y = 30

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        color = (255, 100, 0)
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
        
        pygame.display.flip()

        #convert image so it can be displayed in OpenCV
        view = pygame.surfarray.array3d(screen)

        #  convert from (width, height, channel) to (height, width, channel)
        view = view.transpose([1, 0, 2])

        #  convert from rgb to bgr
        img_bgr = cv2.cvtColor(view, cv2.COLOR_RGB2BGR)

        #Display image, clear cell every 0.5 seconds
        cv2.imshow("test", img_bgr)
        time.sleep(0.5)
