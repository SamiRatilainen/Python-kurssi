luvut = []

luku = input("Anna luku: ")

while luku != "":
    luvut.append(float(luku))
    luku = input("Anna luku: ")

if luvut:
    print("Pienin luku:", min(luvut))
    print("Suurin luku:", max(luvut))
else:
    print("Et antanut yhtään lukua.")