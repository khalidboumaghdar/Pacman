import pygame


class Renderer:
    def __init__(self, width: int, height: int, title: str) -> None:
        pygame.init()

        self.width = width
        self.height = height
        self.title = title

        self.screen = pygame.display.set_mode((2000, 1500), pygame.NOFRAME)
        pygame.display.set_caption(title)

        self.font = pygame.font.Font(None, 50)

    def event(self) -> list[str]:
        events: list[str] = []

        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:
                events.append("QUIT")

            elif ev.type == pygame.KEYDOWN:

                if ev.key == pygame.K_UP:
                    events.append("UP")

                elif ev.key == pygame.K_DOWN:
                    events.append("DOWN")

                elif ev.key == pygame.K_RETURN:
                    events.append("ENTER")

                elif ev.key == pygame.K_ESCAPE:
                    events.append("QUIT")

        return events

    def clear(self) -> None:
        self.screen.fill((255, 255, 0))

    def draw_text(self, text: str, x: int, y: int) -> None:
        image = self.font.render(str(text), True, (0, 0, 0))
        self.screen.blit(image, (x, y))

    def display(self) -> None:
        pygame.display.flip()

    def draw_body(
        self,
        x: int,
        y: int,
        width: int,
        height: int
    ) -> None:

        yellow = (255, 255, 0)

        for i in range(height):

            self.draw_line(
                x,
                y + i,
                x + width,
                y + i,
                yellow
            )

    def draw_line(
        self,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        color: tuple[int, int, int]
    ) -> None:

        pygame.draw.line(
            self.screen,
            color,
            (x1, y1),
            (x2, y2),
            1
        )

    def close(self) -> None:
        pygame.quit()