import math

def pizza_unit_price_eur_per_m2(diameter_cm: float, price_eur: float) -> float:
    radius_cm = diameter_cm / 2
    area_cm2 = math.pi * radius_cm * radius_cm
    area_m2 = area_cm2 / 10_000
    return price_eur / area_m2

d1 = float(input("Pizza 1 halkaisija (cm): "))
p1 = float(input("Pizza 1 hinta (€): "))
d2 = float(input("Pizza 2 halkaisija (cm): "))
p2 = float(input("Pizza 2 hinta (€): "))

u1 = pizza_unit_price_eur_per_m2(d1, p1)
u2 = pizza_unit_price_eur_per_m2(d2, p2)

print(f"Pizza 1: {u1:.2f} €/m²")
print(f"Pizza 2: {u2:.2f} €/m²")

if u1 < u2:
    print("Pizza 1 on edullisempi.")
elif u2 < u1:
    print("Pizza 2 on edullisempi.")
else:
    print("Pizzat ovat yhtä edullisia.")