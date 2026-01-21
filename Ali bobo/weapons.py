import random

class Weapons:
    def __init__(self, name):
        self.name = name
        self.x = random.randint(0, 9)
        self.y = random.randint(0, 9)

    def impact(self):
        return 10