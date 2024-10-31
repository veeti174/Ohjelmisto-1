import numpy as np
import math
pi = math.pi

arvo = int(input("Asteet radiaaneikksi niin 1, jos toiste päin niin 2: "))

if (arvo ==1):
    asteet = int(input("Montako astetta: "))
    aste = math.pi/180*asteet
    print(f"Asteesi {asteet} radiaaneina {aste}.")

elif (arvo ==2):
    radiaanit = int(input("Montako astetta: "))
    rad = 180/math.pi * radiaanit
    print(f"Radiaanisi {radiaanit} asteina {rad}.")

else:
    print("Väärä vastaus.")
    return