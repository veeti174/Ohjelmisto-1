import numpy as np
import math
pi = math.pi

kateetti1 = int(input("Ensimmäisen kateetin pituus: "))
kateetti2 = int(input("Toisen kateetin pituus: "))
hypotenuusa = (kateetti1**2+kateetti2**2)**0.5
print(f"Ensimmäinen kateetti on {kateetti1} pitkä ja toinen kateetti on {kateetti2} pitkä ja hypotenuusa on {hypotenuusa} pitkä.")