
gallon = int(input("Anna määrä: "))
def muutos():
    total = 3.785
    nums = total * gallon
    heitto = ("Gallona litroissa")
    print(heitto)
    return nums
while gallon > 0:
    korva = muutos()
    print(korva)
    gallon = int(input("Anna määrä: "))

