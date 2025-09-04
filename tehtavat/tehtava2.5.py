leiviska_naula = 20
naula_luoti = 32
luoti_gramma = 13.3

leiviskat = float(input("Anna leiviskät. "))
naulat = float(input("Anna naulat. "))
luodit = float(input("Anna luodit. "))

grammat = (leiviskat * leiviska_naula * naula_luoti + naulat * naula_luoti + luodit) * luoti_gramma

kilot = int(grammat // 1000)
grammat_yli = grammat % 1000

print (f"\nMassa nykymittojen mukaan:")
print(f"{kilot} kilogrammaa ja {grammat_yli:.2f} grammaa.")
