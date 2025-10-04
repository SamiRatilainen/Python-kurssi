luvut = []
while True:
    syote = input("Anna luku (tyhjä lopettaa): ")
    if syote == "":
        break
    luvut.append(int(syote))

luvut.sort(reverse=True)
print("Viisi suurinta:", luvut[:5])