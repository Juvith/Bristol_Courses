#KPMG Coding Challenge
import random
print("Welcome to the Game of Rock, Paper, Scissors")
#change in the user print statement and above print statement
user_choice = input("What is your Selection? (Rock, Paper or Scissors): ")

if user_choice == "Paper" :
    print("You picked: " + user_choice)
elif user_choice == "Scissors" :
    print("You picked: " + user_choice)
else :
    print("You picked: " + user_choice)

computer_picked = random.choice(["Rock","Paper","Scissors"])
print("The computer picked: " + computer_picked)

if computer_picked == "Rock" :
    if user_choice == "Paper" :
        print("You Loose")
    elif user_choice == "Scissors" :
        print("You Loose")
    else :
        print("Draw")
elif computer_picked == "Paper" :
    if user_choice == "Rock" :
        print ("You Win")
    elif user_choice == "Scissors" :
        print("You Win")
    else :
        print("Draw")
else :
    if user_choice == "Rock" :
        print("You Win")
    elif user_choice == "Paper" :
        print("You Loose")
    else :
        print("Draw")
