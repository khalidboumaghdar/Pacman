from mlx import Mlx
from typing import Any


class Renderer:
    # Keycodes (X11 / 42 Cluster Linux)
    KEY_W = 119
    KEY_A = 97
    KEY_S = 115
    KEY_D = 100

    KEY_UP = 65362
    KEY_LEFT = 65361
    KEY_DOWN = 65364
    KEY_RIGHT = 65363

    KEY_ESC = 65307

    # X11 Event Types and Masks
    EVENT_KEY_PRESS = 2
    MASK_KEY_PRESS = 1 << 0

    EVENT_DESTROY_NOTIFY = 17  # Red "X" button
    MASK_NO_MASK = 0

    def __init__(self, player: Any, game: Any):
        self.mlx = Mlx()
        self.mlx_ptr = self.mlx.mlx_init()
        self.win = self.mlx.mlx_new_window(self.mlx_ptr, 1400, 1200, "Pac-man")
        self.player = player
        self.game = game

    def setup_hooks(self) -> None:
        # 1. Store callback in self so Python Garbage Collector never deletes it
        self._key_callback = self.handle_key_press
        self._close_callback = self.close_game

        # 2. Pass the saved references to mlx_hook
        self.mlx.mlx_hook(
            self.win,
            self.EVENT_KEY_PRESS,
            self.MASK_KEY_PRESS,
            self._key_callback,
            None
        )

        self.mlx.mlx_hook(
            self.win,
            self.EVENT_DESTROY_NOTIFY,
            self.MASK_NO_MASK,
            self._close_callback,
            None
        )

    def handle_key_press(self, keycode: int, param=None) -> int:
        """Callback triggered by MLX on key press."""
        if keycode in (self.KEY_W, self.KEY_UP):
            self.player.nextDirection = "UP"
        elif keycode in (self.KEY_S, self.KEY_DOWN):
            self.player.nextDirection = "DOWN"
        elif keycode in (self.KEY_A, self.KEY_LEFT):
            self.player.nextDirection = "LEFT"
        elif keycode in (self.KEY_D, self.KEY_RIGHT):
            self.player.nextDirection = "RIGHT"
        elif keycode == self.KEY_ESC:
            self.close_game()

        return 0

    def close_game(self, param=None) -> int:
        """Safely terminates the game loop and destroys the MLX window."""
        self.game.isRunning = False
        if self.mlx and self.win:
            self.mlx.mlx_destroy_window(self.win)
            self.win = None
        return 0
