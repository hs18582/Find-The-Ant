from Entity import *


def Instructions():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text("Rules:", font, (255, 255, 255), screen, 300, 20)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        mainClock.tick(60)