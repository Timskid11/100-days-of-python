#tictactoe

board = [
    [" "," "," ",],
    [" "," "," "],
    [" "," "," "]
         ]


winning_combination = [
    [(0,0),(0,1),(0,2)],
    [(1,0),(1,1),(1,2)],
    [(2,0),(2,1),(2,2)],
    [(0,0),(1,0),(2,0)],
    [(0,1),(1,1),(2,1)],
    [(0,2),(1,2),(2,2)],
    [(0,0),(1,1),(2,2)],
    [(0,2),(1,1),(2,0)],
]

def print_board(board):
    print("\n")
    print("  ", " | ".join(col for col in board[0]))
    print("  ___________")
    print("  ", " | ".join(col for col in board[1]))
    print("  ___________")
    print("  ", " | ".join(col for col in board[2]))
    print('\n')

boxes = {
    "1" : {'row' : 0,
           'column' : 0}
    ,
    "2" : {'row' : 0,
           'column' : 1}
    ,
    "3" : {'row' : 0,
           'column' : 2}
    ,
    "4" : {'row' : 1,
           'column' : 0}
    ,
    "5" : {'row' : 1,
           'column' : 1}
    ,
    "6" : {'row' : 1,
           'column' : 2}
    ,
    "7" : {'row' : 2,
           'column' : 0}
    ,
    "8" : {'row' : 2,
           'column' : 1}
    ,
    "9" : {'row' : 2,
           'column' : 2}

}
def player_input(board,player):
    while True:

        print(f"Player {player} is going to be playing.")
        box = input(f"Player {player}...enter the number(1-9) ")
        if int(box) > 9 or int(box) < 1:
            player_input(board,player)
        elif board[boxes[box]['row']][boxes[box]['column']] != " ":
            print(f"cell already used,try again")
        else:
            col = boxes[box]['column']
            row = boxes[box]['row']
            board[row][col] = player
            break
    return board

def check_board(board):
    list_x = []
    list_y = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == "X":
                list_x.append((row,col))
            elif board[row][col] == "O":
                list_y.append((row,col))
    return list_x,list_y


def run_game(board):
    turn = 0
    while True:
        print_board(board)
        if all(" " not in cells for cells in board):
            print("It's a tie!!")
            break

        Position_x, Position_y = check_board(board)
        if Position_x  in winning_combination:
            print(f'Player \'X\' wins!')
        if Position_y in winning_combination:
            print(f'Player \'Y\' wins!')

        if turn % 2 == 0:
            player = 'X'
        if turn % 2 == 1:
            player = 'O'
        board = player_input(board,player)
        turn += 1

run_game(board)