secret = 36
hearts = 5
print("Guess a number between 1 to 50")
guess = print(int(input("Enter your guess: ")))



if guess >= 46 or guess <= 20:
    print("You are not that far. try again, Ice cold", hearts - 1)
elif guess >= 43 or guess <= 25:
    print("You are close. try again, Cold", hearts - 1)
elif guess >= 40 or guess <= 30:
    print("You are really close try again, Warm", hearts - 1)
elif guess >= 37 or guess <= 35:
     print("You are right next to it, Hot", hearts - 1)

if guess == 36:
    print("You guessed the number!!!, Well Done")

if hearts == 0:
    print("You have no more chances, the number was: ", secret)
