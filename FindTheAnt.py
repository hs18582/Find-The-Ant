import pygame
from pygame.locals import *


def main_menu():
    mainClock = pygame.time.Clock()
    pygame.init()  # start the program
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # set screen size to full screen

    while True:
        screen.fill((0, 0, 0))  # fill screen with colour black

        False
        # 1 - left click, 2 - middle click, 3 - right click, 4 - scroll up, 5 - scroll down
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                # if left button click then make true
                if event.button == 1:
                    True

    pygame.display.update()
    mainClock.tick(60)


main_menu()
