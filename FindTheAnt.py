from Entity import *
from pygame.locals import *
import sys, random

class Init:
    def __init__(self):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.n = 0
        self.running = True
        self.mainClock = pygame.time.Clock()
        self.colour = []
        self.antLocation = []
        self.antFound = False
        self.queueLocation = [[None for j in range(3)] for i in range(3)]
        self.queueClicked = [[] for i in range(3)]

    def setN(self, n):
        self.n = n
        self.colour = [[green for i in range(n)] for j in range(n)]
        self.antLocation = [random.randint(0, n - 1), random.randint(0, n - 1)]

    def getN(self):
        return self.n


Init = Init()
########################################################################################################################
########################################################################################################################
########################################################################################################################
def Game():
    Init.setN(3) # setting a 3x3 grid
    pygame.init()
    while Init.running:
        Init.screen.fill(black)
        mx, my = pygame.mouse.get_pos()
        list_buttons = Grid()
        count = 0

        if Init.antFound:
            x = ((Init.width / (2 * Init.getN()) + ((Init.screen.get_width() / 2) - 300)) + (
                    Init.antLocation[1] * (Init.width / Init.getN()))) - 25
            y = ((Init.height / (2 * Init.getN()) + ((Init.screen.get_width() / 2) - 625)) + (
                    Init.antLocation[0] * (Init.height / Init.getN()))) - 43

            Init.screen.blit(Init.ant, (x, y))
            Init.running = False
            pygame.display.update()
            pygame.time.delay(2000)
            Winner()

        click = False
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        for i in range(Init.getN()):
            for j in range(Init.getN()):
                if list_buttons[i][j].collidepoint((mx, my)):
                    if click and [i, j] not in Init.queueClicked:
                        ButtonOpen(i, j)

                        if Init.queueClicked[2]:
                            ButtonClose(Init.queueClicked[2][0], Init.queueClicked[2][1])
                        for z in range(2, 0, -1):
                            Init.queueClicked[z] = Init.queueClicked[z - 1]
                        Init.queueClicked[0] = [i, j]
                        count += 1
                        Init.scoreList.append(count)

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

def ButtonOpen(x, y):
    Init.colour[x][y] = brown
    if Init.antLocation == [x, y]:
        Init.antFound = True


def ButtonClose(x, y):
    Init.colour[x][y] = green



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
