import time


class Clock:
    """Clock class that define Clock properties"""
    def __init__(self, level_max_time: int) -> None:
        """constructor method"""
        self.oldTime = time.time()
        self.level_max_time = level_max_time
        if self.level_max_time is None:
            self.level_max_time = 90
        self.pauseTime = 0.0
        self.pauseMenu = False
        self.pauseTimeCheateMode = False

    def getRemainingTime(self) -> int:
        """get the remaining time"""
        return (self.level_max_time - int(time.time() - self.oldTime))
