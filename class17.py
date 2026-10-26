"""import random #importing module
playing = True #initalise
number = str(random.randint(0,9)) # random in_built function
print("I will generate a number between 0 to 9, and you have to guess the number one digit a time")
print("The game ends when you get 1 hero!")
#iterate loop till the condition is true
while playing:
    guess = input("Give me your best guess! \n")
    if number == guess:
        print("You win the game")
        print("The number was", number)
        break
    else:
        print("Your guess isn't quite right, try again. ")"""

import random # importing random module
while True: #iterate loop
    user_action = input("Enter a choice (rock , paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    #using random function
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper cover rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cut paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    play_again = input("Play again? (y/n): ")
    if play_again != "y":
        break