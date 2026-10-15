import time


class Clock:
    def __init__(self, level_max_time: int) -> None:
        self.oldTime = time.time()
        self.level_max_time = level_max_time
        if self.level_max_time is None:
            self.level_max_time = 90
        self.pauseTime = 0.0
        self.pauseMenu = False
        self.pauseTimeCheateMode = False

    def getRemainingTime(self) -> int:
        return (self.level_max_time - int(time.time() - self.oldTime))
