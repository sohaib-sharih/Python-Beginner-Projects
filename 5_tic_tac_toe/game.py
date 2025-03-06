from tictactoe import HumanPlayer, randomComputerPlayer, geniusComputerPlayer
import time

class ticTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # We will use a single list to rep 3x3 board
        self.current_winner = None # keep track of winner!

    def print_board(self):
        #This is just getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + '  |')

    @staticmethod

    def print_board_nums():
        # 0 |1 | 2 etc tells us what number corresponds to what box
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + '  |')


    def available_moves(self):
        return[i for i, spot in enumerate(self.board) if spot == ' ']
        # moves=[]
        # for (i, spot) in enumerate(self.board):
        #     # assign tuples ['x'.'x','o'] --> [(o, x),(1,x), (2, o)]
        #     if spot == ' ':
        #         moves.append(i)
        # return moves

    def empty_squares(self):
        return ' ' in self.board
    
    # to find out the number of empty squares:
    def num_empty_squares(self):
        return self.board.count(' ')
        #this will return the number of spaces on the board

    def make_move(self, square, letter):
        # if valid move, then make the move(assign square to letter)
        # then return ture, if invalid, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # winner if 3 in a row anywhere... we have to check all of these!
        # first lets check the row

        row_ind = square // 3
        row = self.board[row_ind*3: (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        #Check column
        col_ind = square % 3
        column = [self.board[col_ind + i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        #check diagnols
        # but only if the square is an even number(0,2,4,6,8)
        # these are the only moves possible to win a diagnol
        if square % 2 == 0:
            diagnol1 = [self.board[i] for i in [0, 4, 8]] # left to right diagnol
            if all([spot == letter for spot in diagnol1]):
                return True
            diagnol2 = [self.board[i] for i in [2, 4, 6]] # right to left diagnol
            if all([spot == letter for spot in diagnol2]):
                return True
        #if all these checks fail, then we dont have a winner
        return False
    
def play(game, x_player, o_player, print_game = True):
    # returns the winner of the game! or None for a tie
    if print_game:
        game.print_board_nums()

    letter = 'x' # starting letter
    # iterate while the game still has empty squares
    # we dont have to worry about winner because we'll just return that
    # which breaks the loop

    #To check if the game still has empty squares
    while game.empty_squares():
        #get the move from the approprate player
        if letter == 'o':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # lets define a function to make a move!
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print(' ') #Just an empty line

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
            #After we made our move, we need to alternate letters
            letter = 'o' if letter == 'x' else 'x'
            # above line works the same as below line of code snippet
            '''
            if letter == 'x':
                letter = 'o'

            else:
                letter = 'x'
            '''
        # tiny breaks to make things easier to read.
        if print_game:
            time.sleep(0.8)
    if print_game:
        print('its a tie!')

"""
1. The below code is for Human player to play with the Genius computer
2. You can also use the genius player to play with the computer player
"""
# if __name__ == '__main__':
#     x_player = HumanPlayer('x')
#     o_player = geniusComputerPlayer('o')
#     t = ticTacToe()
#     play(t, x_player, o_player, print_game=True)

if __name__ == '__main__':
    x_wins = 0
    o_wins = 0
    ties = 0
    for _ in range(100):
        x_player = randomComputerPlayer('x')
        o_player = geniusComputerPlayer('o')
        t = ticTacToe()
        result = play(t, x_player, o_player, print_game=False)
        if result == 'x':
            x_wins += 1
        elif result == 'o':
            o_wins += 1

        else:
            ties += 1

    print(f"After 100 iterations, we see {x_wins} x_wins, {o_wins} o_wins, {ties} ties")
