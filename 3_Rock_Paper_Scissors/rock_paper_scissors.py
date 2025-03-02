import random

def play():
    user = input("Pick one: 'r' for Rock, 's' for Scissors and 'p' for paper")
    computer = random.choice(['r', 's', 'p'])

    if user == computer:
        print("It's a tie!")

    if is_win(user, computer):
        return "You Win!"
    
    return "You Lost!"

def is_win(player, opponent):
    """
    You can only win in the following 3 conditions:
    1. Rock beats Scissors
    2. Scissor beats Paper
    3. Paper beats Rock
    """
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    
print(play())