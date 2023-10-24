from board import Board
from view import View

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.current_player = 1

    def play_game(self):
        while True:
            self.view.display_board(self.model.board)
            move = self.view.get_player_move(self.current_player)

            if self.model.is_valid_move(move):
                self.model.place_piece(move, self.current_player)

                if self.model.check_win(self.current_player):
                    self.view.display_board(self.model.board)
                    self.view.display_message(f"Player {self.current_player} wins!")
                    if self.play_again():
                        self.model = Board()
                        self.current_player = 1
                    else:
                        break
                elif self.model.check_draw():
                    self.view.display_board(self.model.board)
                    self.view.display_message("The game ends in a draw!")
                    if self.play_again():
                        self.model = Board()
                        self.current_player = 1
                    else:
                        break

                self.current_player = 3 - self.current_player  # Switch players (1 <-> 2)
            else:
                self.view.display_message("Invalid move. Try again.")

    def play_again(self):
        while True:
            play_again = input("Play again? (yes/no): ").strip().lower()
            if play_again == "yes":
                return True
            elif play_again == "no":
                return False
            else:
                print("Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    board = Board()
    view = View()
    controller = Controller(board, view)
    controller.play_game()
