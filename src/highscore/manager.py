import json
from pathlib import Path
from typing import List, Dict, Union


class HighscoreManager():
    def __init__(self, filename: str,
                 scores: list[Dict[str, Union[str, int]]]
                 ) -> None:

        self.filepath: Path = Path(filename)
        self.scores: List[Dict[str, Union[str, int]]] = scores
        self._load_scores()

    def _load_scores(self) -> None:
        try:
            if self.filepath.exists():
                with self.filepath.open('r') as file:
                    self.scores = json.load(file)
            else:
                with open(self.filepath, "w") as f:
                    json.dump(self.scores, f, indent=4)

        except (json.JSONDecodeError, IOError) as e:
            print(e)
            self.scores = []
