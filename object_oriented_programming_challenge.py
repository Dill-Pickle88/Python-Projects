
def compareObjects(obj1, obj2):
    return obj1 is obj2

print(compareObjects("a", "a"))

class Shape():
    def __init_(self, side):
        self.side = side

    def what_am_i(self):
        print("I am a shape")

class Square(Shape):

    sqaure_list = []

    def __init__(self, s):
        self.sides = s
        self.sqaure_list.append(self)

    def calculate_permieter(self):
        return self.sides * 4

    def change_size(self, new_size):
        self.sides += new_size

    def __repr__(self):
        return """ {} by {} by {} by {}
               """.format(self.sides, self.sides,
                          self.sides, self.sides)


class Rectangle(Shape):

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_permieter(self):
        return self.width * 2 + self.length * 2
    
my_square = Square(4)
print(my_square)
print(my_square.calculate_permieter())
my_square.change_size(2)
print(my_square.calculate_permieter())
my_square.what_am_i()
my_rect = Rectangle(3, 4)

print(my_rect.calculate_permieter())
my_rect.what_am_i()


class Horse():

    def __init__(self, name, age, breed, rider):
        self.name = name
        self.age = age
        self.breed = breed
        self.rider = rider

class Rider():

    def __init__(self, name, age,):
        self.name = name
        self.age = age

mike = Rider("Mike", 33)
my_horse = Horse("Jerry", 15, "Stanlion", mike)
print(my_horse.rider.name)


