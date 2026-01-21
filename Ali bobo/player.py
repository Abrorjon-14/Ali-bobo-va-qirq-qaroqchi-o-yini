class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.power = 20
        self.x = 0
        self.y = 0

    def attack(self):
        return self.power

    def info(self):
        print(f"{self.name} | Jon: {self.health} | Hujum: {self.power}")

    def move(self, step):
        if step == "w" and self.x > 0:
            self.x -= 1
        elif step == "s" and self.x < 9:
            self.x += 1
        elif step == "a" and self.y > 0:
            self.y -= 1
        elif step == "d" and self.y < 9:
            self.y += 1