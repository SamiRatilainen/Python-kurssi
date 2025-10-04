import random

n = int(input("Anna arpakuutioiden lukumäärä: "))
summa = 0
for i in range(n):
    silmaluku = random.randint(1, 6)
    print("Heitto:", silmaluku)
    summa += silmaluku
print("Silmälukujen summa:", summa)