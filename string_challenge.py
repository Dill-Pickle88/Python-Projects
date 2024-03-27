string = "Camus"
print(string[0])
print(string[1])
print(string[2])
print(string[3])
print(string[4])




print("aldous Huxley was born in 1894".title())

string4 = "Where now? Who now? When now?"

print(string4.split("?"))


fox = ["The", "fox", "jumped", "over", "the", "fence", "."]
fox = " ".join(fox)
fox = fox[0:-2] + "."
print(fox)

s = "A screming comes across the sky."
print(s.replace("s", "$"))

m = "Hemingway"
print(m.index("m"))

my_qoute = " I solemnly swear I am up to no good.\""
print(my_qoute)

con = "three" + "three" + "three"
print(con)

mult = "three" * 3
print(mult)

string6 = "It was a bright cold day in April, and the clocks were striking thirteen."
print(string6[:33])

string1 = input("Enter a word:")
string2 = input("Enter a word:")

print("Yesterday I wrote a {}. I sent it to {}!".format(string1, string2))
