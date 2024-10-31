from random import Random

class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin = alin_kerros
        self.ylin = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros > self.ylin or kohde_kerros < self.alin:
            print(f"Kerrosta {kohde_kerros} ei ole olemassa:")
            return
        if self.nykyinen_kerros < kohde_kerros:
            while self.nykyinen_kerros < kohde_kerros:
                self.kerros_ylos()
        elif self.nykyinen_kerros > kohde_kerros:
            while self.nykyinen_kerros > kohde_kerros:
                self.kerros_alas()

    def kerros_ylos(self):
        if self.nykyinen_kerros == self.ylin:
            print("Ylin kerros jo saavutettu.")
            return
        self.nykyinen_kerros += 1
        print(f"Nykyinen kerros {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros == self.alin:
            print("Alin kerros jo saavutettu.")
            return
        self.nykyinen_kerros -= 1
        print(f"Nykyinen kerros {self.nykyinen_kerros}")

class Talo:
    def __init__(self, alin, ylin, hissien_lkm):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []
        for i in range(hissien_lkm):
            hissi = Hissi(self.alin, self.ylin)
            self.hissit.append(hissi)

    def aja_hissia(self, hissin_nro, kohdekerros):

        hissi = self.hissit[hissin_nro - 1]
        hissi.siirry_kerrokseen(kohdekerros)
        print(f"Hissi {hissin_nro} on nyt halutussa kerroksessa {kohdekerros}")
        return


    def kerro_hissien_sijainnit(self):
        print("- Talon hissien sijainnit -")
        for i in range(len(self.hissit)):
            print(f"hissi {i+1} on kerroksessa {self.hissit[i].nykyinen_kerros}")
        return

    def palohalytys(self):
        for hissi in range(len(self.hissit)):
            self.aja_hissia(hissi, self.alin)

talo = Talo(1, 15, 3)
talo.aja_hissia(3, 14)
talo.aja_hissia(1, 5)
# tarkistetaan talon hissien sijainnit
talo.kerro_hissien_sijainnit()
talo.palohalytys()