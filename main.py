# img = pygame.image.load("Background.png").convert()
# pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])
'''
from pygame.locals import *

flags = FULLSCREEN | DOUBLEBUF
screen = pygame.display.set_mode(resolution, flags, 16)
'''
import math

import pygame
from Objects import Bullet, Cannon

# setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray")
    # command=input("enter angle:speed, like 45:10 : ")
    command = "45:10"  # placeholder input

    angle = float(command[0:command.find(":")])
    speed = float(command[command.find(":") + 1:len(command)])
    vx = speed * math.cos(angle)
    vy = speed * math.sin(angle)

    # creates a bullet whenever a command has been made, making it go zoom
    b = Bullet(200, 200, vx, vy, 5)

    # ----render stuff here-----
    while b.x < 500:  # replace with "until bullet hits something"
        b.draw(screen)
        b.update(1)

        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60
    # --------------------------

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
