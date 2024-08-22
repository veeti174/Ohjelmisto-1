# Harjoitustehtava 2.4
#Reads input from users
numero1 = float(input("Anna mulle kolme kokonaislukua yksi kerrallaan.: "))
numero2 = float(input("Anna mulle vielä kaks kokonaislukua erikseen yksi luku kerrallaan.: "))
numero3 = float(input("Anna mulle se vika kokonaisluku!: "))
#Now that we the kokonaisluvut we can calculate the summa, keskiarvo and tulo
summa =numero1+numero2+numero3
keskiarvo =summa/3
tulo = numero1*numero2*numero3
#Now that we have the bases completed whe only have to present them to the user
print("Tässä on kokonaislukujen summa"+ str(summa) +"keskiarvo"+ str(keskiarvo)+ "tulo" + str(tulo))