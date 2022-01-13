print("Welcome to the Tic Tac Toe Game")

def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board


def view_board(board):
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("-+-+-+-+-+")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("-+-+-+-+-+")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()



def main():
    the_board = create_board()
    view_board(the_board)
    
    




if __name__ == "__main__":
    main()

