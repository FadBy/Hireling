from various import animations
from watchtimer import Timer


class Animator:
    def __init__(self, owner, animation, default, time):
        self.owner = owner
        self.animation = animation
        self.default = default
        self.time = time
        self.frame = 0
        self.started = False
        self.timer = Timer(self.time / len(self.animation), self.change)

    def start(self):
        if not self.started:
            self.started = True
            self.owner.active_animation = self
            self.change()

    def change(self):
        if self.frame != len(self.animation) - 1:
            self.frame += 1
            self.owner.image = self.animation[self.frame]
            self.timer.start()
        else:
            self.started = False
            self.frame = 0

    def cancel(self):
        if self.started:
            self.timer.cancel()
            self.frame = 0
            self.started = False
