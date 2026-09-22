"""MazeModel class representing the active level structure."""

from typing import List
from src.maze.adapter import Adapter


class MazeModel:
    """Data model exposing maze dimensions, tile bounds, and wall collision checks."""

    def __init__(self, width: int = 15, height: int = 15, seed: int = 42) -> None:
        """Loads maze layout via adapter."""
        adapter = Adapter(width=width, height=height, seed=seed)
        self.grid: List[List[int]] = adapter.generate_grid()