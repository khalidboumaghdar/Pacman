"""Configuration loader module using Object-Oriented Programming (OOP)."""

import json
import os
from typing import Any, Dict


class Loader:
    """Handles loading, parsing, and validating configuration files with safe defaults."""

    # Safe default fallback values required by Subject V.3
    DEFAULT_CONFIG: Dict[str, Any] = {
        "highscore_filename": "highscores.json",
        "lives": 3,
        "points_per_pacgum": 10,
        "points_per_super_pacgum": 50,
        "points_per_ghost": 200,
        "seed": 42,
        "level_max_time": 90,
        "levels": [{"width": 15, "height": 15}],
    }

    def __init__(self, filepath: str) -> None:
        """Initializes the loader with a target file path and loads configuration data."""
        self.filepath: str = filepath
        self.config_data: Dict[str, Any] = self._load_config()

    def _strip_comments(self, content: str) -> str:
        """Strips lines starting with '#' from the configuration string."""
        clean_lines = []
        for line in content.splitlines():
            if not line.strip().startswith("#"):
                clean_lines.append(line)
        return "\n".join(clean_lines)

    def _load_config(self) -> Dict[str, Any]:
        """Loads JSON config file, strips comments, and falls back to safe defaults on error."""
        config = self.DEFAULT_CONFIG.copy()

        if not os.path.exists(self.filepath):
            print(
                f"[Warning] Config file '{self.filepath}' not found. "
                "Using default values."
            )
            return config

        try:
            with open(self.filepath, "r", encoding="utf-8") as file:
                raw_content = file.read()

            clean_content = self._strip_comments(raw_content)
            parsed_data = json.loads(clean_content)

            if isinstance(parsed_data, dict):
                for key, value in parsed_data.items():
                    config[key] = value
            else:
                print("[Warning] Invalid JSON root format. Using default values.")

        except Exception as err:
            print(
                f"[Warning] Error parsing '{self.filepath}': {err}. "
                "Using default values."
            )

        return config