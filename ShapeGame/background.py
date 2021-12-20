import pygame, random, time, sys
from pygame_functions import *
from pygame.locals import *
from colour import *

def drawBoxes():
    # boxes
    button_circle = pygame.draw.rect(screen, peach,(1, 570, 290, 130))
    button_square = pygame.draw.rect(screen, light_pink,(293, 570, 290, 130))
    button_triangle = pygame.draw.rect(screen, orange,(586, 570, 290, 130))
    button_rectangle = pygame.draw.rect(screen, yellow,(879, 570, 290, 130))
    button_star = pygame.draw.rect(screen, purple,(1, 703, 290, 130)) 
    button_diamond = pygame.draw.rect(screen, red,(293, 703, 290, 130))
    button_oval = pygame.draw.rect(screen, dark_pink,(586, 703, 290, 130))
    button_heart = pygame.draw.rect(screen, blue,(879, 703, 290, 130))    
    
    #circle
    circlesurface = myfont.render('Circle', False, (0, 0, 0))
    circle = screen.blit(circlesurface,(70,600))

    #square
    squaresurface = myfont.render('Square', False, (0, 0, 0))
    square = screen.blit(squaresurface,(350,600))

    #triangle
    trianglesurface = myfont.render('Triangle', False, (0, 0, 0))
    triangle = screen.blit(trianglesurface,(630,600))

    #rectangle
    rectanglesurface = myfont.render('Rectangle', False, (0, 0, 0))
    rectangle = screen.blit(rectanglesurface,(910,600))

    #star
    starsurface = myfont.render('Star', False, (0, 0, 0))
    star = screen.blit(starsurface,(80,720))

    #diamond
    diamondsurface = myfont.render('Diamond', False, (0, 0, 0))
    diamond = screen.blit(diamondsurface,(350,720))

    #oval
    ovalsurface = myfont.render('Oval', False, (0, 0, 0))
    oval = screen.blit(ovalsurface,(680,720))

    #heart
    heartsurface = myfont.render('Heart', False, (0, 0, 0))
    heart = screen.blit(heartsurface,(970,720))
