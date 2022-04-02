import csv
import random
import sys
from pygame.locals import *
from Entity import *


class Init:
    def __init__(self):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.antFound = False
        self.colour = []
        self.antLocation = []
        self.width = 600
        self.height = 600
        self.mainClock = pygame.time.Clock()
        self.queueClicked = []
        self.queueLocation = []
        self.ant = pygame.image.load('Images/ant.png')
        self.antmini = pygame.image.load('Images/antMini.png')  # https://www.pinclipart.com/maxpin/iTbwbmJ/
        self.scoreList = []
        self.n = 0
        self.highscore = ["-", "-", "-"]
        self.running = True

    def setN(self, n):
        self.n = n
        self.colour = [[green for _ in range(n)] for _ in range(n)]
        self.antLocation = [random.randint(0, n - 1), random.randint(0, n - 1)]
        self.queueClicked = [[] for _ in range(n)]
        self.queueLocation = [[None for _ in range(3)] for _ in range(n)]

    def getN(self):
        return self.n

    def setHighscore(self, highscore, difficulty):
        self.highscore[difficulty] = highscore

    def getHighscore(self, difficulty):
        return self.highscore[difficulty]


Init = Init()


##########################################################################################################
def write_to_file():
    with open("Highscore.csv", "w") as f:
        for i in range(3):
            f.write(str(Init.getHighscore(i)))
            f.write("\n")


##########################################################################################################
def Level():
    pygame.init()

    mainClock = pygame.time.Clock()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    LevelRunning = True
    while LevelRunning:
        screen.fill(black)

        writeText("Levels", fontTitle, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 20)
        mx, my = pygame.mouse.get_pos()

        x = 0
        antmini = pygame.image.load('Images/antMini.png')  # https://www.pinclipart.com/maxpin/iTbwbmJ/
        for i in range(round(screen.get_width() / 200)):
            screen.blit(antmini, (x, 16.8 * screen.get_height() / 20))
            x += 256

        click = False
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        Easy = pygame.Rect(7 * screen.get_width() / 20, 4 * screen.get_height() / 20, 7 * screen.get_width() / 20,
                           2 * screen.get_height() / 20)
        Medium = pygame.Rect(7 * screen.get_width() / 20, 9 * screen.get_height() / 20, 7 * screen.get_width() / 20,
                             2 * screen.get_height() / 20)
        Hard = pygame.Rect(7 * screen.get_width() / 20, 14 * screen.get_height() / 20, 7 * screen.get_width() / 20,
                           2 * screen.get_height() / 20)

        if Easy.collidepoint((mx, my)):
            if click:
                Init.setN(3)
                playAgain()
                Game()
        if Medium.collidepoint((mx, my)):
            if click:
                Init.setN(5)
                playAgain()
                Game()
        if Hard.collidepoint((mx, my)):
            if click:
                Init.setN(10)
                playAgain()
                Game()
        pygame.draw.rect(screen, green, Easy)
        writeText("Easy", fontSmall, brown, screen, screen.get_width() / 2, screen.get_height() / 4.6)

        pygame.draw.rect(screen, brown, Medium)
        writeText("Medium", fontSmall, green, screen, screen.get_width() / 2, screen.get_height() / 2.12)

        pygame.draw.rect(screen, green, Hard)
        writeText("Hard", fontSmall, brown, screen, screen.get_width() / 2, screen.get_height() / 1.4)

        pygame.display.update()
        mainClock.tick(60)


########################################################################################
def Game():
    start_ticks = pygame.time.get_ticks()  # starter tick
    pygame.init()

    while Init.running:
        Init.screen.fill(black)
        mx, my = pygame.mouse.get_pos()
        list_buttons = Grid()

        count = 0
        x = 0

        seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # calculate how many seconds
        if seconds > 180:  # if more than 10 seconds close the game
            pygame.display.update()
            Loser()

        for i in range(round(Init.screen.get_width() / 200)):
            Init.screen.blit(Init.antmini, (x, 16.8 * Init.screen.get_height() / 20))
            x += 256

        Tscore = len(Init.scoreList)
        writeText("Score:  " + str(Tscore), fontSmall, green, Init.screen, 3 * Init.screen.get_width() / 4,
                  Init.screen.get_height() / 20)

        if Init.getN() == 3:
            writeText("Highscore:  " + str(Init.getHighscore(0)), fontSmall, green, Init.screen,
                      Init.screen.get_width() / 4, Init.screen.get_height() / 20)
        elif Init.getN() == 5:
            writeText("Highscore:  " + str(Init.getHighscore(1)), fontSmall, green, Init.screen,
                      Init.screen.get_width() / 4, Init.screen.get_height() / 20)
        elif Init.getN() == 10:
            writeText("Highscore:  " + str(Init.getHighscore(2)), fontSmall, green, Init.screen,
                      Init.screen.get_width() / 4, Init.screen.get_height() / 20)

        click = False
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # Creating and Drawing back button
        Back = pygame.Rect(3 * Init.screen.get_width() / 4, 7 * Init.screen.get_height() / 10,
                           Init.screen.get_width() / 4,
                           Init.screen.get_height() / 10)
        if Back.collidepoint((mx, my)):
            if click:
                pygame.time.delay(500)
                main_menu()
        pygame.draw.rect(Init.screen, green, Back)
        writeText("Back", fontSmall, brown, Init.screen, 4 * Init.screen.get_width() / 5,
                  14.5 * Init.screen.get_height() / 20)

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
            colours = [red, orange, yellow, green, blue, light_blue, pink, purple, grey, white]
            for i in range(Init.getN() - 1, -1, -1):
                if Init.queueLocation[i][2] == True and [Init.queueLocation[i][0],
                                                         Init.queueLocation[i][1]] in Init.queueClicked:
                    x = (Init.width / (2 * Init.getN()) + ((Init.screen.get_width() / 2) - 300)) + (
                            Init.queueLocation[i][1] * (Init.width / Init.getN()))
                    y = (Init.height / (2 * Init.getN()) + ((Init.screen.get_width() / 2) - 625)) + (
                            Init.queueLocation[i][0] * (Init.height / Init.getN()))
                    pygame.draw.circle(Init.screen, colours[i], (x, y), 20)

            for i in range(Init.getN()):
                for j in range(Init.getN()):
                    if list_buttons[i][j].collidepoint((mx, my)):
                        if click and [i, j] not in Init.queueClicked:
                            ButtonOpen(i, j)

                            if Init.queueClicked[Init.getN() - 1]:
                                ButtonClose(Init.queueClicked[Init.getN() - 1][0],
                                            Init.queueClicked[Init.getN() - 1][1])
                            for z in range(Init.getN() - 1, 0, -1):
                                Init.queueClicked[z] = Init.queueClicked[z - 1]
                            Init.queueClicked[0] = [i, j]
                            count += 1
                            Init.scoreList.append(count)

                            if not Init.antFound:
                                Pheromone()
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
    droppingPoint = 0
    # is the tipping point if number > 50 then drop if less hold( if num = 50 then 50% of being dropped

    for z in range(Init.getN() - 1, 0, -1):
        Init.queueLocation[z] = Init.queueLocation[z - 1]
    if random.randint(0, 100) >= droppingPoint:
        for i in range(1, Init.getN() - 1):
            if [Init.antLocation[0], Init.antLocation[1], True] == Init.queueLocation[i]:
                Init.queueLocation[i][2] = False
        # if [Init.antLocation[0], Init.antLocation[1], True] == Init.queueLocation[1]:
        #     Init.queueLocation[1][2] = False
        # if [Init.antLocation[0], Init.antLocation[1], True] == Init.queueLocation[2]:
        #     Init.queueLocation[2][2] = False
        Init.queueLocation[0] = [Init.antLocation[0], Init.antLocation[1], True]
    else:
        Init.queueLocation[0] = [Init.antLocation[0], Init.antLocation[1], False]


def playAgain():
    Init.mainClock = pygame.time.Clock()
    Init.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    Init.colour = [[green for _ in range(Init.getN())] for _ in range(Init.getN())]
    Init.antLocation = [random.randint(0, Init.getN() - 1), random.randint(0, Init.getN() - 1)]
    Init.ant = pygame.image.load('Images/ant.png')
    Init.antmini = pygame.image.load('Images/antMini.png')  # https://www.pinclipart.com/maxpin/iTbwbmJ/
    Init.antFound = False
    Init.width = 600
    Init.height = 600
    Init.scoreList = []
    Init.running = True


##########################################################################################################

def Winner():
    pygame.init()

    antmini = pygame.image.load('Images/antMini.png')  # https://www.pinclipart.com/maxpin/iTbwbmJ/
    mainClock = pygame.time.Clock()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    Tscore = len(Init.scoreList)

    WinnerRunning = True

    while WinnerRunning:
        screen.fill((0, 0, 0))

        x = 0
        for i in range(round(screen.get_width() / 200)):
            screen.blit(antmini, (x, 16.8 * screen.get_height() / 20))
            x += 256

        click = False
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if Init.getN() == 3:
            if int(Tscore) <= int(Init.getHighscore(0)):
                Init.setHighscore(Tscore, 0)
                # write_to_file()
                writeText("Congratulations! New Highscore!", fontTitle, (255, 255, 255), screen, screen.get_width() / 2,
                          screen.get_height() / 20)
                writeText("Your score is: ", fontTitle, (255, 255, 255), screen, screen.get_width() / 2,
                          8 * screen.get_height() / 20)
                writeText(str(Tscore), fontTitle, (255, 255, 255), screen, screen.get_width() / 2,
                          screen.get_height() / 2)
            else:
                writeText("Congratulations!", fontTitle, (255, 255, 255), screen, screen.get_width() / 2,
                          screen.get_height() / 20)
                writeText("Your score is: ", fontTitle, (255, 255, 255), screen, screen.get_width() / 2,
                          8 * screen.get_height() / 20)
                writeText(str(Tscore), fontTitle, (255, 255, 255), screen, screen.get_width() / 2,
                          screen.get_height() / 2)
                writeText("HighScore: " + str(Init.getHighscore(0)), fontSmall, (255, 255, 255), screen,
                          screen.get_width() / 2,
                          14 * screen.get_height() / 20)

        if Init.getN() == 5:
            if int(Tscore) <= int(Init.getHighscore(1)):
                Init.setHighscore(Tscore, 1)
                writeText("Congratulations! New Highscore!", fontTitle, (255, 255, 255), screen, screen.get_width() / 2,
                          screen.get_height() / 20)
                writeText("Your score is: ", fontTitle, (255, 255, 255), screen, screen.get_width() / 2,
                          8 * screen.get_height() / 20)
                writeText(str(Tscore), fontTitle, (255, 255, 255), screen, screen.get_width() / 2,
                          screen.get_height() / 2)
            else:
                writeText("Congratulations!", fontTitle, (255, 255, 255), screen, screen.get_width() / 2,
                          screen.get_height() / 20)
                writeText("Your score is: ", fontTitle, (255, 255, 255), screen, screen.get_width() / 2,
                          8 * screen.get_height() / 20)
                writeText(str(Tscore), fontTitle, (255, 255, 255), screen, screen.get_width() / 2,
                          screen.get_height() / 2)
                writeText("HighScore: " + str(Init.getHighscore(1)), fontSmall, (255, 255, 255), screen,
                          screen.get_width() / 2,
                          14 * screen.get_height() / 20)

        if Init.getN() == 10:
            if int(Tscore) <= int(Init.getHighscore(2)):
                Init.setHighscore(Tscore, 2)
                writeText("Congratulations! New Highscore!", fontTitle, (255, 255, 255), screen, screen.get_width() / 2,
                          screen.get_height() / 20)
                writeText("Your score is: ", fontTitle, (255, 255, 255), screen, screen.get_width() / 2,
                          8 * screen.get_height() / 20)
                writeText(str(Tscore), fontTitle, (255, 255, 255), screen, screen.get_width() / 2,
                          screen.get_height() / 2)
            else:
                writeText("Congratulations!", fontTitle, (255, 255, 255), screen, screen.get_width() / 2,
                          screen.get_height() / 20)
                writeText("Your score is: ", fontTitle, (255, 255, 255), screen, screen.get_width() / 2,
                          8 * screen.get_height() / 20)
                writeText(str(Tscore), fontTitle, (255, 255, 255), screen, screen.get_width() / 2,
                          screen.get_height() / 2)
                writeText("Highscore: " + str(Init.getHighscore(2)), fontSmall, (255, 255, 255), screen,
                          screen.get_width() / 2,
                          14 * screen.get_height() / 20)

        # Creating and Drawing back button
        mx, my = pygame.mouse.get_pos()
        Back = pygame.Rect(3 * screen.get_width() / 4, 7 * screen.get_height() / 10, screen.get_width() / 4,
                           screen.get_height() / 10)
        if Back.collidepoint((mx, my)):
            if click:
                write_to_file()
                pygame.time.delay(500)
                main_menu()
        pygame.draw.rect(screen, green, Back)
        writeText("Back", fontSmall, brown, screen, 4 * screen.get_width() / 5, 14.5 * screen.get_height() / 20)

        Reset = pygame.Rect(0 * screen.get_width(), 7 * screen.get_height() / 10, screen.get_width() / 4,
                            screen.get_height() / 10)
        if Reset.collidepoint((mx, my)):
            if click:
                write_to_file()
                pygame.time.delay(500)
                playAgain()
                Game()
        pygame.draw.rect(screen, green, Reset)
        writeText("Play Again?", fontSmall, brown, screen, 1 * screen.get_width() / 10, 14.5 * screen.get_height() / 20)

        pygame.display.update()
        mainClock.tick(60)


##########################################################################################################
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

        x = 0
        for i in range(round(screen.get_width() / 200)):
            screen.blit(antmini, (x, 16.8 * screen.get_height() / 20))
            x += 256

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
                write_to_file()
                pygame.time.delay(500)
                main_menu()
        pygame.draw.rect(screen, green, Back)
        writeText("Back", fontSmall, brown, screen, 4 * screen.get_width() / 5, 14.5 * screen.get_height() / 20)

        Reset = pygame.Rect(0 * screen.get_width(), 7 * screen.get_height() / 10, screen.get_width() / 4,
                            screen.get_height() / 10)
        if Reset.collidepoint((mx, my)):
            if click:
                write_to_file()
                pygame.time.delay(500)
                playAgain()
                Game()
        pygame.draw.rect(screen, green, Reset)
        writeText("Play Again?", fontSmall, brown, screen, 1 * screen.get_width() / 10, 14.5 * screen.get_height() / 20)

        pygame.display.update()
        mainClock.tick(60)


##########################################################################################################
def HighScore():
    pygame.init()

    mainClock = pygame.time.Clock()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    HighscoreRunning = True

    while HighscoreRunning:
        screen.fill((0, 0, 0))
        mx, my = pygame.mouse.get_pos()

        x = 0
        antmini = pygame.image.load('Images/antMini.png')  # https://www.pinclipart.com/maxpin/iTbwbmJ/
        for i in range(round(screen.get_width() / 200)):
            screen.blit(antmini, (x, 16.8 * screen.get_height() / 20))
            x += 256

        writeText("Levels", fontTitle, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 20)

        writeText("Easy mode:  " + str(Init.getHighscore(0)), fontSmall, brown, screen, screen.get_width() / 2,
                  screen.get_height() / 4.6)

        writeText("Medium mode:  " + str(Init.getHighscore(1)), fontSmall, green, screen, screen.get_width() / 2,
                  screen.get_height() / 2.12)

        writeText("Hard mode:  " + str(Init.getHighscore(2)), fontSmall, brown, screen, screen.get_width() / 2,
                  screen.get_height() / 1.4)

        click = False
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # Creating and Drawing back button
        Back = pygame.Rect(3 * screen.get_width() / 4, 7 * screen.get_height() / 10, screen.get_width() / 4,
                           screen.get_height() / 10)
        if Back.collidepoint((mx, my)):
            if click:
                pygame.time.delay(500)
                main_menu()
        pygame.draw.rect(screen, green, Back)
        writeText("Back", fontSmall, brown, screen, 4 * screen.get_width() / 5, 14.5 * screen.get_height() / 20)

        pygame.display.update()
        mainClock.tick(60)


#############################################################################
def Rules():
    pygame.init()

    ant = pygame.image.load('Images/antRules.png')
    mainClock = pygame.time.Clock()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    RuleRunning = True

    while RuleRunning:
        screen.fill(black)
        mx, my = pygame.mouse.get_pos()

        writeText("Rules:", fontTitle, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 20)
        writeText("Objective: Find the ant by uncovering the boxes before time runs out!", fonttiny, (255, 255, 255),
                  screen, screen.get_width() / 2, 3.5 * screen.get_height() / 20)
        writeText("1. The game ends either by finding the ant or the 3 minute timer runs out", fonttiny,
                  (255, 255, 255), screen, screen.get_width() / 2, 5 * screen.get_height() / 20)
        writeText("2. There are 3 levels: Easy, Medium and Hard", fonttiny, (255, 255, 255), screen,
                  screen.get_width() / 2, 6.5 * screen.get_height() / 20)
        writeText("3. There are 5 possible options that can be uncovered: ", fonttiny, (255, 255, 255), screen,
                  screen.get_width() / 2, 8 * screen.get_height() / 20)
        writeText("- empty patch of soil", fonttiny, (255, 255, 255), screen, screen.get_width() / 2,
                  9.5 * screen.get_height() / 20)
        writeText("- A Pheromone (its colour can tell where the ant has been or will be)", fonttiny, (255, 255, 255),
                  screen, screen.get_width() / 2, 11 * screen.get_height() / 20)
        writeText("- An Ant", fonttiny, (255, 255, 255), screen, screen.get_width() / 2,
                  15.5 * screen.get_height() / 20)
        writeText("BUT remember .. the ant doesn't always have to leave a clue behind!", fonttiny, (255, 255, 255),
                  screen, screen.get_width() / 2, 18.5 * screen.get_height() / 20)

        Init.screen.blit(ant, (8 * screen.get_width() / 20, 15 * screen.get_height() / 20))

        click = False
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # Creating and Drawing back button
        colour = pygame.Rect(4.5 * screen.get_width() / 20, 12.75 * screen.get_height() / 20,
                             11 * screen.get_width() / 20, 2 * screen.get_height() / 20)
        if colour.collidepoint((mx, my)):
            if click:
                Colours()
        pygame.draw.rect(screen, green, colour)
        writeText("Click here for the pheromone colours", fontSmall, brown, screen, 10 * screen.get_width() / 20,
                  13 * screen.get_height() / 20)

        # Creating and Drawing back button
        Back = pygame.Rect(15 * screen.get_width() / 20, 15.5 * screen.get_height() / 20, 5 * screen.get_width() / 20,
                           2 * screen.get_height() / 20)
        if Back.collidepoint((mx, my)):
            if click:
                pygame.time.delay(500)
                main_menu()
        pygame.draw.rect(screen, green, Back)
        writeText("Back", fontSmall, brown, screen, 4 * screen.get_width() / 5, 16 * screen.get_height() / 20)

        pygame.display.update()
        mainClock.tick(60)


##########################################################################################################
def Colours():
    pygame.init()
    mainClock = pygame.time.Clock()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    ColourRunning = True

    while ColourRunning:
        screen.fill(black)

        writeText("Pheromone colours:", fontTitle, (255, 255, 255), screen, screen.get_width() / 2,
                  screen.get_height() / 20)

        writeText("1 day: Red", fonttiny, (255, 255, 255), screen, screen.get_width() / 2,
                  3.5 * screen.get_height() / 20)
        pygame.draw.circle(Init.screen, red, (12 * screen.get_width() / 20, 3.75 * screen.get_height() / 20), 20)

        writeText("2 days: Orange", fonttiny, (255, 255, 255), screen, screen.get_width() / 2,
                  5 * screen.get_height() / 20)
        pygame.draw.circle(Init.screen, orange, (12 * screen.get_width() / 20, 5.15 * screen.get_height() / 20), 20)

        writeText("3 days: Yellow", fonttiny, (255, 255, 255), screen, screen.get_width() / 2,
                  6.5 * screen.get_height() / 20)
        pygame.draw.circle(Init.screen, yellow, (12 * screen.get_width() / 20, 6.75 * screen.get_height() / 20), 20)

        writeText("4 days: Green", fonttiny, (255, 255, 255), screen, screen.get_width() / 2,
                  8 * screen.get_height() / 20)
        pygame.draw.circle(Init.screen, green, (12 * screen.get_width() / 20, 8.15 * screen.get_height() / 20), 20)

        writeText("5 days: Blue", fonttiny, (255, 255, 255), screen, screen.get_width() / 2,
                  9.5 * screen.get_height() / 20)
        pygame.draw.circle(Init.screen, blue, (12 * screen.get_width() / 20, 9.75 * screen.get_height() / 20), 20)

        writeText("6 days: Light Blue", fonttiny, (255, 255, 255), screen, screen.get_width() / 2,
                  11 * screen.get_height() / 20)
        pygame.draw.circle(Init.screen, light_blue, (12 * screen.get_width() / 20, 11.15 * screen.get_height() / 20),
                           20)

        writeText("7 days: Pink", fonttiny, (255, 255, 255), screen, screen.get_width() / 2,
                  12.5 * screen.get_height() / 20)
        pygame.draw.circle(Init.screen, pink, (12 * screen.get_width() / 20, 12.75 * screen.get_height() / 20), 20)

        writeText("8 days: Purple", fonttiny, (255, 255, 255), screen, screen.get_width() / 2,
                  14 * screen.get_height() / 20)
        pygame.draw.circle(Init.screen, purple, (12 * screen.get_width() / 20, 14.15 * screen.get_height() / 20), 20)

        writeText("9 days: Grey", fonttiny, (255, 255, 255), screen, screen.get_width() / 2,
                  15.5 * screen.get_height() / 20)
        pygame.draw.circle(Init.screen, grey, (12 * screen.get_width() / 20, 15.75 * screen.get_height() / 20), 20)

        writeText("10 days: White", fonttiny, (255, 255, 255), screen, screen.get_width() / 2,
                  17 * screen.get_height() / 20)
        pygame.draw.circle(Init.screen, white, (12 * screen.get_width() / 20, 17.15 * screen.get_height() / 20), 20)

        writeText("To help you remember they are very similar to the colours the rainbow!", fonttiny, (255, 255, 255),
                  screen, screen.get_width() / 2, 18.5 * screen.get_height() / 20)

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
                Rules()
        pygame.draw.rect(screen, green, Back)
        writeText("Back", fontSmall, brown, screen, 4 * screen.get_width() / 5, 14.5 * screen.get_height() / 20)

        pygame.display.update()
        mainClock.tick(60)


########################################################################################################################
def main_menu():
    mainClock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    with open("Highscore.csv", "r") as f:
        file_read = csv.reader(f)
        Init.highscore = list(file_read)
    for i in range(len(Init.highscore)):
        numeric_filter = filter(str.isdigit, Init.highscore[i])
        Init.highscore[i] = int("".join(numeric_filter))

    while True:

        screen.fill((0, 0, 0))
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
                Level()
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
#####################################################
