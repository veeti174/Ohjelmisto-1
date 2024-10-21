
class Auto:
    def __init__(self, plate, topspeed):
        self.plate = plate
        self.topspeed = topspeed
        self.speed = 60
        self.distance = 2000


    def kiihdyta(self, nopeus):
        if self.speed + nopeus > self.topspeed:
            self.speed = self.topspeed
        elif self.speed + nopeus < 0:
            self.speed = 0
        else:
            self.speed += nopeus


    def kulje(self, aika):
        self.distance += self.speed * aika



autor = Auto("ABC-123", 142,)

print(autor.distance)
autor.kulje(1.5)
print(autor.distance)

autor.kiihdyta(30)
autor.kiihdyta(70)
autor.kiihdyta(50)
print(autor.speed)
autor.kiihdyta(-200)
print(autor.speed)
#print(f"Auton rekkari on {auto.plate}, max nopeus on {auto.topspeed} km/h, nopeus tällä hetkellä on {auto.speed} km/h, ja matka mitä autolla on kuljettu on {auto.distance} km.")
