from board import Board
from view import View
from controller import Controller

if __name__ == "__main__":
    board = Board()
    view = View()
    controller = Controller(board, view)
    controller.play_game()