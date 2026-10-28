import pygame
import sys


def draw():

    pygame.init()
    sc = pygame.display.set_mode((2000, 1500), pygame.NOFRAME)
    pygame.display.set_caption("test")
    font = pygame.font.Font(None, 50)
    txt = font.render("Hello bkhalid", True, (255, 215, 0))
    rn = True
    while rn:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                rn = False

        pygame.display.flip()

    sc.blit(txt, (15, 15))
    pygame.quit()
    sys.exit()


draw()
