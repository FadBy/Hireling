from threading import Timer as MainTimer


class Timer(MainTimer):
    def __init__(self, time, function):
        super().__init__(time, function)
        self.time = time
        self.function = function

    def start(self):
        super().__init__(self.time, self.function)
        super().start()





