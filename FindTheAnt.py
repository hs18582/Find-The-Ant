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
        self.width = 600
        self.height = 600
        self.antLocation = []
        self.antFound = False
        self.queueLocation = [[None for j in range(3)] for i in range(3)]
        self.queueClicked = [[] for i in range(3)]
        self.ant = pygame.image.load('Images/ant.png')
        self.scoreList = []

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
    Init.setN(3)  # setting a 3x3 grid
    pygame.init()
    while Init.running:
        Init.screen.fill(black)
        mx, my = pygame.mouse.get_pos()
        list_buttons = Grid()
        count = 0
        start_ticks = pygame.time.get_ticks()

        seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # calculate how many seconds
        if seconds > 180:  # if more than 10 seconds close the game
            pygame.display.update()
            Loser()

        Tscore = len(Init.scoreList)
        writeText("Score:  " + str(Tscore), fontSmall, green, Init.screen, 3 * Init.screen.get_width() / 4,
                  Init.screen.get_height() / 20)

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
        else:
            if Init.queueLocation[2][2] == True and [Init.queueLocation[2][0],
                                                     Init.queueLocation[2][1]] in Init.queueClicked:
                x = (Init.width / (2 * Init.getN()) + ((Init.screen.get_width() / 2) - 300)) + (
                            Init.queueLocation[2][1] * (Init.width / Init.getN()))
                y = (Init.height / (2 * Init.getN()) + ((Init.screen.get_width() / 2) - 625)) + (
                            Init.queueLocation[2][0] * (Init.height / Init.getN()))
                pygame.draw.circle(Init.screen, red, (x, y), 20)

            if Init.queueLocation[1][2] == True and [Init.queueLocation[1][0],
                                                     Init.queueLocation[1][1]] in Init.queueClicked:
                x = (Init.width / (2 * Init.getN()) + ((Init.screen.get_width() / 2) - 300)) + (
                            Init.queueLocation[1][1] * (Init.width / Init.getN()))
                y = (Init.height / (2 * Init.getN()) + ((Init.screen.get_width() / 2) - 625)) + (
                            Init.queueLocation[1][0] * (Init.height / Init.getN()))
                pygame.draw.circle(Init.screen, orange, (x, y), 20)

            if Init.queueLocation[0][2] == True and [Init.queueLocation[0][0],
                                                     Init.queueLocation[0][1]] in Init.queueClicked:
                x = (Init.width / (2 * Init.getN()) + ((Init.screen.get_width() / 2) - 300)) + (
                            Init.queueLocation[0][1] * (Init.width / Init.getN()))
                y = (Init.height / (2 * Init.getN()) + ((Init.screen.get_width() / 2) - 625)) + (
                            Init.queueLocation[0][0] * (Init.height / Init.getN()))
                pygame.draw.circle(Init.screen, yellow, (x, y), 20)

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

                        if not Init.antFound:
                            MoveAnt()

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


def MoveAnt():
    x, y = Init.antLocation[0], Init.antLocation[1]
    possiblemoves = [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]
    if possiblemoves[0][0] == Init.getN():
        possiblemoves[0][0] = 0

    if possiblemoves[1][0] == -1:
        possiblemoves[1][0] = Init.getN() - 1

    if possiblemoves[2][1] == Init.getN():
        possiblemoves[2][1] = 0

    if possiblemoves[3][1] == -1:
        possiblemoves[3][1] = Init.getN() - 1

    for i in range(3, -1, -1):
        if possiblemoves[i] in Init.queueClicked:
            possiblemoves.pop(i)

    index = random.randint(0, len(possiblemoves) - 1)

    Init.antLocation = possiblemoves[index]


def Pheromone():
    droppingPoint = 50
    # is the tipping point if number > 50 then drop if less hold( if num = 50 then 50% of being dropped

    for z in range(2, 0, -1):
        Init.queueLocation[z] = Init.queueLocation[z - 1]
    if random.randint(0, 100) >= droppingPoint:
        if [Init.antLocation[0], Init.antLocation[1], True] == Init.queueLocation[1]:
            Init.queueLocation[1][2] = False
        if [Init.antLocation[0], Init.antLocation[1], True] == Init.queueLocation[2]:
            Init.queueLocation[2][2] = False
        Init.queueLocation[0] = [Init.antLocation[0], Init.antLocation[1], True]
    else:
        Init.queueLocation[0] = [Init.antLocation[0], Init.antLocation[1], False]


def playAgain():
    Init.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    Init.running = True
    Init.mainClock = pygame.time.Clock()
    Init.colour = [[green for i in range(Init.getN())] for j in range(Init.getN())]
    Init.width = 600
    Init.height = 600
    Init.antLocation = [random.randint(0, Init.getN() - 1), random.randint(0, Init.getN() - 1)]
    Init.antFound = False
    Init.queueLocation = [[None for j in range(3)] for i in range(3)]
    Init.queueClicked = [[] for i in range(3)]
    Init.ant = pygame.image.load('Images/ant.png')
    Init.scoreList = []
    # Init.antmini = pygame.image.load('Images/antMini.png')  # https://www.pinclipart.com/maxpin/iTbwbmJ/


########################################################################################################################
def Winner():
    pygame.init()

    mainClock = pygame.time.Clock()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    Tscore = len(Init.scoreList)

    while True:
        screen.fill((0, 0, 0))

        click = False
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        writeText("Your score is: ", fontTitle, (255, 255, 255), screen, screen.get_width() / 2,
                  8 * screen.get_height() / 20)
        writeText(str(Tscore), fontTitle, (255, 255, 255), screen, screen.get_width() / 2,
                  screen.get_height() / 2)

        # Creating and Drawing back button
        mx, my = pygame.mouse.get_pos()
        Back = pygame.Rect(3 * screen.get_width() / 4, 7 * screen.get_height() / 10, screen.get_width() / 4,
                           screen.get_height() / 10)
        if Back.collidepoint((mx, my)):
            if click:
                pygame.time.delay(500)
                main_menu()
        pygame.draw.rect(screen, green, Back)
        writeText("Back", fontSmall, brown, screen, 4 * screen.get_width() / 5, 14.5 * screen.get_height() / 20)

        Reset = pygame.Rect(0 * screen.get_width(), 7 * screen.get_height() / 10, screen.get_width() / 4,
                            screen.get_height() / 10)
        if Reset.collidepoint((mx, my)):
            if click:
                pygame.time.delay(500)
                playAgain()
                Game()
        pygame.draw.rect(screen, green, Reset)
        writeText("Play Again?", fontSmall, brown, screen, 1 * screen.get_width() / 10, 14.5 * screen.get_height() / 20)

        pygame.display.update()
        mainClock.tick(60)
########################################################################################################################
def Loser():
    mainClock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    LoserRunning = True
    antmini = pygame.image.load('Images/antMini.png')  # https://www.pinclipart.com/maxpin/iTbwbmJ/

    while LoserRunning:
        screen.fill((0, 0, 0))

        writeText("Time's Up!", fontTitle, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 20)
        writeText("Sorry you didnt find the ant in time! ", fontTitle, (255, 255, 255), screen, screen.get_width() / 2,
                  8 * screen.get_height() / 20)

        click = False
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # Creating and Drawing back button
        mx, my = pygame.mouse.get_pos()
        Back = pygame.Rect(3 * screen.get_width() / 4, 7 * screen.get_height() / 10, screen.get_width() / 4,
                           screen.get_height() / 10)
        if Back.collidepoint((mx, my)):
            if click:
                pygame.time.delay(500)
                main_menu()
        pygame.draw.rect(screen, green, Back)
        writeText("Back", fontSmall, brown, screen, 4 * screen.get_width() / 5, 14.5 * screen.get_height() / 20)

        Reset = pygame.Rect(0 * screen.get_width(), 7 * screen.get_height() / 10, screen.get_width() / 4,
                            screen.get_height() / 10)
        if Reset.collidepoint((mx, my)):
            if click:
                pygame.time.delay(500)
                playAgain()
                Game()
        pygame.draw.rect(screen, green, Reset)
        writeText("Play Again?", fontSmall, brown, screen, 1 * screen.get_width() / 10, 14.5 * screen.get_height() / 20)

        pygame.display.update()
        mainClock.tick(60)


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
