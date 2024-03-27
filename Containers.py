# List
colors = ["purple",
          "orange",
          "green"]

guess = input("Guess a color:")

if guess in colors:
    print("You guessed correctly!")
else:
    print("Wrong! Try again.")

# Tuple  
dys = ("1984",
       "Brave New World",
       "Fahrenheit 451")

# This results in an error
# dys[1] = "Handmaid's Tale"

dys[2]

# Dictionary
fruits = {"Apple":
	 "Red",
	 "Banana":
	 "Yellow"}

facts = dict()

# add a value
facts["code"] = "fun"
#look up a key
facts["code"]

# add a value
facts["Bill"] = "Gates"
#look up a key
facts["Bill"]

# add a value
facts["founded"] = "1776"
#look up a key
facts["founded"]

bill = {"Bill Gates":
        "charitable"}
"Bill Gates" in bill

"Bill Doors" not in bill

books = {"Dracula": "Stoker",
         "1984": "Orwell",
         "The Trial": "Kafka"}
del books["The Trial"]

rhymes = {"1": "fun",
          "2": "blue",
          "3": "me",
          "4": "floor",
          "5": "live"
         }

n = input("Type a number:")
if n in rhymes:
    rhyme = rhymes[n]
    print(rhyme)
else:
    print("Not found.")
          
lists = []
rap = ["Kanye West",
       "Jay Z",
       "Eminem"
       "Nas"]

rock = ["Bob Dylan",
        "The Beatles",
        "Led Zeppelin"
        ]

djs = ["Zeds Dead",
       "Tiesto"]

lists.append(rap)
lists.append(rock)
lists.append(djs)

print(lists)

rap = lists[0]
rap.append("Kendrick Lamar")
print(rap)
print(lists)

locations = []
la = (34.0522, 188.2437)
chicago = (41.8781, 87.6298)

locations.append(la)
locations.append(chicago)

print(locations)

eights = ["Edgar Allan Poe",
          "Charles Dickens"]

nines = ["Hemingway",
         "Fitzgerald",
         "Orwell"]

authors = (eights, nines)
print(authors)

bday = {"Hemingway":
        "7.21.1899",
        "Fitzgerald":
        "9.24.1896"}

my_list = [bday]
print(my_list)
my_tuple = (bday, )
print(my_tuple)

ny = {"location":
      (40.7128,
       74.0059),

      "celebs":
      ["W. Allen",
       "Jay Z",
       "K. Bacon"],

      "facts":
      {"state":
       "Ny",
       "country":
       "America"}
      }
