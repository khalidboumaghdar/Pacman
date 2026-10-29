from src.ui.renderer import Renderer
from pathlib import Path
import json
from typing import Any


class Score:
    """This class to display highscore list"""
    def __init__(self, renderer: Renderer, heighscors: str) -> None:
        self.renderer: Renderer = renderer
        self.heighscors: str = heighscors

    def check_event(self, event: str) -> str | None:
        """This method use to check event"""

        if event == "ENTER":
            return "MENU"

        if event == "QUIT":
            return "QUIT"

        return None

    def draw_scors(self) -> None:
        """This method use to draw highscore list"""

        self.renderer.clear()

        self.renderer.draw_text(
            "SCORE-S",
            180,
            100
        )
        fl = Path(self.heighscors)
        f: list[dict[str, Any]] = []
        if fl.exists():
            with fl.open("r") as file:
                f = json.load(file)

        # print(f)
        f = sorted(f, key=lambda x: x["score"], reverse=True)[:10]

        i = 0
        for p in f:
            self.renderer.draw_text(
                p["name"],
                100,
                150 + i
            )
            # print(p["score"])
            self.renderer.draw_text(
                p["score"],
                300,
                150 + i
            )
            i += 50
        # exit(0)

        self.renderer.draw_text(
            "Press ENTER to go back",
            100,
            800
        )

        self.renderer.display()


class Insruction:
    """This class use to renderer instruction menu"""
    def __init__(self, renderer: Renderer) -> None:
        self.renderer: Renderer = renderer

    def check_event(self, event: str) -> str | None:
        """This method use to check event"""

        if event == "ENTER":
            return "MENU"

        if event == "QUIT":
            return "QUIT"

        return None

    def display_ins(self) -> None:
        """This method use to renderer text in instruction menu"""
        self.renderer.clear()

        self.renderer.draw_text(
            "INSTRUCTION",
            150,
            100
        )

        self.renderer.draw_text(
            "ARROW KEYS: MOVE",
            150,
            200
        )

        self.renderer.draw_text(
            "EAT ALL PAC-DOTS",
            150,
            250
        )

        self.renderer.draw_text(
            "AVOID THE GHOSTS",
            150,
            300
        )
        self.renderer.draw_text(
            "F5 KEY CHEAT MODE",
            150,
            350
        )

        self.renderer.draw_text(
            "F6 KEY DISACTIVATE TIMER COMPLITLY",
            150,
            400
        )

        self.renderer.draw_text(
            "ENTER: BACK TO MENU",
            150,
            550
        )

        self.renderer.display()
