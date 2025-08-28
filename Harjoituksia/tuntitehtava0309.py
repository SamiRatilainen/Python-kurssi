luku = int(input("Anna kokonaisluku: "))

if luku % 3 == 0 and luku % 5 == 0:
    print("BoomBuzz")
elif luku % 3 == 0:
    print("Boom")
elif luku % 5 == 0:
    print("Buzz")
