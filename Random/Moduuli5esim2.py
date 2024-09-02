"""
range funktio ja for-toisto
"""

print("Tulostan parilliset luvut väliltä 10 ... 20")

for nro in range(10, 21, 2):
    # huom: alkuarvo 10 kuuluu tarkasteltavaan väliin,
    # mutta loppuarvo 21 EI kuuli.
    # Kolmas parametri (nyt 2) kertoo lisäyksen määrän
    print(nro)

print("Tulostan kaikki luvut väliltä 5 ... 10")

for nro in range(5, 11):
    # lisäksen oletuarvo on 1
    print(nro)

# Terveditään 5 kertaa
for nro in range(5):
    print(f"Hei {nro+1}, kerran")