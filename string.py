""" line one
    line two
    line three
"""

author = "Kafka"
author[0]
author[1]
author[2]
author[3]
author[4]
author[-1]
author[-2]
author[-3]

ff = "F. Fitzgerald"
ff = "F. Scott Fitzgerald"
print(ff)

print("cat " + "in" + " the" + " hat")
print("Sawyer" * 3)

print("We hold these truths...".upper())
print("SO IT GOES.".lower())
print("four score and...".capitalize())

last = "Faulkner"
print("William {}".format(last))

author = "William Faulkner"
year_born = "1897"

print("{} was born in {}.".format(author, year_born))

print("Hello.Yes!".split("."))

first_three = "abc"
result = "+".join(first_three)
print(result)

words = ["The",
         "fox",
         "jumped",
         "over",
         "the",
         "fence",
         "."]
one = " ".join(words)
print(one)

n1 = input("Enter a noun:")
v = input("Enter a verb:")
adj = input("Enter an adj:")
n2 = input("Enter a noun:")

r = """The {} {} the {} {}
    """.format(n1,
               v,
               adj,
               n2)
print(r)

s = "    The    "
s = s.strip()
print(s)

equ = "All animals are equal."
equ = equ.replace("a", "@")
print(equ)
    
print("animals".index("m"))

print("Cat" in "Cat in the hat.")

print("She said \"Surely.\"")

print("line1\nline2\nline3")

fict = ["Tolstoy",
        "Camus",
        "Orwell",
        "Huxley",
        "Austin"]

print(fict[0:3])

ivan = "In place of death there was light."

print(ivan[:17])
print(ivan[17:])
print(ivan[:])
