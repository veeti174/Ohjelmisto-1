#Harjoitustehtävä 2.3
#Lukee inputtia käyttäjältä
kanta = float(input("Paljonko on suorakulmion kanta?: "))
korkeus = float(input("Paljonko on suorakulmion korkeus?: "))
#annetaan kanta ja korkeus
pintaala = kanta * korkeus
piiri = kanta*2+korkeus*2
#Se laskee ja sitten antaa sen vastauksen
print("Suorakulmion kanta ja korkeus on " +  str(kanta) + str(korkeus) + "sen pinta-ala on: " + str(pintaala)+"suorakulmion piiri on:"+str(piiri))