print("Welcome to the Tic Tac Toe Game")
player_turn = "x"

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

def user_choose_square(player_turn, board):
    print(f"It is {player_turn}'s turn to pick a square(1-9)")
    square_choice = int(input("What square will you choose"))

    board[square_choice - 1] = player_turn

def winner(board): 
    return (board[0] == board[1] == board[2] or
           board[0] == board[3] == board[6] or
           board[1] == board[4] == board[7] or
           board[2] == board[5] == board[8] or
           board[3] == board[4] == board[5] or
           board[6] == board[7] == board[8] or
           board[0] == board[4] == board[8] or
           board[2] == board[4] == board[6])

def tie(board):
    print("Its a tie")



def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

           



def main():
    player = next_player("")
    the_board = create_board()

    while not (winner(the_board)):
        view_board(the_board)
        user_choose_square(player_turn, the_board)
        player = next_player(player)
    
    view_board(the_board)
    print("Good Game!")

    
    




if __name__ == "__main__":
    main()

