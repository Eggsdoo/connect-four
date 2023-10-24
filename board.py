class Board:
    def __init__(self, rows=6, cols=7):
        self.rows = rows
        self.cols = cols
        self.board = [[0] * cols for _ in range(rows)]

    def place_piece(self, col, player):
        for row in range(self.rows - 1, -1, -1):
            if self.board[row][col] == 0:
                self.board[row][col] = player
                return

    def is_valid_move(self, col):
        return 0 <= col < self.cols and self.board[0][col] == 0

    def check_win(self):
        pass
        # Implement code to check for a win horizontally, vertically, and diagonally

    def check_draw(self):
    # Check if all columns are full
        return all(self.board[0][col] != 0 for col in range(self.cols))

    def print_board(self):
        for row in self.board:
            print(" ".join(map(str, row)))
    
    def check_win(self, player):
        for row in range(self.rows):
            for col in range(self.cols):
                # Check horizontally
                if col + 3 < self.cols and all(self.board[row][col + i] == player for i in range(4)):
                    return True

                # Check vertically
                if row + 3 < self.rows and all(self.board[row + i][col] == player for i in range(4)):
                    return True

                # Check diagonally (from top-left to bottom-right)
                if col + 3 < self.cols and row + 3 < self.rows and all(self.board[row + i][col + i] == player for i in range(4)):
                    return True

                # Check diagonally (from top-right to bottom-left)
                if col - 3 >= 0 and row + 3 < self.rows and all(self.board[row + i][col - i] == player for i in range(4)):
                    return True

        return False

