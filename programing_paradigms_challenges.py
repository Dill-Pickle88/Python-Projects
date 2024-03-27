import math



class Apple:
    def __init__(self, c, t, w,s):
        self.color = c
        self.type = t
        self.weight = w
        self.size = s
        
class Circle:

    def __init__(self, c, r):
        self.circumference = c
        self.radius = r

    def area(self):
        return math.pi * self.radius**2

circle = Circle(10, 5)
print(circle.area())

class Triangle:

    def __init__(self, base, height):
        self.base = base
        self.height = height


    def area(self):
        return 1/2 * self.base * self.height

triangle = Triangle(3, 6)
print(triangle.area())


class Hexagon:

    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6

    def calculate_perimeter(self):
        return self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.s6

hexagon = Hexagon(4, 6, 8, 10, 12, 15)
print(hexagon.calculate_perimeter())
