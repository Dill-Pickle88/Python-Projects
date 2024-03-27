import random

def rock_paper_scissors():
    print("Welocome to rock, paper, scissors")

    randAnswers = ["rock", "paper", "scissors"]

    answer = randAnswers[random.randint(0,2)]

    while True:
        user = input(" Choose rock, paper or scissors: ")
        
        if (user == "rock" and answer == "scissors") or (user == "paper" and answer == "rock") or (user == "scissors" and answer == "paper"):
            print("You win!")
            break
        elif (answer == "rock" and user == "scissors") or (answer == "paper" and user == "rock") or (answer == "scissors" and user == "paper"):
              print("You lose!")
              break
        else:
            print("It's a tie!")
            break

rock_paper_scissors()

    
