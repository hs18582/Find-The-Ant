from Entity import *
import random


colour = [[green for i in range(n)] for j in range(n)]
queueClicked = [[] for i in range(3)]
queueLocation = [[None for j in range(3)] for i in range(3)]
antLocation = [random.randint(0, n - 1), random.randint(0, n - 1)]
ant = pygame.image.load('Images/ant.png')
hole = pygame.image.load('Images/holec.png')
antFound = False
width = 600
height = 600

def Game():
    running = True
    count = 0

    while running:
        screen.fill((0, 0, 0))

        mx, my = pygame.mouse.get_pos()
        list_buttons = Grid()

        txt = font.render("Score:", True, green)
        screen.blit(txt, (3*screen.get_width()/4, 20))
        txt = font.render(str(count), True, brown)
        screen.blit(txt, (9*screen.get_width()/10, 20))
        count = int(count)


        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if antFound:
            # print(antLocation)
            x = ((width / (2 * n) + ((screen.get_width() / 2) - 300)) + (antLocation[1] * (width / n))) - 25
            y = ((height / (2 * n) + ((screen.get_width() / 2) - 625)) + (antLocation[0] * (height / n))) - 43

            screen.blit(ant, (x, y))

        else:
            # print(*queueLocation)
            if queueLocation[2][2] == True and [queueLocation[2][0], queueLocation[2][1]] in queueClicked:
                x = (width / (2 * n) + ((screen.get_width() / 2) - 300)) + (queueLocation[2][1] * (width / n))
                y = (height / (2 * n) + ((screen.get_width() / 2) - 625)) + (queueLocation[2][0] * (height / n))
                pygame.draw.circle(screen, red, (x, y), 20)
            if queueLocation[1][2] == True and [queueLocation[1][0], queueLocation[1][1]] in queueClicked:
                x = (width / (2 * n) + ((screen.get_width() / 2) - 300)) + (queueLocation[1][1] * (width / n))
                y = (height / (2 * n) + ((screen.get_width() / 2) - 625)) + (queueLocation[1][0] * (height / n))
                pygame.draw.circle(screen, orange, (x, y), 20)
            if queueLocation[0][2] == True and [queueLocation[0][0], queueLocation[0][1]] in queueClicked:
                x = (width / (2 * n) + ((screen.get_width() / 2) - 300)) + (queueLocation[0][1] * (width / n))
                y = (height / (2 * n) + ((screen.get_width() / 2) - 625)) + (queueLocation[0][0] * (height / n))
                pygame.draw.circle(screen, yellow, (x, y), 20)

            for i in range(n):
                for j in range(n):
                    if list_buttons[i][j].collidepoint((mx, my)):
                        if click and [i, j] not in queueClicked:
                            ButtonOpen(i, j)

                            if queueClicked[2] != []:
                                ButtonClose(queueClicked[2][0], queueClicked[2][1])
                            for z in range(2, 0, -1):
                                queueClicked[z] = queueClicked[z - 1]
                            queueClicked[0] = [i, j]
                            count += 1

                            print(count)

                            if not antFound:
                                Pheromone()
                                MoveAnt()

        pygame.display.update()
        mainClock.tick(60)


def Grid():
    # CREATING A LIST USING LIST COMPREHENSION
    list_buttons = [
        [pygame.Rect(((width / n) * i) + ((screen.get_width() / 2) - 300),
                     ((height / n) * j) + ((screen.get_height() / 2) - 300), (width / n) - 2, (height / n) - 2) for i in
         range(n)] for j in range(n)]

    # LOOP TO CREATE A N BY N GRID
    for i in range(len(list_buttons)):
        for j in range(len(list_buttons[i])):
            pygame.draw.rect(screen, colour[i][j], list_buttons[i][j])  # CREATING A GREEN RECTANGLE

    return list_buttons


def ButtonOpen(x, y):
    global antFound
    colour[x][y] = brown
    if antLocation == [x, y]:
        antFound = True
        # colour[x][y] = (0, 0, 0)


def ButtonClose(x, y):
    colour[x][y] = green


def MoveAnt():
    global antLocation

    x, y = antLocation[0], antLocation[1]
    possiblemoves = [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]
    if possiblemoves[0][0] == n:
        possiblemoves[0][0] = 0

    if possiblemoves[1][0] == -1:
        possiblemoves[1][0] = n - 1

    if possiblemoves[2][1] == n:
        possiblemoves[2][1] = 0

    if possiblemoves[3][1] == -1:
        possiblemoves[3][1] = n - 1

    for i in range(3, -1, -1):
        if possiblemoves[i] in queueClicked:
            possiblemoves.pop(i)

    index = random.randint(0, len(possiblemoves) - 1)

    antLocation = possiblemoves[index]


def Pheromone():
    droppingPoint = 0  # is the tipping point if number > 50 then drop if less hold

    for z in range(2, 0, -1):
        queueLocation[z] = queueLocation[z - 1]
    if random.randint(0, 100) >= droppingPoint:
        if [antLocation[0], antLocation[1], True] == queueLocation[1]:
            queueLocation[1][2] = False
        if [antLocation[0], antLocation[1], True] == queueLocation[2]:
            queueLocation[2][2] = False
        queueLocation[0] = [antLocation[0], antLocation[1], True]
    else:
        queueLocation[0] = [antLocation[0], antLocation[1], False]
