from threading import Timer as MainTimer


class Timer(MainTimer):
    def __init__(self, time, function):
        super().__init__(time, function)
        self.time = time
        self.function = function
        self.timer = MainTimer(self.time, self.function)

    def start(self):
        self.timer = MainTimer(self.time, self.function)
        self.timer.start()

    def cancel(self):
        self.timer.cancel()

