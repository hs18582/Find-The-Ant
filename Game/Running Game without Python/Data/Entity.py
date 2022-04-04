import pygame


pygame.init()
fontTitle = pygame.font.Font("Data/Images/YanoneKaffeesatz-Regular.ttf", 100)
fontSmall = pygame.font.Font("Data/Images/YanoneKaffeesatz-Regular.ttf", 70)
fonttiny = pygame.font.SysFont("Data/Images/YanoneKaffeesatz-Regular.ttf", 40)

green = (0, 154, 23)
brown = (85, 63, 35)
black = (0, 0, 0)
white = (255, 255, 255)

yellow = (255, 255, 0)
orange = (255, 128, 0)
red = (255, 0, 0)
pink =(199, 138, 245)
purple = (64, 29, 211)
blue = (21, 105, 172)
light_blue = (41, 211, 251)
grey = (169,169,169)
turquoise = (11, 150, 168)



def writeText(text, font, colour, canvas, x, y):
    textobj = font.render(text, 1, colour)
    textrect = textobj.get_rect()
    textrect.midtop = (x, y)
    canvas.blit(textobj, textrect)
