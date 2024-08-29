import random
arvaus = ""
salaisuus = random.randint(1,10)
while salaisuus != arvaus:
    arvaus = int(input("Arvaa: "))
    if salaisuus < arvaus:
        print("Liian suuri arvaus. ")
    if salaisuus > arvaus:
        print("Liian pieni arvaus. ")
    if salaisuus == arvaus:
        print("Oikein hurraa! ")