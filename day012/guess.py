import random
import art

EASY_TURNS = 10
HARD_TURNS = 5

NUMBER = random.randint(1, 100)

def set_difficulty():
    difficulty = 'None'
    while not (difficulty == 'easy' or difficulty == 'hard'):
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return EASY_TURNS
    else:
        return HARD_TURNS

def check_guess(guess):
    if guess == NUMBER:
        print(f"You got it! The answer was {NUMBER}.")
        return True
    elif guess < NUMBER:
        print("Too low.")
    else:
        print("Too high.")

    return False

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

guesses_left = set_difficulty()
while guesses_left > 0:
    print(f"You have {guesses_left} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    game_over = check_guess(guess)
    if game_over:
        guesses_left = 0
    else:
        guesses_left -= 1
        if guesses_left > 0:
            print("Guess again.")
        else:
            print("You've run out of guesses. You lose!")
