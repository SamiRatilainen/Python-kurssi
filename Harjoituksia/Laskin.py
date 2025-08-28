print("-----Tervetuloa käyttämään laskinta!-----")
print("Valitse mitä toimintoa haluat käyttää:")
print("A: Yhteenlasku")
print("B: Vähennyslasku")
print("C: Kertolasku")
print("D: Jakolasku")

valinta = input("Valintasi (A - D): ").upper()

if valinta == "A":
    a = float(input("Anna ensimmäinen luku: "))
    b = float(input("Anna toinen luku: "))
    print("Yhteenlasku:", a + b)

elif valinta == "B":
    a = float(input("Anna ensimmäinen luku: "))
    b = float(input("Anna toinen luku: "))
    print("Vähennyslasku:", a - b)

elif valinta == "C":
    a = float(input("Anna ensimmäinen luku: "))
    b = float(input("Anna toinen luku: "))
    print("Kertolasku:", a * b)

elif valinta == "D":
    a = float(input("Anna ensimmäinen luku: "))
    b = float(input("Anna toinen luku: "))
    if b != 0:
        print("Jakolasku:", a / b)
    else:
        print("Nollalla ei voi jakaa!")

else:
    print("Valintasi oli virheellinen.")
