import time


class Clock:
    def __init__(self, level_max_time: int):
        self.oldTime = time.time()
        self.level_max_time = level_max_time
        if self.level_max_time == None:
            self.level_max_time = 90
        self.pauseTime = 0

    def getRemainingTime(self):
        return (self.level_max_time - int(time.time() - self.oldTime))