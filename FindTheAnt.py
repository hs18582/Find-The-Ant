from Entity import *
from pygame.locals import *


########################################################################################################################

def main_menu():
    mainClock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    while True:

        screen.fill(black)

        writeText("Find The Ant", fontTitle, brown, screen, 3 * screen.get_width() / 4, screen.get_height() / 20)

        click = False
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


main_menu()
