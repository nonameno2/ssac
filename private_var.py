import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi * (self.__radius ** 2)

    # getter and setter
    def get_radius(self):
        return self.__radius
    def set_radius(self, value):
        self.__radius = value


circle = Circle(15)
print("circumference: ", circle.get_circumference())
print("area: ", circle.get_area())
print("radius: ", circle.get_radius())

circle.set_radius(17)
print("circumference2: ", circle.get_circumference())
print("area2: ", circle.get_area())
print("radius: ", circle.get_radius())
