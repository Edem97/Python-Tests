#User guessing game

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
        
#Computer guessing game

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
computer_guess(15)

#Rock paper scissors game
def play():
    user = input(" Please enter your choice: 'r' for rock, 'p' for paper. 's's for scissors\n")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'It\'s a tie'
    # r > s, s > p, p > r
    if is_win(user,computer):
        return 'You won!'
    return 'You lost'

def is_win(player, opponent):
    #return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
