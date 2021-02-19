from random import randint
from os import system
from art import logo, vs
from game_data import data

clear = lambda: system('clear')

def get_guess(a, b):
    print(f"Compare A: {a['name']}, a {a['description']} from {a['country']}.")
    print(vs)
    print(f"Against B: {b['name']}, a {b['description']} from {b['country']}.")
    return input("Who has more followers? Type 'A' or 'B': ").upper()

def get_highest_followers(a, b):
    if a['follower_count'] > b['follower_count']:
        return "A"
    else:
        return "B"

def play_round(a, b, correct_answer):
    clear()
    print(logo)
    
    guess = get_guess(a, b)
    return guess == correct_answer

def game():
    score = 0
    game_over = False
    a_index = randint(0, len(data) - 1)
    while not game_over:
        b_index = a_index
        while b_index == a_index:
            b_index = randint(0, len(data) - 1)
        answer = get_highest_followers(data[a_index], data[b_index])
        guessed_correctly = play_round(data[a_index], data[b_index], answer)
        if guessed_correctly:
            score += 1
            if answer == 'B':
                a_index = b_index
        else:
            game_over = True
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")

game()

