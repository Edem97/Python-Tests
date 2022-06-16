#User guesses Computer's Secret Number

import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input('Guess the number between 1 and {}:'.format(x)))
        if guess < random_number:
            print('sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
        else:
            print('Congrats, you have guessed the right number {}'.format(random_number))
