import random

class Medicine:
    def __init__(self, name):
        self.name = name
        self.heal = 20
        self.x = random.randint(0, 9)
        self.y = random.randint(0, 9)

    def use(self, player):
        player.health += self.heal
        if player.health > 100:
            player.health = 100
        print("Dori ishlatildi! Jon tiklandi")