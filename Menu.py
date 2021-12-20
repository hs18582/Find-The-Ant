from Entity import *
from Instructions import Instructions
from Game import Game
from LeaderBoard import LeaderBoard


def main_menu():
    while True:
        screen.fill((0, 0, 0))
        ant = pygame.image.load('Images/antMain.png')

        draw_text("Find The Ant", fontTitle, brown, screen, 3 * screen.get_width() / 5, screen.get_height() / 20)
        mx, my = pygame.mouse.get_pos()

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

        Start = pygame.Rect(screen.get_width() / 20, screen.get_height() / 8, screen.get_width() / 2,
                            screen.get_height() / 8)
        Instruction = pygame.Rect(screen.get_width() / 20, (screen.get_height() / 8 + (screen.get_height() / 4)),
                                  (3 * screen.get_width()) / 8, screen.get_height() / 8)
        Leaderboard = pygame.Rect(screen.get_width() / 20, (screen.get_height() / 8 + (screen.get_height() / 2)),
                                  (screen.get_width()) / 4, screen.get_height() / 8)
        Quit = pygame.Rect(screen.get_width() / 20, (screen.get_height() / 8 + (3 * screen.get_height() / 4)),
                           (screen.get_width()) / 8, screen.get_height() / 8)

        if Start.collidepoint((mx, my)):
            if click:
                Game()
        if Instruction.collidepoint((mx, my)):
            if click:
                Instructions()
        if Leaderboard.collidepoint((mx, my)):
            if click:
                LeaderBoard()
        if Quit.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(screen, green, Start)
        screen.blit(font.render('Start', True, brown),
                    (screen.get_width() / 20, (screen.get_height() / 4) - screen.get_height() / 12))

        pygame.draw.rect(screen, brown, Instruction)
        screen.blit(font.render('Rules', True, green),
                    (screen.get_width() / 20, (screen.get_height() / 8) + screen.get_height() / 3.5))

        pygame.draw.rect(screen, green, Leaderboard)
        screen.blit(font.render('Leaderboard', True, brown),
                    (screen.get_width() / 20, (screen.get_height() / 16) + screen.get_height() / 1.65))

        pygame.draw.rect(screen, brown, Quit)
        screen.blit(font.render('Quit', True, green),
                    (screen.get_width() / 20, (screen.get_height() / 16) + screen.get_height() / 1.17))

        screen.blit(ant, (screen.get_width() / 2, (screen.get_height() / 8) + screen.get_height() / 3.5))

        pygame.display.update()
        mainClock.tick(60)


main_menu()
