import pygame
# import sys


def draw():

    pygame.init()
    sc = pygame.display.set_mode((2000, 1500), pygame.NOFRAME)
    pygame.display.set_caption("test")
    font = pygame.font.Font(None, 50)
    txt = font.render("Hello bkhalid", True, (0, 0, 0))
    rn = True
    while rn:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                rn = False
        sc.fill((0, 0, 0))

        x, y, w, h = 100, 50, 1500, 900

        color = (255, 255, 0)
        for i in range(w):
            pygame.draw.line(sc, color, (x + i, y), (x + i + 1, y), 1)
            pygame.draw.line(sc, color, (x + i, y + h), (x + i + 1, y + h), 1)

        for i in range(h):
            pygame.draw.line(sc, color, (x, y + i), (x, y + i + 1), 1)
            pygame.draw.line(sc, color, (x + w, y + i), (x + w, y + i + 1), 1)

        for i in range(h):
            pygame.draw.line(sc, color, (x, y + i), (x + w, y + i), 1)

        sc.blit(txt, (150, 130))

        pygame.display.flip()


draw()
