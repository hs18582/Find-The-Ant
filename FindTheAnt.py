from Entity import *
from pygame.locals import *
import sys, random


class Init:
    def __init__(self):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.running = True
        self.mainClock = pygame.time.Clock()


Init = Init()


########################################################################################################################
########################################################################################################################
########################################################################################################################
def Game():
    pygame.init()
    while Init.running:
        Init.screen.fill(black)
        list_buttons = Grid()

    pygame.display.update()
    Init.mainClock.tick(60)


def Grid():
    # CREATING A LIST USING LIST COMPREHENSION
    list_buttons = [
        [pygame.Rect(((Init.width / Init.getN()) * i) + ((Init.screen.get_width() / 2) - 300),
                     ((Init.height / Init.getN()) * j) + ((Init.screen.get_height() / 2) - 300),
                     (Init.width / Init.getN()) - 2,
                     (Init.height / Init.getN()) - 2) for i in
         range(Init.getN())] for j in range(Init.getN())]

    # LOOP TO CREATE A N BY N GRID
    for i in range(len(list_buttons)):
        for j in range(len(list_buttons[i])):
            pygame.draw.rect(Init.screen, Init.colour[i][j], list_buttons[i][j])  # CREATING A GREEN RECTANGLE

    return list_buttons


########################################################################################################################
class Rules:
    pass


########################################################################################################################
class HighScore:
    pass


########################################################################################################################
def main_menu():
    mainClock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    while True:

        screen.fill(black)
        ant = pygame.image.load('Images/antMain.png')

        writeText("Find The Ant", fontTitle, brown, screen, 3 * screen.get_width() / 4, screen.get_height() / 20)
        mx, my = pygame.mouse.get_pos()

        click = False
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        Start = pygame.Rect(screen.get_width() / 20, screen.get_height() / 8, screen.get_width() / 2,
                            screen.get_height() / 8)
        Instruction = pygame.Rect(screen.get_width() / 20, (screen.get_height() / 8 + (screen.get_height() / 4)),
                                  (3 * screen.get_width()) / 8, screen.get_height() / 8)
        Highscore = pygame.Rect(screen.get_width() / 20, (screen.get_height() / 8 + (screen.get_height() / 2)),
                                (screen.get_width()) / 4, screen.get_height() / 8)
        Quit = pygame.Rect(screen.get_width() / 20, (screen.get_height() / 8 + (3 * screen.get_height() / 4)),
                           (screen.get_width()) / 8, screen.get_height() / 8)

        if Start.collidepoint((mx, my)):
            if click:
                Game()
        if Instruction.collidepoint((mx, my)):
            if click:
                Rules()
        if Highscore.collidepoint((mx, my)):
            if click:
                HighScore()
        if Quit.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(screen, green, Start)
        writeText("Start", fontSmall, brown, screen, screen.get_width() / 10, screen.get_height() / 6)

        pygame.draw.rect(screen, brown, Instruction)
        writeText("Rules", fontSmall, green, screen, screen.get_width() / 10, screen.get_height() / 2.4)

        pygame.draw.rect(screen, green, Highscore)
        writeText("Highscore", fontSmall, brown, screen, screen.get_width() / 7.5, screen.get_height() / 1.5)

        pygame.draw.rect(screen, brown, Quit)
        writeText("Exit", fontSmall, green, screen, screen.get_width() / 11, screen.get_height() / 1.1)

        screen.blit(ant, (screen.get_width() / 2, (screen.get_height() / 8) + screen.get_height() / 3.5))

        pygame.display.update()
        mainClock.tick(60)


main_menu()
