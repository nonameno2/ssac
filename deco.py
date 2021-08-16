import math

# class
class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi * (self.__radius ** 2)

    # getter and setter
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self, value): 
        if value <= 0:
            raise TypeError("not a positive number")
        self.__radius = value

# circumference and area of ​​a circle
circle = Circle(5)
print("radius1: ", circle.radius)
circle.radius = 10
print("radius2: ", circle.radius)

# raise an exception
circle.radius = -5
