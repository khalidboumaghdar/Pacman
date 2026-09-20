"""MazeAdapter module to adapt external mazegenerator for Pac-Man tile grid."""

from typing import Any, List
import mazegenerator


class Adapter:
    """Adapts external maze generator grid into a tile matrix with closed outer borders."""

    def __init__(self, width: int, height: int, seed: int = 42) -> None:
        """Initializes generator with cell dimensions and seed."""
        self.width = width
        self.height = height
        self.seed = seed

        self.generator = mazegenerator.MazeGenerator(
            (self.width, self.height),
            seed=self.seed,
            perfect=False
        )

    def _extract_val(self, cell: Any) -> int:
        """Extracts bitmask integer value from raw cell object or hex string."""
        if hasattr(cell, "value"):
            cell = cell.value
        if isinstance(cell, str):
            try:
                return int(cell, 16)
            except ValueError:
                return 15
        if isinstance(cell, int):
            return cell
        return 15

    def _get_cell(self, maze_data: Any, x: int, y: int) -> int:
        """Safely extracts cell value regardless of [y][x] or [x][y] grid structure."""
        try:
            return self._extract_val(maze_data[y][x])
        except (IndexError, TypeError):
            return self._extract_val(maze_data[x][y])

    def generate_grid(self) -> List[List[int]]:
        """Generates expanded 2D tile matrix with strictly closed outer borders."""
        print(">>> EXECUTING V3 GUARDED ADAPTER <<<")
        
        result: Any = self.generator.generate()
        source: Any = result if result is not None else self.generator
        maze_data: Any = getattr(
            source, "grid", getattr(source, "maze", source)
        )

        grid_height = 2 * self.height + 1
        grid_width = 2 * self.width + 1

        # 1. Initialize all tiles as solid walls (1)
        grid: List[List[int]] = [
            [1 for _ in range(grid_width)] for _ in range(grid_height)
        ]

        # 2. Carve paths (Guarded to NEVER touch the outer index)
        for y in range(self.height):
            for x in range(self.width):
                val = self._get_cell(maze_data, x, y)

                if val == 15:
                    continue

                cy, cx = 2 * y + 1, 2 * x + 1
                grid[cy][cx] = 0

                # Bit 0 (1): North path
                if not (val & 1) and y > 0:
                    if self._get_cell(maze_data, x, y - 1) != 15:
                        grid[cy - 1][cx] = 0

                # Bit 1 (2): East path
                if not (val & 2) and x < self.width - 1:
                    if self._get_cell(maze_data, x + 1, y) != 15:
                        grid[cy][cx + 1] = 0

                # Bit 2 (4): South path (This prevents the bottom-row holes)
                if not (val & 4) and y < self.height - 1:
                    if self._get_cell(maze_data, x, y + 1) != 15:
                        grid[cy + 1][cx] = 0

                # Bit 3 (8): West path
                if not (val & 8) and x > 0:
                    if self._get_cell(maze_data, x - 1, y) != 15:
                        grid[cy][cx - 1] = 0
        # 3. Absolute Perimeter Seal (Overrides any stray paths mathematically)
        for x in range(grid_width):
            grid[0][x] = 1
            grid[grid_height - 1][x] = 1
        for y in range(grid_height):
            grid[y][0] = 1
            grid[y][grid_width - 1] = 1
        # Absolute Perimeter Seal
        for x in range(grid_width):
            grid[0][x] = 1
            grid[grid_height - 1][x] = 1

        for y in range(grid_height):
            grid[y][0] = 1
            grid[y][grid_width - 1] = 1
        return grid