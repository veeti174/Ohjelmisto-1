nimi = ()
lista = set()
while nimi != "":
    nimi = input("Anna nimi: ")
    if nimi in lista:
        lista.add(nimi)
        print("Aikaisemmin syötetty nimi.")
    elif nimi == "":
        break
    else:
        print("Uusi nimi")
        lista.add(nimi)
print(*lista, sep = "\n")
