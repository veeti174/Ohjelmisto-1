# , speed="0", distance="0"
class Auto:
    def __init__(self, plate, topspeed):
        self.plate = plate
        self.topspeed = topspeed
        self.speed = 0
        self.distance = 0


    def kiihduta(self, nopeus):
        if self.speed + nopeus < self.topspeed:
            self.speed = self
        elif:

        else:


auto = Auto("ABC-123", "142 km/h",)

print(f"Auton rekkari on {auto.plate}, max nopeus on {auto.topspeed}, nopeus tällä hetkellä on {auto.speed} km/h, ja matka mitä autolla on kuljettu on {auto.distance} km.")