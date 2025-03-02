"""
1. Develop a program where your program has to guess a number you pick.

"""
import random


def guessA(x):
    low = 1
    high = x
    fb = ''
    while fb != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        fb = input(f"Computer's guess is: {guess} Enter H for High, Eneter L for Low, or C for CORRECT: ").lower()
        
        if fb == 'h':
            high = guess - 1
        elif fb == 'l':
            low = guess + 1
    

    print(f"Great! You've guessed it right, its {guess}")
guessA(10)

