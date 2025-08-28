pituus = int(input("Anna kuhan pituus senttimetreinä: "))
if pituus < 37:
    puuttuu = 37 - pituus
    print (f"Kuha on alamittainen, laske se takaisin järveen.")
    print (f"Pituudesta puuttuu {puuttuu} cm vähimmäismitasta.")
else:
    print ("Kuha on pyyntimitan täyttävä, saat pitää sen.")
