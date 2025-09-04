sukupuoli = input ("Anna sukupuoli (nainen/mies): ").lower()
hb = int(input("Anna hemoglobiiniarvo (g/l): "))
if sukupuoli == "nainen":
    if hb < 117:
        print ("Hemoglobiiniarvo on alhainen.")
    elif hb <= 175:
        print ("Hemoglobiiniarvo on normaali.")
    else:
        print ("Hemoglobiiniarvo on korkea.")
if sukupuoli == "mies":
    if hb < 134:
        print("Hemoglobiiniarvo on alhainen.")
    elif hb <= 195:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")
else:
    print ("Virheellinen sukupuoli.")
