#KPMG Coding Challenge
import random
print("Welcome to Rock, Paper, Scissors")
user_choice = input("What is your move? (rock, paper,scissors): ")

if user_choice == "paper" :
    print("You picked: " + user_choice)
elif user_choice == "scissors" :
    print("You picked: " + user_choice)
else :
    print("You picked: " + user_choice)

computer_picked = random.choice(["rock","paper","scissors"])
print("The computer picked: " + computer_picked)

if computer_picked == "rock" :
    if user_choice == "paper" :
        print("You Loose")
    elif user_choice == "scissors" :
        print("You Loose")
    else :
        print("Draw")
elif computer_picked == "paper" :
    if user_choice == "rock" :
        print ("You Win")
    elif user_choice == "scissors" :
        print("You Win")
    else :
        print("Draw")
else :
    if user_choice == "rock" :
        print("You Win")
    elif user_choice == "paper" :
        print("You Loose")
    else :
        print("Draw")
