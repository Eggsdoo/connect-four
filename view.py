class View:
    def __init__(self):
        pass

    def display_board(self, board):
        print("\nConnect Four")
        for row in board:
            print("| " + " | ".join(map(lambda x: "X" if x == 1 else "O" if x == 2 else " ", row)) + " |")
        print("+---+---+---+---+---+---+---+")
        print("  1   2   3   4   5   6   7  ")

    def get_player_move(self, player):
        while True:
            try:
                col = int(input(f"Player {player}, enter a column (1-7): ")) - 1
                if 0 <= col < 7:
                    return col
                else:
                    print("Invalid column. Please choose a column from 1 to 7.")
            except ValueError:
                print("Invalid input. Please enter a valid column number.")

    def display_message(self, message):
        print(message)
