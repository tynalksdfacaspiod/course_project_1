from PySide6.QtWidgets import QDialog

from frontend.layouts.arrange_window_layouts import ArrangeWindowLayout
from frontend.widgets.chess_board import ChessBoard
from backend.other.file import (
    cleanup,
    write_board_file, read_board_file, is_board_config_exists
)



class ArrangeWindow(QDialog):
    def __init__(self, board_config):
        super().__init__()
        self.board_config = board_config 

        if self._is_board_exists():
            self.board_config = self._get_board_config()

        self.board = ChessBoard(self.board_config, clickable_enabled=True)
        
        self.setWindowTitle("Окно расстановки фигур")
        self.setFixedSize(1000, 700)
        self.setLayout(ArrangeWindowLayout(parent_window=self))

    
    def _get_board_config(self):
        return read_board_file()


    def _is_board_exists(self):
        return is_board_config_exists()


    def accept(self):
        self.board.save_princesses_count()

        params = self.board.get_params()
        princesses_coords = self.board.get_princesses_coords()
        moves_coords = self.board.get_moves_coords()
        free_squares_coords = self.board.get_free_squares_coords()

        write_board_file(params, princesses_coords, moves_coords, free_squares_coords)

        super().accept()


    def reject(self):
        super().reject()
