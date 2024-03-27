name = "Ted"
for character in name:
    print(character)

tv = ["GOT",
         "Narcos",
         "Vice"]

for i, show in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new
    
print(tv)

all_shows = []

for show in tv:
    show = show.upper()
    all_shows.append(show)

coms = ("A. Development",
        "Friends",
        "Always Sunny")

for show in coms:
    show = show.upper()
    all_shows.append(show)
    
people = {"G. Bluth II":
          "A. Development",
          "Barney":
          "HIMYM",
          "Dennis":
          "Always Sunny"}

for character in people:
    print(character)

print(all_shows)

for i in range(1, 11):
    print(i)

x = 10
while x > 0:
    print('{}'.format(x))
    x -= 1
print("Happy New Year!")

for i in range(0, 100):
    print
    break

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1


for i in range(1, 3):
    print(i)
    for letter in ["a", "b", "c"]:
        print(letter)


list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
added = []
for i in list1:
    for j in list2:
        added.append(i + j)

print(added)


while input('y or n?') != 'n':
    for i in range(1, 6):
        print(i)

qs = ["What is your name?",
      "What is your fav. color?",
      "What is your quest?"]
n = 0
while True:
    print("Type q to quit")
    a  = input(qs[n])
    if a == "q":
        break
    n = (n + 1) % 3
