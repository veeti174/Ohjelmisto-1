empty = (-0)
arvot = []
arvo = int(input("Anna kokonaisluku yksikerrallaan: "))
if arvo != empty:
    arvot.append(arvo)
    arvot.sort()
while arvo != empty:
    arvo = int(input("Anna kokonaisluku yksikerrallaan ja kun olet valmis kirjoita -0: "))
    if arvo == empty:
        break
    arvot.append(arvo)
    arvot.sort()



def inv():

    arvotus = arvot
    print(sum(arvotus))
korva = inv()
print(korva)
