from renderer import Renderer
from menu import Menu
from screens import Score, Insruction


renderer = Renderer(2000, 1500, "Pac-Man")

menu = Menu(renderer)
score = Score(renderer, "heighscors.json")
instruction = Insruction(renderer)

screen = "MENU"
run = True

while run:

    events = renderer.event()

    for event in events:

        if screen == "MENU":

            result = menu.check_event(event)

            if result == "START":
                print("start game...")

            elif result == "SCORES":
                print("open scores...")
                screen = "SCORES"
            elif result == "INSTARUCTION":
                print("open instaruction ...")
                screen = "INSTARUCTION"

            elif result == "QUIT":
                run = False

        elif screen == "SCORES":

            result = score.check_event(event)

            if result == "MENU":
                screen = "MENU"

            elif result == "QUIT":
                run = False
        elif screen == "INSTARUCTION":
            result = instruction.check_event(event)

            if result == "MENU":
                screen = "MENU"

            elif result == "QUIT":
                run = False

    if screen == "MENU":
        menu.draw()

    elif screen == "SCORES":
        score.draw_scors()
    elif screen == "INSTARUCTION":
        instruction.display_ins()


renderer.close()
