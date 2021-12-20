import pygame
import sys
from pygame.locals import *

n = 5
mainClock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
MainMenu = pygame.Rect(200, 400, 200, 50)
fontTitle = pygame.font.SysFont(None, 100)
font = pygame.font.SysFont(None, 70)
# def colour(option):
# if option == "gree"
green = (0, 154, 23)
brown = (85, 63, 35)
yellow = (255, 255, 0)
orange =(255, 128, 0)
red =(255, 0, 0)
black = (0, 0, 0)


def draw_text(text, font, colour, canvas, x, y):
    textobj = font.render(text, 1, colour)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    canvas.blit(textobj, textrect)
