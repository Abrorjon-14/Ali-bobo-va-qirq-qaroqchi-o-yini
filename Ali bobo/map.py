class Map:
    def __init__(self, player, enemies, weapon, medicines):
        self.player = player
        self.enemies = enemies
        self.weapon = weapon
        self.medicines = medicines

    def draw(self):
        for i in range(10):
            for j in range(10):
                printed = False

                if i == self.player.x and j == self.player.y:
                    print("P", end=" ")
                    printed = True

                for e in self.enemies:
                    if e.health > 0 and i == e.x and j == e.y:
                        print("*", end=" ")
                        printed = True

                if i == self.weapon.x and j == self.weapon.y:
                    print("*", end=" ")
                    printed = True

                for m in self.medicines:
                    if i == m.x and j == m.y:
                        print("*", end=" ")
                        printed = True

                if not printed:
                    if i == 9 and j == 9:
                        print("*", end=" ")
                    else:
                        print("*", end=" ")
            print()