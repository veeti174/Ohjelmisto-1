# Piin likiarvon laskeminen
# pii=4n/N, jossa n on yksikköympyrän sisälle osuvat pisteet, N on kaikki pisteet
# epäyhtälöllä x^2+y^2-1 testataan, onko uksittäinen piste ympyrän sisällä
# TOinen tapa  importata vain yksittäisiä toimintoja/funktioita
#from random import randint
# randint(.1, 1)

import math
import random
iterator = 0
#Todo: Kysy N arvo käyttäjältä
N = int(input("Montako pistettä halutaan? "))
# pisteiden kokonaismäärä
n = 0 # ympyrän sisään osuvat pisteet
while iterator < N:
    #arvotaan koordinaatiot väliltä -1 ka 1
    iterator += 1
    x = random.random() * 2 - 1
    y = random.uniform(-1, 1)
    #print(f"Satunnainen piste: {x}, {y}")
    #print(x**2 +y**2 < 1)
    if x**2 +y**2 < 1:
        #print("Osui ympyran sisalle.")
        n += 1
print(f"{N} pisteestä {n} osui yksikkö ympyrän sisälle.")
result = 4 * n / N
print(f"Piin likiarvo on {result}")
print(f"Virhe verrattuna math.pi {math.pi:.5f} {result - math.pi:.5f}")