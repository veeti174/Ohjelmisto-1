#importataan random
import random
#Tässä randomoidaan niitä numeroita ensimmäiseen numerokoodiin
numero1 = random.randint(0,9)
numero2 = random.randint(0,9)
numero3 = random.randint(0,9)

#Tässä randomoidaan numeroita toiseen numero kooidiin, joka on 4 merkin pituinen 1-6 väliltä
num1 = random.randint(1,6)
num2 = random.randint(1,6)
num3 = random.randint(1,6)
num4 = random.randint(1,6)
print("Tässä on kolminumeroinen numerokoodi " +str(numero1)+str(numero2)+str(numero3)+" ja tässä on se nelinumeroine on numerokoodi "+str(num1)+str(num2)+str(num3)+str(num4))

