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


class Kilpailu:
