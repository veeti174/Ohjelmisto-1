"""
Määritellään Kissa-luokka.
Luokalla on KOlem ominaisuutta.
"""

#new*
class Kissa:
    # Määritellään luokan alustaja
    def __init__(self, nimi, age):
        self.nimi = nimi
        self.ika = age
        # Määritellään myös kolmas ominaisuus
        self.omistaja = "Tuntematon"

# Pääohjelma
# Luodaaan uusi Kissa-tyyppinen olio
ekaKissa = Kissa("Pörri", 3)
# Tulostetaan kissan arvoja
print(f"Kissa nimi on {ekaKissa.nimi} ja kissan ikä")