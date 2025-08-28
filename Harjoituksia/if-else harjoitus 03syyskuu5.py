nimi = input("Kerro nimesi: ").lower()

if nimi != "matti":
    annokset = int(input("Montako keittoannosta? "))
    print(f"Kokonaishinta on ", annokset * 5.9)
    print("Seuraava, kiitos!")
else:
    print("Seuraava, kiitos!")




