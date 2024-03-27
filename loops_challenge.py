shows = ["The Walking Dead", "Entourage",
         "The Sopranos", "The Vampire Diaries"]

for show in shows:
    print(show)

for i in range(25, 51):
    print(i)

for i, show in enumerate(shows):
    print(i)
    print(show)



list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
list3 = []

for i in list1:
    for j in list2:
        mult = i * j
        list3.append(mult)
print(list3)


nums = [2, 4, 6, 8, 10]

while True:
    user = input("Guess a number or type q to quit")
    if user == "q":
        break
    try:
       user = int(user)
    except ValueError:
        print("please type a number or q to quit.")    
    if user in nums:
        print("You guessed correctly")
    else:
        print("You guessed incorrectly")
