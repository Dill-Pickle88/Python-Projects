rock = []
country = []

def collect_songs():
    song = "Enter a song."
    ask = "Type r or c. q to quit"

    while True:
        genre = input(ask)
        if genre == "q":
            break


        if genre == "r":
            rk = input(song)
            rock.append(rk)

        elif genre == "c":
            cy = input(song)
            country.append(cy)

        else:
            print("Invalid.")

        print(rock)
        print(country)


def increment(a):
    return a + 1

class Orange():
    def __init__(self):
        """all weights are in oz"""
        self.weight = 6
        self.color = 'orange'
        self.mold = 0

    def rot(self, days, temperature):
        self.mold = days * (temperature * .1)


orange = Orange()
print(orange.mold)
orange.rot(10, 98)
print(orange.mold)

class Rectangle():
    def __init__(self,  w, l):
        self.width = w
        self.len =l

    def area(self):
        return self.width * self.len

    def change_size(self, w, l):
        self.width = w
        self.len = l

rectangle = Rectangle(10, 20)
print(rectangle.area())
rectangle.change_size(20, 40)
print(rectangle.area())
