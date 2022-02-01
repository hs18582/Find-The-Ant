import pygame


pygame.init()
fontTitle = pygame.font.Font("Images/YanoneKaffeesatz-Regular.ttf", 100)
fontSmall = pygame.font.Font("Images/YanoneKaffeesatz-Regular.ttf", 70)


green = (0, 154, 23)
brown = (85, 63, 35)
yellow = (255, 255, 0)
orange = (255, 128, 0)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)


def writeText(text, font, colour, canvas, x, y):
    textobj = font.render(text, 1, colour)
    textrect = textobj.get_rect()
    textrect.midtop = (x, y)
    canvas.blit(textobj, textrect)
