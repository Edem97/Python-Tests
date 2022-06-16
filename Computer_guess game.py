#Computer Guesses Your Secret Number Game
import random
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
                guess = low # could also be high
        feedback = input('Is {} too high(H), too low(L), or correct(c):'.format(guess))
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print('Yay, The computer guessed your number {} correctly'.format(guess))
    #Try with a high bound of 100
computer_guess(100)
