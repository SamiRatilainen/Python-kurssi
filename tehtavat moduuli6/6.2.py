import random

def roll_die_sides(sides: int):
    return random.randint(1, sides)

sides = int(input("Nopan tahkojen määrä: "))
while True:
    n = roll_die_sides(sides)
    print(n)
    if n == sides:
        break