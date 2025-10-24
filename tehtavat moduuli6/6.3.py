def gallons_to_liters(gallons: float) -> float:
    return gallons * 3.785

while True:
    g = float(input("Anna määrä gallonoina (negatiivinen päättää): "))
    if g < 0:
        break
    print(f"{g} gallonaa = {gallons_to_liters(g):.3f} litraa")