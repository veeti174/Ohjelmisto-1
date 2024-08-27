# Harjoitustehtävä 1.1 ja 1.2

#print("Hei Veeti Isokangas!")

# Harjotustehtävä 2.1
#Lukee inputtia käyttäjältä

name = input('Kuka olet?: ')

# printtaa inputtia

print("Moi, " + name + "!")

#Harjoitustehtävä 2.2

#Lukee inputtia käyttäjältä
säde = float(input("Paljonko on ympyrän säde?: "))
#annetaan pinta
pintaala = 3.14159265359 * säde ** 2
pintaala = round(pintaala, 3) #pyöristää
#Se laskee ja sitten antaa sen vastauksen
print("Ympyran sade on " + str(säde) + " ja pintaala on: " + str(pintaala))

