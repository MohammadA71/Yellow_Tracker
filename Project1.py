import cv2
import numpy as np
import pygame

cap = cv2.VideoCapture(0)

pygame.init()
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))

robot_x, robot_y = WIDTH // 2, HEIGHT // 2
robot_speed = 3 

WHITE = (255, 255, 255)
RED = (255, 0, 0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])

    mask = cv2.inRange(hsvImage, lower_yellow, upper_yellow)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    object_x, object_y = None, None

    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        M = cv2.moments(largest_contour)
        if M["m00"] != 0:
            object_x = int(M["m10"] / M["m00"])
            object_y = int(M["m01"] / M["m00"])

            object_x = int(object_x * WIDTH / frame.shape[1])  
            object_y = int(object_y * HEIGHT / frame.shape[0])  
        else:
            object_x, object_y = None, None

    cv2.imshow('Webcam (Press q to exit)', frame)
    cv2.imshow('Yellow Mask', mask)

    screen.fill(WHITE)

    if object_x is not None and object_y is not None:
        if robot_x < object_x:
            robot_x += robot_speed
        elif robot_x > object_x:
            robot_x -= robot_speed
        if robot_y < object_y:
            robot_y += robot_speed
        elif robot_y > object_y:
            robot_y -= robot_speed

    pygame.draw.circle(screen, RED, (robot_x, robot_y), 10)

    pygame.display.flip()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
pygame.quit()
