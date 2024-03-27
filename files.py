import os
import csv

os.path.join("Users",
             "bob",
             "st.txt")

st = open("st.txt", "w")
st.write("Hi from Python!")
st.close()

my_list = list()

with open("st.txt", "r") as f:
    my_list.append(f.read())

print(my_list)


with open("st.csv", "w", newline='') as f:
    w = csv.writer(f,
                   delimiter=",")
    w.writerow(["one",
                "two",
                "three"])
    w.writerow(["four",
                "five",
                "six"])
    
with open("st.csv", "r") as f:
   r = csv.reader(f, delimiter=",")
   for row in r:
       print(",".join(row))

with open("test.txt", "r") as f:
    print(f.read())


movies_list = [["Top Gun", "Risky Business", "Minority Report"],
               ["Titanic", "The Revenant", "Inception"],
               ["Training Day", "Man on Fire", "Flight"]]

with open("movie.csv", "w", newline="") as f:
    w = csv.writer(f,
                   delimiter=",")
    w.writerow(["Top Gun", "Risky Business", "Minority Report"])
    w.writerow(["Titanic", "The Revenant", "Inception"])
    w.writerow(["Training Day", "Man on Fire", "Flight"])

with open("movie.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))

answer = input("What's your favorite moive? ")

with open("moive.txt", "w") as f:
    f.write(answer)
    
