jakaja = ()
luku = int(input("Anna luku "))
if luku > 1:
    for jakaja in range(2, luku-1):
        if luku % jakaja == 0:
            print("Lukusi ei ole alkuluku")
            break
    else:
        print("Lukusi on alku luku ")