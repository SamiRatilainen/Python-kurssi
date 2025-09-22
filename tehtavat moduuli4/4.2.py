tuuma = float(input("Anna tuumat: "))

while tuuma >= 0:
    cm = tuuma * 2.54
    print(f"{tuuma} tuumaa = {cm:.2f} cm")
    tuuma = float(input("Anna tuumat: "))

print("Ohjelma lopetettu.")