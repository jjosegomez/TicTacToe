# TicTacToe.

def game():
    ticTacToe = {
        0: " ",1: " ",2: " ",
        3: " ",4: " ",5: " ",
        6: " ",7: " ",8: " ",
    }

    turns = 0
    print_board(ticTacToe)
    for i in range(9):
        if (turns % 2 == 0):
            print("player 1 (X) it is your turn")
            play = int(input("insert a number from 0 to 8: "))
            while(True):
                if(ticTacToe[play] == "X" or ticTacToe[play] == "O"):
                    print("ALERT: this is already taken try another position")
                    play = int(input("insert a number from 0 to 8: "))
                else:
                    ticTacToe[play] = "X"
                    break

        else:    
            print("player 2 (O) it is your turn")
            play = int(input("insert a number from 0 to 8: "))
            while(True):
                if(ticTacToe[play] == "X" or ticTacToe[play] == "O"):
                    print(" ALERT: this is already taken try another position")
                    play = int(input("insert a number from 0 to 8: "))
                else:
                    ticTacToe[play] = "O"
                    break
        
        print_board(ticTacToe)

        turns += 1

        if(check_winner(ticTacToe)):
            break

    if not check_winner(ticTacToe):
        print("is a draw :)")
        
    else:
        if ((turns -1) % 2 == 0):
            print("player 1 (X) has won!!")

        else:
            print("player 2 (O) has won!!")

    print("game is over thank you for playing\n")


def print_board(board):
    print("\n\t ",board[0],"|",board[1],"|",board[2])
    print("\t-------------")
    print("\t ",board[3],"|",board[4],"|",board[5])
    print("\t-------------")
    print("\t ",board[6],"|",board[7],"|",board[8],"\n\n")


def check_winner(board):
    # Winning combinations
    combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                    (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                    (0, 4, 8), (2, 4, 6)]
    for combination in combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] and board[combination[0]] != ' ':
            return True
    return False


game()