# 4.1
class Planet:
    def __init__(self, name, distance_from_sun, planet_type):
        self.name = name
        self.distance_from_sun = distance_from_sun
        self.planet_type = planet_type

    def get_distance_to_earth(self):
        # Keeping the int a positive number
        distance_to_earth = abs(self.distance_from_sun - 147000000)
        return f"{distance_to_earth} kilometers"


mars = Planet("Mars", 225000000, "Terrestrial")
distance_to_earth = mars.get_distance_to_earth()
print(distance_to_earth)

# 4.2


class Mercury(Planet):
    def __init__(self):
        name = "Mercury"
        distance_from_sun = 58000000
        planet_type = "Terrestrial"
        super().__init__(name, distance_from_sun, planet_type)

    @staticmethod
    def happy_new_year():
        return "Happy New Year to Mercury! A year on Mercury lasts 88 Earth days."


mercury = Mercury()
print(f"Name: {mercury.name}")
print(f"Distance from sun: {mercury.distance_from_sun} kilometers")
print(f"Planet type: {mercury.planet_type}")
print(mercury.get_distance_to_earth())
print(Mercury.happy_new_year())

# 4.3


class Jupiter(Planet):
    def __init__(self):
        name = "Jupiter"
        distance_from_sun = 779000000
        planet_type = "Gas Giant"
        number_of_moons = 80
        super().__init__(name, distance_from_sun, planet_type)
        self.number_of_moons = number_of_moons

    @staticmethod
    def happy_new_year():
        return "Happy new year to Jupiter! A year on Jupiter lasts 4383 Earth days."


jupiter = Jupiter()

print(f"Name: {jupiter.name}")
print(f"Distance from sun: {jupiter.distance_from_sun} kilometers")
print(f"Planet type: {jupiter.planet_type}")
print(f"Number of moons: {jupiter.number_of_moons}")
print(jupiter.get_distance_to_earth())
print(Jupiter.happy_new_year())
