# , speed="0", distance="0"
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


autor = Auto("ABC-123", 142,)
autor.kiihdyta(30)
autor.kiihdyta(70)
autor.kiihdyta(50)
print(autor.speed)
auto.kiihdyta(-200)
print(autor.speed)
#print(f"Auton rekkari on {auto.plate}, max nopeus on {auto.topspeed} km/h, nopeus tällä hetkellä on {auto.speed} km/h, ja matka mitä autolla on kuljettu on {auto.distance} km.")