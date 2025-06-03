from PySide6.QtWidgets import QDialog

from frontend.layouts.render_window_layouts import RenderWindowLayout
from frontend.widgets.chess_board import ChessBoard
from backend.other.file import (
    read_input_file,
    read_board_file, is_board_file_exists
)

class RenderWindow(QDialog):
    def __init__(self, values):
        super().__init__()
        
        self.values = values
        self._init_board()

        self.setWindowTitle("Окно отрисовки результатов")
        self.setFixedSize(1000,700)
        self.setLayout(RenderWindowLayout(self))

    
    def _init_board(self):
        if self._is_board_exists():
            self.board_config = self._get_board_config()
            self.board = ChessBoard(self.values, self.board_config, clickable_enabled=False)
        else:
            self.board = ChessBoard(self.values, clickable_enabled=False)



    def _is_board_exists(self):
        return is_board_file_exists()


    def _get_board_config(self):
        return read_board_file()


    def _get_input_data(self):
        return read_input_file()

    def accept(self):
        pass
