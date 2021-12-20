import csv
import random
import time

from colour import *
from pygame_functions import *

#variables
pygame.mixer.init(buffer=512)
pygame.init()
pygame.font.init()  
pygame.display.set_caption('Learn your Shapes')
screen = pygame.display.set_mode((1180, 818))
FPS = 10 #change this to about 5-10!
clock = pygame.time.Clock()
homescreen_image = pygame.image.load("images/Mainmenu.png").convert()
shape_circle = pygame.image.load("images/circle.png").convert_alpha()
shape_square = pygame.image.load("images/square.png").convert()
shape_triangle = pygame.image.load("images/triangle.png").convert()
shape_rectangle = pygame.image.load("images/rectangle.png").convert()   
shape_star = pygame.image.load("images/star.png").convert()
shape_diamond = pygame.image.load("images/diamond.png").convert()
shape_oval = pygame.image.load("images/oval.png").convert()
shape_heart = pygame.image.load("images/heart.png").convert()
circleY = pygame.image.load("images/circleY.png").convert()
squareN = pygame.image.load("images/squareN.png").convert()
thumbs_up = pygame.image.load("images/thumbsup.png").convert()
menu = "start"
myfont = pygame.font.SysFont('Comic Sans MS', 50)
score = 0
highest = 0
font = pygame.font.SysFont("draglinebtndm", 60)
match_start = time.time()
feedback_text = ""
feedback = myfont.render(feedback_text, True, (0,0,0))
timer= 5

# background music
pygame.mixer.music.load("Sound/shapesong1.mp3")
pygame.mixer.music.play (-1, 0.0)

#shape list
shapes=["circle", "square", "triangle", "rectangle", "star", "diamond", "oval", "heart"]

#game background
screen.fill(black)

button_circle = pygame.draw.rect(screen, Pink,(1, 570, 290, 130))
button_square = pygame.draw.rect(screen, Pink,(293, 570, 290, 130))
button_triangle = pygame.draw.rect(screen, Pink,(586, 570, 290, 130))
button_rectangle = pygame.draw.rect(screen, Pink,(879, 570, 290, 130))
button_star = pygame.draw.rect(screen, Pink,(1, 703, 290, 130)) 
button_diamond = pygame.draw.rect(screen, Pink,(293, 703, 290, 130))
button_oval = pygame.draw.rect(screen, Pink,(586, 703, 290, 130))
button_heart = pygame.draw.rect(screen, Pink,(879, 703, 290, 130))

def drawBoxes():
    # boxes    
    button_circle = pygame.draw.rect(screen, brown1,(1, 570, 290, 130))
    button_square = pygame.draw.rect(screen, brown1,(293, 570, 290, 130))
    button_triangle = pygame.draw.rect(screen, brown1,(586, 570, 290, 130))
    button_rectangle = pygame.draw.rect(screen, brown1,(879, 570, 290, 130))
    button_star = pygame.draw.rect(screen, brown1,(1, 703, 290, 130)) 
    button_diamond = pygame.draw.rect(screen, brown1,(293, 703, 290, 130))
    button_oval = pygame.draw.rect(screen, brown1,(586, 703, 290, 130))
    button_heart = pygame.draw.rect(screen, brown1,(879, 703, 290, 130))    
    
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


def csv_into_list(csv_file): 
    myScores = [] 
    with open(csv_file) as my_file:
        reader = csv.reader(my_file)
        for row in reader:
            myScores.append(row)
    return myScores


def list_into_csv(myScores,csv_file):
    #write back to the csv
    with open(csv_file, 'w', newline='') as my_file:
        writer = csv.writer(my_file)
        writer.writerows(myScores)


def bubbleSortAList(twoDList,sortItemIndex):
    '''
    expected structure is a 2 D list in form
    [
        [username, score]
    ]
    :param twoDList: 
    :param sortItemIndex: this is the index of item to be used to sort on,
    :e.g. 0 would sort on the first item in each of the records.
    :return: 
    '''
    for row in range(len(twoDList)):
        temp = twoDList[row][1]
        temp = int(temp)
        twoDList[row][1] = temp
        
    sort_by_field = sortItemIndex
    n = len(twoDList)
    swapped = True
    while n > 0 and swapped == True:
        swapped = False
        n = n - 1
        for row in range(0, n):
            if twoDList[row][sort_by_field] < twoDList[row + 1][sort_by_field]:
                tempRow = twoDList[row] # save for later
                twoDList[row] = twoDList[row +1]
                twoDList[row+1] = tempRow
                swapped = True


#drawing the shapes and making it move
class Particle:
    def __init__(self, position, shape):
        self.x, self.y = position
        self.dy = random.randint(2,4)
        self.dx = random.choice((-1,1))*self.dy
        self.shape = shape
        # self.spawn_time = time.time()
        
    def move(self):
        self.x += self.dx
        self.y += self.dy

    def draw(self):
        if self.shape == "circle":
            screen.blit(shape_circle, (self.x, self.y))
        elif self.shape == "square":
            screen.blit(shape_square, (self.x, self.y))
        elif self.shape == "triangle":
            screen.blit(shape_triangle, (self.x, self.y))
        elif self.shape == "rectangle":
            screen.blit(shape_rectangle, (self.x, self.y))
        elif self.shape == "star":
            screen.blit(shape_star, (self.x, self.y))
        elif self.shape == "diamond":
            screen.blit(shape_diamond, (self.x, self.y))
        elif self.shape == "oval":
            screen.blit(shape_oval, (self.x, self.y))
        elif self.shape == "heart":
            screen.blit(shape_heart, (self.x, self.y))
        elif self.shape == "thumbsup":
            screen.blit(thumbs_up, (580, 170))

    def bounce(self):
        if self.x < 0 or self.x > 570:
            self.dx *= -1
     
    def off_screen(self):
        return self.y > 440

next_shape = random.choice(shapes[0:8])
particle = Particle((150, 50),next_shape)

#data structures
players = ["Ghost","Blaze","Canyon","Flame","Hunter","Ocean","Phoenix","River","Sky",
           "Storm","Thunder","Wind","Dragon","Buckbeak","Grindylow","Charm","Patronus","Super","Blade",
           "Maze", "Lion","Space"]

myScores = csv_into_list("leaderboard.csv")
myPlayer = random.choice(players)+str(random.randint(1,100)) # generated before game play

pygame.display.update()

done = False
#Main game
while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            done=True
            sys.exit()

    if menu == "start":
        screen.blit(homescreen_image, (0,0))
        buttonrect = pygame.Rect(850, 650, 300, 300)
        if pygame.mouse.get_pressed()[0] and buttonrect.collidepoint(pygame.mouse.get_pos()):
            menu = "game"
            time.sleep(1)
            match_start = time.time()

    elif menu == "game":
        screen.fill(light_purple)
        drawBoxes()
        
        txt = font.render("score", True, (255,0,255))
        screen.blit(txt, (20,20))
        txt = font.render(str(score), True, (255,255,255))
        screen.blit(txt, (170,20))  
        score = int(score)
        feedback = myfont.render(feedback_text,True,black)
        screen.blit(feedback, (470, 200))
        txt = font.render(str(int(time.time() - match_start)), True, (255,255,255))
        screen.blit(txt, (screen.get_width()/2 - txt.get_width()/2, 20))
        txt = font.render("Username:", True, (255,255,255))
        screen.blit(txt, (710,20))
        txt = font.render(myPlayer, True, (255,255,255))
        screen.blit(txt, (950,20))

        if pygame.mouse.get_pressed()[0] and button_circle.collidepoint(pygame.mouse.get_pos()):
            if next_shape == "circle":
                score += 1
                feedback_text = "Circle, good job!"
            else:
                feedback_text = "That was not a circle"
            next_shape = random.choice(shapes[0:8])
            particle = Particle((150, 50),next_shape)
            
        elif pygame.mouse.get_pressed()[0] and button_square.collidepoint(pygame.mouse.get_pos()):
            if next_shape == "square":
                score += 1
                feedback_text = "Square, good job!"
            else:
                feedback_text = "That was not a square"
            next_shape = random.choice(shapes[0:8])
            particle = Particle((150, 50),next_shape)
            
        elif pygame.mouse.get_pressed()[0] and button_triangle.collidepoint(pygame.mouse.get_pos()):
            if next_shape == "triangle":
                score += 1
                feedback_text = "Triangle, good job!"
            else:
                feedback_text = "That was not a triangle"
            next_shape = random.choice(shapes[0:8])
            particle = Particle((150, 50),next_shape)
            
        elif pygame.mouse.get_pressed()[0] and button_rectangle.collidepoint(pygame.mouse.get_pos()):
            if next_shape == "rectangle":
                score += 1
                feedback_text = "Rectangle, good job!"
            else:
                feedback_text = "That was not a rectangle"
            next_shape = random.choice(shapes[0:8])
            particle = Particle((150, 50),next_shape)
            
        elif pygame.mouse.get_pressed()[0] and button_star.collidepoint(pygame.mouse.get_pos()):
            if next_shape == "star":
                score += 1
                feedback_text = "Star, good job!"
            else:
                feedback_text = "That was not a star"
            next_shape = random.choice(shapes[0:8])
            particle = Particle((150, 50),next_shape)
            
        elif pygame.mouse.get_pressed()[0] and button_diamond.collidepoint(pygame.mouse.get_pos()):
            if next_shape == "diamond":
                score += 1
                feedback_text = "Diamond, good job!"
            else:
                feedback_text = "That was not a diamond"
            next_shape = random.choice(shapes[0:8])
            particle = Particle((150, 50),next_shape)
            
        elif pygame.mouse.get_pressed()[0] and button_oval.collidepoint(pygame.mouse.get_pos()):
            if next_shape == "oval":
                score += 1
                feedback_text = "Oval, good job!"
            else:
                feedback_text = "That was not an oval"
            next_shape = random.choice(shapes[0:8])
            particle = Particle((150, 50),next_shape)
            
        elif pygame.mouse.get_pressed()[0] and button_heart.collidepoint(pygame.mouse.get_pos()):
            if next_shape == "heart":
                score += 1
                feedback_text = "Heart, good job!"
            else:
                feedback_text = "That was not a heart"
            next_shape = random.choice(shapes[0:8])
            particle = Particle((150, 50),next_shape)
        
        if not particle.off_screen():
            particle.draw()
            particle.move()
            particle.bounce()
        else:
            next_shape = random.choice(shapes[0:8])
            particle = Particle((150, 50),next_shape)

        if time.time() - match_start > 10:
            menu = "phase"
            phase_start = time.time()
            
    elif menu == "phase":
        screen.fill(light_purple)
        drawBoxes()
        txt = font.render("score", True, (255,0,255))
        screen.blit(txt, (20,20))
        txt = font.render(str(score), True, (255,255,255))
        screen.blit(txt, (170,20))  
        score = int(score)
        txt = font.render("Username:", True, (255,255,255))
        screen.blit(txt, (710,20))
        txt = font.render(myPlayer, True, (255,255,255))
        screen.blit(txt, (950,20))
        final_text = "Good game! You got "+str(score)
        final_blit = myfont.render(final_text,True,black)
        screen.blit(final_blit, (470, 200))
        if time.time() - phase_start > 3:
            menu = "end"
            myList = [myPlayer, score]
       
    elif menu == "end":
        screen.fill(orchid)
### Making the actual leaderboard table
        leader_rectangle = pygame.draw.rect(screen, orchid4,(300, 25, 580, 775))
        pygame.draw.line(screen, black, (600, 25), (600, 800), 4) # middle line
        pygame.draw.line(screen, black, (300, 96), (880, 96), 4) #title line
        pygame.draw.line(screen, black, (300, 160), (880, 160), 4)
        pygame.draw.line(screen, black, (300, 224), (880, 224), 4)
        pygame.draw.line(screen, black, (300, 288), (880, 288), 4)
        pygame.draw.line(screen, black, (300, 352), (880, 352), 4)
        pygame.draw.line(screen, black, (300, 416), (880, 416), 4)
        pygame.draw.line(screen, black, (300, 480), (880, 480), 4)
        pygame.draw.line(screen, black, (300, 544), (880, 544), 4)
        pygame.draw.line(screen, black, (300, 608), (880, 608), 4)
        pygame.draw.line(screen, black, (300, 672), (880, 672), 4)
        pygame.draw.line(screen, black, (300, 736), (880, 736), 4)

        if myList not in myScores:
            myScores.append(myList)
            list_into_csv(myScores,"leaderboard.csv")

            bubbleSortAList(myScores,1)
            
            #myScores.sort(key=lambda x: x[1])
            
        # this must be sorted (using a sorting algorithm actually) so that
        # the high scores table displays in order.
        
        txt = font.render("Score", True, (255,0,255))
        screen.blit(txt, (685,40))
        txt = font.render("Username", True, (255,0,255))
        screen.blit(txt, (350,40))
        
        y_offset = 105
        for score in myScores:
            txt = font.render(str(score[1]), True, (255,255,255))
            screen.blit(txt, (730,y_offset))
            txt = font.render(str(score[0]), True, (255,255,255))
            screen.blit(txt, (330,y_offset))
            # define the y pixel gap between rows, and each successive row,
            # add that y coordinate to the 105 argument
            if y_offset <= 768:
                y_offset += 64
        
        #txt = font.render(str(score), True, (255,255,255))
        #screen.blit(txt, (730,105)) 
        #txt = font.render(myPlayer, True, (255,255,255))
        #screen.blit(txt, (330,105)) 
        #score = int(score)

        #myPlayer = random.choice(players)+str(random.randint(1,100)) # generated again IF suser selects playAgain
                
    #pygame.display.flip()
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
