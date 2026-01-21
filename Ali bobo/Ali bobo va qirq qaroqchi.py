from player import *
from qaroqchi import *
from weapons import *
from medicine import *
from fight import *
from map  import *

oyinchi = Player("Ali bobo")

qaroqchilar = []
for i in range(6):
    qaroqchilar.append(Enemy(f"Qaroqchi {i+1}"))

weapon = Weapons("Xanjar")

medicines = []
for i in range(3):
    medicines.append(Medicine(f"Dori {i+1}"))

xarita = Map(oyinchi, qaroqchilar, weapon, medicines)

# ================= MAIN =================
while True:
    xarita.draw()

    if oyinchi.x == 9 and oyinchi.y == 9:
        print("Tabriklayman! Finishga yetdingiz!")
        break

# Qaroqchi bilan urushish
    for qaroqchi in qaroqchilar:
        if qaroqchi.health > 0 and oyinchi.x == qaroqchi.x and oyinchi.y == qaroqchi.y:
            fight(oyinchi, qaroqchi)
            if oyinchi.health <= 0:
                print("Siz yutqazdingiz!")
                exit()

# Qurol olish
    if oyinchi.x == weapon.x and oyinchi.y == weapon.y:
        add_attack(oyinchi, weapon)
        weapon.x = -1
        weapon.y = -1

# Jon qo'shish
    for m in medicines:
        if oyinchi.x == m.x and oyinchi.y == m.y:
            m.use(oyinchi)
            m.x = -1
            m.y = -1

    print("Harakatlar: w-tepa | s-past | a-chap | d-o‘ng")
    step = input("Yo‘nalish: ")
    oyinchi.move(step)