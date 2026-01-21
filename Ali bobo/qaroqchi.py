import random

class Enemy:
    def __init__(self, name):
        self.name = name
        self.health = 30
        self.x = random.randint(0, 9)
        self.y = random.randint(0, 9)

    def attack(self):
        return 20

    def info(self):
        print(f"{self.name} joni: {self.health}")