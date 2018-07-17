import random

def display_board(board):    #Making the Board
    print('\n'*100)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])

def player_input():           #Taking the player's input
    marker = ''
    while marker !='X' and marker != 'O':
        marker = input('Hey Player 1!, please choose between "X" or "O": ').upper()
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1,player2)

def place_holder(board,marker,pos):        #Placing marker at proper position
    board[pos] = marker
    
def win_checking(board,marker):                 #Winning Logic
    return ((board[1] == marker and board[2] == marker and board[3] == marker) or 
            (board[4] == marker and board[5] == marker and board[6] == marker) or
            (board[7] == marker and board[8] == marker and board[9] == marker) or
            (board[1] == marker and board[4] == marker and board[7] == marker) or
            (board[2] == marker and board[5] == marker and board[8] == marker) or
            (board[3] == marker and board[6] == marker and board[9] == marker) or
            (board[7] == marker and board[5] == marker and board[3] == marker) or
            (board[1] == marker and board[5] == marker and board[9] == marker))
    
def choose_first():                      #Choosing the 1st player to start the game
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def board_blankcheck(board,pos):               #Checking blank space
    if board[pos] == ' ':
        return True

def board_fullcheck(board):                    #Checking board is full or not
    for i in range(1,10):
        if board_blankcheck(board,i):
            return False
    return True

def position_choice(board):         #Taking position from player
    pos = 0
    while pos not in [1,2,3,4,5,6,7,8,9] or not board_blankcheck(board,pos):
        pos = int(input('Choose your next position: (1-9):'))
    return pos

def replay():                        #For again playing
    rep = input('Do you want to play again? Enter Y or N: ').lower()
    if rep == 'y':
        return True

#Main Part
print('Welcome to Tic Tac Toe!')
while True:
    main_board = [' '] * 10
    player1_input,player2_input = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    start_game = input('Are you ready to play? Enter Y or N: ').lower()
    if start_game == 'y':
        game = True
    else:
        game = False
    while game:
        if turn == 'Player 1':
            display_board(main_board)
            position = position_choice(main_board)
            place_holder(main_board,player1_input,position)
            if win_checking(main_board,player1_input):
                display_board(main_board)
                print('Congratulations! Player 1 have won the game!')
                game = False
            else:
                if board_fullcheck(main_board):
                    display_board(main_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
            display_board(main_board)
            position = position_choice(main_board)
            place_holder(main_board,player2_input,position)
            if win_checking(main_board,player2_input):
                display_board(main_board)
                print('Congratulations! Player 2 have won the game!')
                game = False
            else:
                if board_fullcheck(main_board):
                    display_board(main_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break