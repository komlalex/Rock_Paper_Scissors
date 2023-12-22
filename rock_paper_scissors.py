import random 

options = ["rock", "paper", "scissors"]

user_points = 0
computer_points = 0

while True:
    user_input = input("Choose rock, paper or scissors or exit: ")
    computer_input = random.choice(options)
    if user_input == "exit":
        break
    
    if user_input == "rock":
        if computer_input == "rock":
            print("Your input is rock")
            print("Computer input is rock")
            print("It's a tie")
        elif computer_input == "paper":
            computer_points += 1
            print("Your input is rock")
            print("Computer input is paper")
            print("Computer wins")
        elif  computer_input == "scissors":
            user_points += 1
            print("Your input is rock")
            print("Computer input is scissors")
            print("You win")
    elif user_input == "paper":
        if computer_input == "rock":
            user_points += 1
            print("Your input is paper")
            print("Computer input is rock")
            print("You win")
        elif computer_input == "paper":
            print("Your input is paper")
            print("Computer input is paper")
            print("It's a tie")
        elif  computer_input == "scissors":
            computer_points += 1
            print("Your input is paper")
            print("Computer input is scissors")
            print("Computer wins")
    elif user_input == "scissors":
        if computer_input == "rock":
            computer_points += 1
            print("Your input is scissors")
            print("Computer input is rock")
            print("Computer wins")
        elif computer_input == "paper":
            user_points += 1
            print("Your input is scissors")
            print("Computer input is paper")
            print("You win")
        elif  computer_input == "scissors":
            print("Your input is scissros")
            print("Computer input is scissors")
            print("It's a tie")
        
        elif user_input != "rock" or user_input != "paper" or user_input == "scissors":
            print("Invalid input")


print(f"You {user_points} : {computer_points} Computer")