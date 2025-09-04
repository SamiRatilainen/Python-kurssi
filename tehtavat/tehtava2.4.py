#Kysytään kolme kokonaislukua
luku1 = int(input("Anna ensimmäinen kokonaisluku: "))
luku2 = int(input("Anna toinen kokonaisluku: "))
luku3 = int(input("Anna kolmas kokonaisluku: "))

#Lasketaan summa, tulo ja ka.
summa = luku1+luku2+luku3
tulo = luku1 * luku2 * luku3
keskiarvo = summa / 3

#Tulostetaan vastaukset
print(f"Lukujen summa on {summa} ")
print(f"Lukujen tulo on {tulo} ")
print(f"Lukujen keskiarvo on {keskiarvo:.2f} ")
