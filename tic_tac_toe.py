print("Welcome to the Tic Tac Toe Game")
space_1 = 1 
space_2 = 2
space_3 = 3
space_4 = 4
space_5 = 5
space_6 = 6
space_7 = 7
space_8 = 8
space_9 = 9
player_turn = "x"

def view_board():
    print(f"{space_1} | {space_2} | {space_3}")
    print("-+-+-+-+-+")
    print(f"{space_4} | {space_5} | {space_6}")
    print("-+-+-+-+-+")
    print(f"{space_7} | {space_8} | {space_9}")


def main():
    view_board()
    print(f"{player_turn}'s turn to choose a square (1-9)")




if __name__ == "__main__":
    main()

