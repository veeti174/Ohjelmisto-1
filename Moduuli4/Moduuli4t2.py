command = ""
while command != "lopeta":
    arvo = int(input("Miten pitkä on se? "))
    tulo = arvo * 2.54
    print(f"Sen pituus cm on {tulo}.")
    if arvo < 0:
        print("moro")
        exit(1)