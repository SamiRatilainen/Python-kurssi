import random

koodi3 = ""
for _ in range(3):
    koodi3 += str(random.randint(0, 9))

koodi4 = ""
for _ in range(4):
    koodi4 += str(random.randint(1, 6))

print("Kolminumeroinen koodi:", koodi3)
print("Nelinumeroinen koodi:", koodi4)