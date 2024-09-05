import math

def calculate_square_price(diameter, price):
    # muutetaan sentit metreiksi
    diameter = diameter / 100
    #pizzan pinta-ala pi *r^2
    r = diameter/2
    area = math.pi * r ** 2
    return price/area

"""
Pääohjelma kysyy käyttäjältä kahden pizzan halkasija ja hinnat 
sekä ilmoittaa kumpi pizza antaa paremman vastineen rahalle

print(calculate_square_price(1, 30))
print(calculate_square_price(0.3, 20))
"""



pizza1_diameter = float(input("Syötä 1. pizzan halkaisija (cm): "))
pizza2_diameter = float(input("Syötä 2. pizzan halkaisija (cm): "))
pizza1_price = float(input("Syötä 1. pizzan hinta: "))
pizza2_price = float(input("Syötä 2. pizzan hinta: "))

pizza1_square_price = calculate_square_price(pizza1_diameter, pizza1_price)
pizza2_square_price = calculate_square_price(pizza2_diameter, pizza2_price)

print(f"Ensimmäisen pizzan neliöhinta on {pizza1_square_price:.2f}")
print(f"Ensimmäisen pizzan neliöhinta on {pizza2_square_price:.2f}")

if pizza1_square_price < pizza2_square_price:
    print("Ensimmäisen pizzan neliöhinta on halvempi kuin toisen.")
if pizza2_square_price < pizza1_square_price:
    print("Toisen pizzan neliöhinta on halvempi kuin ensimmäisen.")
elif pizza2_square_price == pizza1_square_price:
    print("Pizzoilla on sama neliöhinta")
