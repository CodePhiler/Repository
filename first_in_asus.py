def print_board(board):
    for i, row in enumerate(board):
        row_str = " "
        for j, value in enumerate(row):
            row_str += value
            if len(row)-1 != j:
                row_str += " | "
        print(row_str)
        if len(board)-1 != i:
            print("-----------")
    print()

def get_move(turn, board):
    while True:
        row=int(input("Row: "))
        col=int(input("Column: "))
        print()
        if row<1 or row>len(board):
            print("Invalid row. Please enter a number between 1 and", len(board))
        elif col<1 or col>len(board[row-1]):
            print("Invalid column. Please enter a number between 1 and", len(board[row]))
        elif board[row-1][col-1] != " ":
            print("Position already occupied. Please choose another position.")
        else:
            break
    board[row-1][col-1]=turn

def check_win(turn, board):
    lines=[
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],
        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)],
        [(0,0), (1,1), (2,2)],
        [(0,2), (1,1), (2,0)]
    ]
    for line in lines:
        win=True
        for pos in line:
            row, col = pos
            if  board[row][col] != turn:
                win=False
                break
        if win:
            return True
    # here when win==True it returns 'True' and the for loop ends here only...
    # Otherwise it doesn't goes if statement and the below "retun False" will return.
    return False

board=[
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

turn="X"
turn_number=0
print_board(board)
while turn_number<9:
    print("It 's", turn,"'s turn")
    get_move(turn, board)
    winner=check_win(turn, board)
    print_board(board)
    if winner:
        break
    # To swap the values
    if turn == "X":
        turn="O"
    else:
        turn="X"
    turn_number+=1
if turn_number==9:
    print("Game tied!! ")
else:
    print("The winner was,", turn)
    