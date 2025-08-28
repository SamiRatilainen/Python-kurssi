n = int(input("Anna kokonaisluku: "))

if n > 0:
    if n % 2 == 0:
        print("Numero on parillinen")
    else:
        print("Numero on pariton")
else:
    print("Numero oli nagatiivinen tai nolla.")
