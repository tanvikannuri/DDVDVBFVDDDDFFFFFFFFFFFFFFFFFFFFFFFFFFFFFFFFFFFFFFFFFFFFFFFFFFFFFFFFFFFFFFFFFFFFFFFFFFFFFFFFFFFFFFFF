#NumberGuessingGame

import random

lives = 3

luckynum = random.randint(1, 10)

print("You have 5 lives.")

while (lives > 0) :
    guessednumber = int(input("Guess the number: \n"))

    if guessednumber==luckynum :
        print("Congratulations!")
        lives=0
    elif guessednumber > luckynum and lives > 1 :
        print("Opps! The guessed number is larger.")
        lives = lives - 1
    elif guessednumber < luckynum and lives > 1 :
        print("Opps! The guessed number is smaller.")
        lives = lives - 1
    else :
        print("You lost!")
        lives = lives - 1