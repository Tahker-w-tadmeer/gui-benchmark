import time


class CalculateTime:
    def __init__(self, func):
        self.time = 0
        self.output = None
        self.func = func

    def execute(self):
        start = time.time_ns()
        self.output = self.func()
        end = time.time_ns()

        self.time = end - start
        return self.time