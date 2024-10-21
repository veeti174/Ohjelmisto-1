class Kissa:
    # luokkamuuttuja, kaikille luokan olioille yhteinen
    kissojenLKM = 0

    # Määritellään luokan alustaja
    def __init__(self, nimi, age, tervehdys = "Miau, miau"):
        # Tervehdys-parametria ei ole pakko antaa
        self.nimi = nimi
        self.ika = age
        # Määritellään myös kolmas ominaisuus
        self.omistaja = "Tuntematon"
        self.tervehdys = tervehdys
        # Päivitetään luokkamuuttujan arvo
        Kissa.kissojenLKM += 1


    # Määritetllääm oliolle toiminto eli metodi
    def tervehdi(self):
        print(self.tervehdys)


tokaKissa = Kissa("Mörri", 3, "MOOUU!!!")
kolmasKissa = Kissa("Mirri", 1)
# Kutsutaan olioiden toimintoa
tokaKissa.tervehdi()
kolmasKissa.tervehdi()
# Tulostan luokkamuuttujan arvon
print(f"Kissa-olioita on luotu {Kissa.kissojenLKM} kpl" )