import random
from words import words
import string

"""
1. The program should select a random word from the list of words.

"""
# print(words[57])


#------------------------------------------------

import random
from words import words
import string

def select_words(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()  # Convert to uppercase for consistency

def hangman():
    word = select_words(words)
    word_letters = set(word)  # Letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # Letters guessed by the user
    word_list = ['-' for _ in word]  # Initialize word display with dashes

    print(f"Word to guess: {' '.join(word_list)}")  # Initial display

    lives = 6
    while '-' in word_list and lives > 0:  # Keep looping until no '-' left
        print(f"\nYou have {lives} lives left. You've used these letters: ", ' '.join(sorted(used_letters)))
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                # Update the word_list
                for i, letter in enumerate(word):
                    if letter == user_letter:
                        word_list[i] = user_letter  # Replace dashes with correct letter
            else:
                        lives = lives -1 #take away life
                        print("letter is not in a word, you've lost a life!")
        elif user_letter in used_letters:
            print("You've already used that letter, please try again.")
        else:
            print("Invalid character. Please enter a valid letter.")

    print(f"\nCongratulations! The word was: {word}")

hangman()

