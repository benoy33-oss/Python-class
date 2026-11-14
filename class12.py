secret = 36
hearts = 5
count = 0
print("Guess a number between 1 to 50")
while count < hearts:
    guess = (int(input("Enter your guess: ")))
    guess != secret
    count += 1
    if guess >= 46 and guess <= 50 or guess <= 20 and guess >= 1:
       print("You are not that far. try again, Ice cold")
    elif guess >= 43 and guess <= 45 or guess <= 25:
        print("You are close. try again, Cold")
    elif guess >= 40 or guess <= 30:
        print("You are really close try again, Warm")
    elif guess >= 37 or guess <= 35:
        print("You are right next to it, Hot")
    if guess == 36:
        print("You guessed the number!!!, Well Done")
        break
    if hearts == 0:
        print("You have no more chances, the number was: ", secret)
    if guess != secret:
        hearts - 1
    remaning = hearts - count