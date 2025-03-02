# Hangman Game in Python

## Overview

This is a simple Hangman game implemented in Python. The program selects a random word from a predefined list and allows the user to guess letters one by one. The user has 6 lives, and an incorrect guess reduces their lives by 1. The game continues until either the user guesses the word correctly or they run out of lives.

## How the Code Works

### Importing Required Modules

```
import random  # Used to randomly select a word from the list
from words import words  # Import a predefined list of words from an external file
import string  # Provides access to uppercase alphabet letters
```

1. `random.choice(words)`: Picks a random word from the list.
2. `string.ascii_uppercase`: Provides all uppercase letters (A-Z) for validation.

### Function: `select_words(words)`

```
def select_words(words):
    word = random.choice(words)  # Selects a random word from the list
    while '-' in word or ' ' in word:  # Ensures the word doesn't contain spaces or hyphens
        word = random.choice(words)
    return word.upper()  # Converts the word to uppercase for uniformity
```

**Purpose:** This function selects a word for the game while ensuring it does not contain spaces or hyphens.

### Function: `hangman()`

```
def hangman():
    word = select_words(words)  # Selects a word for the game
    word_letters = set(word)  # Stores unique letters in the word
    alphabet = set(string.ascii_uppercase)  # Set of uppercase letters A-Z
    used_letters = set()  # Stores letters guessed by the user
    word_list = ['-' for _ in word]  # Initializes the word display with dashes
```

1. `word_letters`: A set of letters in the word to track progress.
2. `alphabet`: A set containing all uppercase letters.
3. `used_letters`: Keeps track of letters the user has guessed.
4. `word_list`: Stores the word as `-` initially and updates as the user guesses correctly.

### Display Initial State

```
 print(f"Word to guess: {' '.join(word_list)}")  # Displays the initial word with dashes
```

`'.join(word_list)'`: Joins elements of the list with spaces for a neat display.

### Main Game Loop

```
lives = 6  # User starts with 6 lives
    while '-' in word_list and lives > 0:  # Loop until the word is guessed or lives are exhausted
```

1. The loop runs as long as there are dashes (`-`), meaning the word is not fully guessed.
2. The game stops when the user runs out of lives.

#### Displaying Game Status

```
print(f"Word to guess: {' '.join(word_list)}")  # Displays the initial word with dashes
```

`'.join(word_list)'`: Joins elements of the list with spaces for a neat display.

#### Taking User Input

```
  user_letter = input('Guess a letter: ').upper()
```

Converts user input to uppercase to match the word format.

#### Checking User Input

```
 if user_letter in alphabet - used_letters:  # If it's a valid new guess
            used_letters.add(user_letter)  # Add to guessed letters
            if user_letter in word_letters:
                word_letters.remove(user_letter)  # Remove from remaining letters to guess
```

1. Ensures the guessed letter is valid and has not been used before.
2. If correct, the letter is removed from `word_letters`.

#### Updating the Word Display

```
 for i, letter in enumerate(word):  # Enumerate returns index and letter
                    if letter == user_letter:
                        word_list[i] = user_letter  # Replace dashes with correct letter
```

**Purpose of **``: It provides the index (`i`) and the letter (`letter`) so we can update the correct position in `word_list`.

#### Reducing Lives on Wrong Guess

```
else:
                lives -= 1  # Deduct a life for an incorrect guess
                print("Letter is not in the word, you've lost a life!")
```

Only reduces lives **once** per incorrect guess, not per letter in the word.

#### Handling Repeated or Invalid Inputs

```
elif user_letter in used_letters:
            print("You've already used that letter, please try again.")
        else:
            print("Invalid character. Please enter a valid letter.")
```

Prevents repeated guesses and invalid inputs.
### Game End Conditions

```
    if lives == 0:
        print(f"\nYou lost! The word was: {word}")
    else:
        print(f"\nCongratulations! You guessed the word: {word}")
        
```

1. If `lives == 0`, the user loses and the word is revealed.
2. If the user guesses all letters, they win.

### Running the Game

```
hangman()
```

## Summary of Key Features

1. Selects a random word from a list while ensuring no spaces or hyphens.
2. Allows user to guess letters and updates the word display.
3. Tracks guessed letters and prevents repeated guesses.
4. Deducts 1 life per incorrect guess.
5. Ends when the word is guessed or when the user runs out of lives.

## How to Run the Game

```
1. Clone the repository: git clone https://github.com/yourusername/hangman-game.git
2. Navigate to the Project Directory: cd hangman-game
3. Run the Script: python hangman.py
```

**Author:** Sohaib Sharih
**Linkedin:** https://www.linkedin.com/in/sohaib-sharih-a105303b/
**Website:** https://www.codeinterpret.com
Enjoy playing Hangman! 🎉