from IPython.display import clear_output
import random


def display_board(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print("_____")
    print(board[4] + '|' + board[5] + '|' + board[6])
    print("_____")
    print(board[7] + '|' + board[8] + '|' + board[9])


def player_input():
    player1 = ''
    while player1.upper() not in ['X', 'O']:
        player1 = input("Please pick a marker 'X' or 'O'")

    return player1


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    if mark == board[1] == board[2] == board[3]:
        return True
    elif mark == board[4] == board[5] == board[6]:
        return True
    elif mark == board[7] == board[8] == board[9]:
        return True
    elif mark == board[1] == board[4] == board[7]:
        return True
    elif mark == board[2] == board[5] == board[8]:
        return True
    elif mark == board[3] == board[6] == board[9]:
        return True
    elif mark == board[3] == board[5] == board[7]:
        return True
    elif mark == board[1] == board[5] == board[9]:
        return True
    else:
        return False


def choose_first():
    return random.ranint(1, 2)


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for item in board[1:]:
        if item == ' ':
            return False

    return True


def player_choice(board):
    answer = 0
    while answer not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        answer = int(input("Please enter a board position: "))

    if space_check(board, answer):
        return answer


def replay():
    answer = ''
    while answer.Upper() not in ['Y', 'N']:
        answer = input('Do you wish to play again Y/N')

    return answer.Upper() == 'Y'


print('Welcome to Tic Tac Toe!')

# while True:
# Set the game up here
# pass

# while game_on:
# Player 1 Turn


# Player2's turn.

# pass

# if not replay():
# break


print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    display_board(board)
    # pass
    game_on = True
    while game_on:
    # Player 1 Turn

    # Player2's turn.

    # pass

    if not replay():
        break
