from PySide6.QtWidgets import QDialog

from frontend.layouts.render_window_layouts import RenderWindowLayout
from frontend.widgets.chess_board import ChessBoard
from backend.other.file import (
    read_board_file, is_board_config_exists
)

class RenderWindow(QDialog):
    def __init__(self, board_config):
        super().__init__()
        
        self.board_config = board_config 

        if is_board_config_exists():
            self.board_config =  self._get_board_config()


        self.board = ChessBoard(self.board_config, clickable_enabled=False)


        self.setWindowTitle("Окно отрисовки результатов")
        self.setFixedSize(1000,700)
        self.setLayout(RenderWindowLayout(self))

    
    def _get_board_config(self):
        return read_board_file()


    def _get_input_data(self):
        return read_input_file()


    def accept(self):
        pass
