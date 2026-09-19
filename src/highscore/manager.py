import json
from pathlib import Path
from typing import List, Dict, Union


class HighscoreManager():
    def __init__(self, filename: str = "highscores.json"):

        self.filepath: Path = Path(filename)
        self.scores: List[Dict[str, Union[str, int]]] = []
        self._load_scores()

    def _load_scores(self) -> None:
        try:
            if self.filepath.exists():
                with self.filepath.open('r') as file:
                    self.scores = json.load(file)

        except (json.JSONDecodeError, IOError) as e:
            print(e)
            self.scores = []


if __name__ == '__main__':
    manager = HighscoreManager()
    print("File:", manager.filepath)
    print("Scores:", manager.scores)
