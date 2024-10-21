from random import randint
import numpy as np

class Auto:
    def __init__(self, plate, topspeed):
        self.plate = plate
        self.topspeed = topspeed
        self.speed = 0
        self.distance = 0


    def kiihdyta(self, nopeus):
        if self.speed + nopeus > self.topspeed:
            self.speed = self.topspeed
        elif self.speed + nopeus < 0:
            self.speed = 0
        else:
            self.speed += nopeus


    def kulje(self, aika):
        self.distance += self.speed * aika

race = []
y = 1
while y <= 10:
    race.append(Auto(f"ABC-{int(y)}", randint(100, 200)))
    y += 1

kisa = True
while kisa:
    for auto in kisa:
        auto-kiihdyta(randint(-10, 15))
        auto.kulje(1)