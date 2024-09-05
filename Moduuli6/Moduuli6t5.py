empty = (-0)
arvot = []
rounds = 0
arvo = int(input("Anna kokonaisluku yksikerrallaan: "))
if arvo != empty:
    rounds +=1
    arvot.append(arvo)
    arvot.sort()
while arvo != empty:
    arvo = int(input("Anna kokonaisluku yksikerrallaan ja kun olet valmis kirjoita -0: "))
    rounds += 1
    if arvo == empty:
        break
    arvot.append(arvo)
    arvot.sort()



def pari():

    arvotus = arvot
    print(sum(arvotus))
korva = pari()
print(korva)

print(arvot)