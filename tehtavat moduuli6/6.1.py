import random

def roll_die():
    return random.randint(1, 6)

while True:
    n = roll_die()
    print(n)
    if n == 6:
        break