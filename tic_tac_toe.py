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

def user_choose_square(player, board): #player_turn
    print(f"It is {player}'s turn to pick a square(1-9)")
    square_choice = int(input("What square will you choose"))

    board[square_choice - 1] = player

def winner(board): 
    return (board[0] == board[1] == board[2] or
           board[0] == board[3] == board[6] or
           board[1] == board[4] == board[7] or
           board[2] == board[5] == board[8] or
           board[3] == board[4] == board[5] or
           board[6] == board[7] == board[8] or
           board[0] == board[4] == board[8] or
           board[2] == board[4] == board[6])

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
        user_choose_square(player, the_board)
        player = next_player(player)
    
    view_board(the_board)
    if (the_board[0] == the_board[1] == the_board[2] or
        the_board[0] == the_board[3] == the_board[6] or
        the_board[1] == the_board[4] == the_board[7] or
        the_board[2] == the_board[5] == the_board[8] or
        the_board[3] == the_board[4] == the_board[5] or
        the_board[6] == the_board[7] == the_board[8] or
        the_board[0] == the_board[4] == the_board[8] or
        the_board[2] == the_board[4] == the_board[6]):
            if player == "x":
                print("O is the winner! Good game!")

            if player == "o":
                print("X is the winner! Good game!")

    elif (the_board[0] and the_board[1] and the_board[2] and 
          the_board[3] and the_board[4] and the_board[5] and 
          the_board[6] and the_board[7] and the_board[8]) == "x" or "o":
        print("The Game has ended a tie!")

if __name__ == "__main__":
    main()

