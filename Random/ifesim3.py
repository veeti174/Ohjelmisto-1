#if-ehto ja loogise operaattorit

luku = int(input("Anna 3:lla jaollinen luku, joka on alle 20 "))

#Ehdot: jaollinen 3:lla ja alle 20
# sulut koodissa eivät ole nyt pakollisia

if (luku % 3 == 0)  and (luku < 20):
    print("Osaisit, hyvä!")
else:
    print("Tollo!")

