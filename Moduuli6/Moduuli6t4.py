arvo1 = int(input("Anna kokonais luku: "))
arvo2 = int(input("Anna kokonais luku: "))
arvo3 = int(input("Anna kokonais luku: "))
arvo4 = int(input("Anna kokonais luku: "))
kaikki = []
kaikki.append(arvo1)
kaikki.append(arvo2)
kaikki.append(arvo3)
kaikki.append(arvo4)


def inv():

    arvo = kaikki
    print(sum(arvo))
korva = inv()
print(korva)
