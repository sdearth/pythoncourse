import random
import os
from . import hangman_art
from . import hangman_words

clear = lambda: os.system('clear')

lives = 6
word = random.choice(hangman_words.word_list)

print(hangman_art.logo)
print(f'Pssst, the solution is {word}.')

display = ['-' for i in range(len(word))]

end_of_game = False
guesses = []
while not end_of_game:
    print(hangman_art.stages[lives])
    print(f"{' '.join(display)}")
    guess = input('Guess a letter: ').lower()
    for idx, letter in enumerate(word):
        if guess == letter:
            display[idx] = guess
            found = True
    if guess in guesses:
        print(f"You've already guessed {guess}")
    else:
        if guess not in word:
            print(f"You guessed {guess}. That's not in the word. You lose a life.")
            lives -= 1

        if lives == 0:
            print('You lose!')
            end_of_game = True
        elif not '-' in display:
            end_of_game = True
            print('You won!')
    guesses.append(guess)