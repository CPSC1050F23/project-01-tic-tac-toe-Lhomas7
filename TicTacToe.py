
"""makes the array into a tictactoe board"""
def board_string(board):
    new_string = ""
    for row in board:
        new_string += "|"
        for col in row:
            if col != "":
                new_string += f" {col} |"
            else:
                new_string += " _ |"
        new_string += "\n"
    return new_string
"""places an input onto the board"""
def place_input(row, column):
    for i in range(3):
        for j in range(3):
            if (i == row and j == column):
                board[i][j] = value
"""checks for a win on the board"""
def check_win(board):
    O_win = False
    X_win = False
    """across win"""
    for i in range(3):
        count = 0
        for j in range(3):
            if board[i][j] == 'O':
                count += 1
            if count == 3:
                O_win = True
        count = 0
        for j in range(3):
            if board[i][j] == 'X':
                count += 1
            if count == 3:
                X_win = True
    """vertical wins"""
    count = 0
    for i in range(3):
        for j in range(3):
            if j == 0 and board[i][j] == 'O':
                count += 1
    if count == 3:
        O_win = True
    count = 0
    for i in range(3):
        for j in range(3):
            if j == 0 and board[i][j] == 'X':
                count += 1
    if count == 3:
        X_win = True
    count = 0
    for i in range(3):
        for j in range(3):
            if j == 1 and board[i][j] == 'O':
                count += 1
    if count == 3:
        O_win = True
    count = 0
    for i in range(3):
        for j in range(3):
            if j == 1 and board[i][j] == 'X':
                count += 1
    if count == 3:
        X_win = True
    count = 0
    for i in range(3):
        for j in range(3):
            if j == 2 and board[i][j] == 'O':
                count += 1
    if count == 3:
        O_win = True
    count = 0
    for i in range(3):
        for j in range(3):
            if j == 2 and board[i][j] == 'X':
                count += 1
    if count == 3:
        X_win = True
    """check diagonal 1"""
    count = 0
    for i in range(3):
        for j in range(3):
            if i == j and board[i][j] == 'O':
                count += 1
    if count == 3:
        O_win = True
    count = 0
    for i in range(3):
        for j in range(3):
            if i == j and board[i][j] == 'X':
                count += 1
    if count == 3:
        X_win = True
    """check diagonal 2"""
    count = 0
    for i in range(3):
        for j in range(3):
            if j == 2 - i and board[i][j] == 'O':
                count += 1
    if count == 3:
        O_win = True
    count = 0
    for i in range(3):
        for j in range(3):
            if j == 2 - i and board[i][j] == 'X':
                count += 1
    if count == 3:
        X_win = True
    if X_win:
        return "Player X wins!"
    elif O_win:
        return "Player O wins!"
    else:
        return "It's a TIE!"


    
"""function that checks if a spot on the board is out of bounds"""
def check_out_of_bounds(row, column):
    out_of_bounds = False
    if (row != 1 and row != 2 and row != 3) or (column != 1 and column != 2 and column != 3):
        out_of_bounds = True
    return out_of_bounds

"""function that checks if a spot on the board is full"""
def check_full(row, column):
    empty = True
    if board[row][column] != '':
        empty = False
    return empty




board = [['','',''],['','',''],['','','']]

"""game intro"""
play = 'y'
while play == 'y':
    print("Let's play Tic-Tac-Toe!\nWhen prompted, enter desired row and column numbers")
    print('Example: 1 3')
    board = [['','','X'],['','',''],['','','']]
    print(board_string(board))
    print("\nLet's play!\nPlayer X starts!")
    board = [['','',''],['','',''],['','','']]
    print(board_string(board))
    """begin gameplay"""
    for i in range(9):
        value = i
        if value % 2 == 0:
            value = 'X'
        else:
            value = 'O'
        print(f"Enter row and column for player {value}")
        position_input = input().split()
        position = []
        """validate that input is a numbered position"""
        for item in position_input:
            try: 
                position.append(int(item))
            except: 
                print("Please enter valid row and col numbers from 1 to 3:")
                position_input = input().split()
                position = []
        """check if the input will be out of bounds"""
        while check_out_of_bounds(position[0],position[1]):
            print("Please enter valid row and col numbers from 1 to 3:")
            position_input = input().split()
            position = []
            for item in position_input:
                try: 
                    position.append(int(item))
                except: 
                    print("Please enter valid row and col numbers from 1 to 3:")
                    position_input = input().split()
                    position = []
        """check if the spot is full and validate new input"""
        while not check_full(position[0] - 1,position[1] - 1):
            print(f"That spot is full!\n\nEnter row and column for player {value}")
            position_input = input().split()
            position = []
            for item in position_input:
                try: 
                    position.append(int(item))
                except: 
                    print("Please enter valid row and col numbers from 1 to 3:")
                    position_input = input().split()
                    position = []
        place_input(position[0] - 1, position[1] - 1)
        print(board_string(board))
        """check for a win or tie"""
        if i != 8 and (check_win(board)) == "It's a TIE!":
            continue
        elif i != 8 and check_win(board) != "It's a TIE!":
            print(check_win(board))
            break
        else:
            print(check_win(board))
            break 
    """ask if user would like to play again"""      
    print("Do you want to play again? Y or N")
    play = input().lower()
    while play != 'y' and play != 'n':
        print('Please enter valid input: Y or N')
        print("Do you want to play again? Y or N")
        play = input().lower()
    if play == 'n':
        break






    
    
    


    

