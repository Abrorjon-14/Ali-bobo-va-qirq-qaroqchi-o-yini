def fight(player, enemy):
    print(f"{enemy.name} bilan jang!")

    enemy.health -= player.attack()
    print("Siz zarba berdingiz")

    if enemy.health > 0:
        player.health -= enemy.attack()
        print("Qaroqchi zarba berdi")
    else:
        print("Qaroqchi yo‘q qilindi")

    player.info()
    enemy.info()


def add_attack(player, weapon):
    player.power += weapon.impact()
    print("Qurol olindi! Hujum kuchi oshdi")