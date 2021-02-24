import random
import numberArt


print(numberArt.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = random.randint(1, 101)
if input("Choose a difficulty. Type 'easy' or 'hard': ").lower() == 'hard':
    attempts = 5
else:
    attempts = 10

still_attempting = True
while still_attempting:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if attempts > 1:
        if guess > answer:
            print("Too high.\nGuess again")
            attempts -= 1
        elif guess < answer:
            print("Too low.\nGuess again.")
            attempts -= 1
        else:
            print("You guessed it. You win!")
            still_attempting = False
    else:
        print("You have no more attempts left. Game over.")
        still_attempting = False
