# Moduuli 4 - while esimerkkeja
""""""
#while True:
    #print("Ikuinen silmukka")
"""
hooray_count = int(input("Kuinka monta kertaa hurrataan? "))
hooray_counter = 0

while hooray_counter < hooray_count:  # ehdosta syntyy aina True tai false
    # tulostetaan ehdosta syntyvä arvo
    # print(hooray_counter <3)
    hooray_counter = hooray_counter + 1
    print(hooray_counter < 3)
    print(f"{hooray_counter}, kerran Hurraa!")
print(f"Hurrattiin {hooray_counter} kertaa")

"""
import random
# noppapeli

rounds = 0
total_throw_count = 0
while rounds < 100:
    rounds += 1
    die1 = die2 = counter = 0
    while die1 != 6 or die2 !=6 :
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        counter +=1
        #print(f"Nopan silmäluku: {die1}, heittojen lkm: {counter}")
    total_throw_count = total_throw_count+ counter
    print(f"Heittojen lkm: {counter}, yhteensä: {total_throw_count}")
    print(f"Heittojen lkm keskiarvo: {total_throw_count/rounds}")


"""
# komentorivikäyttöliittymä
command = ""
while command != "lopeta":
    command = input("Anna komento> ")
    if command == "tulosta":
        print("Tulostetaan")
    elif command == "lopeta":
        print("Lopetetaan ohjelma")
    elif command == "hurraa":
        hooray_count = int(input("Kuinka monta kertaa hurrataan? "))
        hooray_counter = 0

        while hooray_counter < hooray_count:  # ehdosta syntyy aina True tai false
            # tulostetaan ehdosta syntyvä arvo
            # print(hooray_counter <3)
            hooray_counter = hooray_counter + 1
            print(hooray_counter < 3)
            print(f"{hooray_counter}, kerran Hurraa!")
        print(f"Hurrattiin {hooray_counter} kertaa")
        #break # toistorakenteen suoritus loppuu heti
    else:
        print("En ymmärrä, Tarkista komentosi, kiitos.")
print("Ohlejman suoritus loppui.")
"""