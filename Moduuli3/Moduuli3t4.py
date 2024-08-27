arvo = int(input("Mika vuosi on? "))

if (arvo % 4 == 0):
    if (arvo % 100 == 0) and (arvo % 400 == 0):
        print("Vuosi "+str(arvo)+" on karkausvuosi.")
    else:
        print("Vuosi " + str(arvo) + " ei ole karkausvuosi.")
else:
    print("Vuosi "+str(arvo)+" ei ole karkausvuosi.")