from src.ui.renderer import Renderer
from pathlib import Path
import json
from typing import Any


class Score:
    def __init__(self, renderer: Renderer, heighscors: str) -> None:
        self.renderer: Renderer = renderer
        self.heighscors: str = heighscors

    def check_event(self, event: str) -> str | None:

        if event == "ENTER":
            return "MENU"

        if event == "QUIT":
            return "QUIT"

        return None

    def draw_scors(self) -> None:

        self.renderer.clear()

        self.renderer.draw_text(
            "SCORE-S",
            180,
            100
        )
        fl = Path("highscore.json")
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
    def __init__(self, renderer: Renderer) -> None:
        self.renderer: Renderer = renderer

    def check_event(self, event: str) -> str | None:

        if event == "ENTER":
            return "MENU"

        if event == "QUIT":
            return "QUIT"

        return None

    def display_ins(self) -> None:
        self.renderer.clear()

        self.renderer.draw_text(
            "INSTRUCTION",
            150,
            50
        )

        self.renderer.draw_text(
            "ARROW KEYS: MOVE",
            80,
            150
        )

        self.renderer.draw_text(
            "EAT ALL PAC-DOTS",
            80,
            210
        )

        self.renderer.draw_text(
            "AVOID THE GHOSTS",
            80,
            270
        )

        self.renderer.draw_text(
            "ENTER: BACK TO MENU",
            80,
            350
        )

        self.renderer.display()
