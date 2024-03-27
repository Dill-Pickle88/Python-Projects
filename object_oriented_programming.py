
class Data:

    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]

    def change_data(self, index, n):
        self.nums[index] = n

data_one = Data()
data_one.nums[0] = 100
print(data_one.nums)

data_two = Data()
data_two.change_data(0, 100)
print(data_two.nums)

class PublicPrivateExample:
    def __init__(self):
        sefl.public = "safe"
        self._unsafe = "unsafe"

        def public_method(self):
            # clients can use this
            pass

        def _unsafe_method(self):
            # cilents shouldn't use this
            pass

print(type("Hello, World!"))
print(type(200))
print(type(200.1))


# Do not run

# Drawing shapes
# w/o polymorphism
# shapes = [tr1, sq1, cr1]
# for a_shape in shapes:
"""
    if type(a_shape) == "Triangle":
        a_shape.draw_triangle()
    if type(a_shape) == "Sqaure":
        a_shape.draw_sqaure()
    if type(a_shape) == "Circle":
        a_shape.draw_circle()
"""

# Drawing shapes
# with polymorphism
# shapes = [tr1,
          # sw1,
          # cr1]
# for a_shape in shapes:
   #  a_shape.draw()

class Shape():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("""{} by {}
              """.format(self.width,
                         self.len))
my_shape = Shape(20, 25)
my_shape.print_size()

class Square(Shape):
    def area(self):
        return self.width * self.len

    def print_size(self):
        print("""I am {} by {}
              """.format(self.width,
                         self.len))

a_square = Square(20,20)
a_square.print_size()

class Dog():
    def __init__(self,
                 name,
                 breed,
        owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person():
    def __init__(self):
        self.name = 'Bob'

bob = Person()
same_bob = bob
print(bob is same_bob)
another_bob = Person()
print(bob is another_bob)

# mick = Person("Mick Jagger")
#stan = Dog("Stanley",
          # "Bulldog",
           # mick)
# print(stan.owner.name)

class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

lion = Lion("Dilbert")
print(lion)

class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        return abs(self.n + other.n)

x = AlwaysPositive(-20)
y = AlwaysPositive(10)

print(x + y) 

x = 10
if x is None:
    print("x is None :( ")
else:
    print("x is not None")

x = None
if x is None:
    print("x is None :(")
else:
    print("x is not None")
    
