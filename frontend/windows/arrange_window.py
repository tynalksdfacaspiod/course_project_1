from PySide6.QtWidgets import QDialog

from frontend.layouts.arrange_window_layouts import ArrangeWindowLayout
from frontend.widgets.chess_board import ChessBoard
from backend.other.file import (
    cleanup,
    write_input_file, read_input_file,
    write_board_file, read_board_file, is_board_file_exists
)



class ArrangeWindow(QDialog):
    def __init__(self, values):
        super().__init__()
        self.values = values

        if self._is_board_exists() and self.values == self._get_cached_values():
            self.board_config = self._get_board_config()
            self.board = ChessBoard(self.values, self.board_config, clickable_enabled=True)
        else:
            cleanup()
            self.board = ChessBoard(self.values, clickable_enabled=True)
        
        self.setWindowTitle("Окно расстановки фигур")
        self.setFixedSize(1000, 700)
        self.setLayout(ArrangeWindowLayout(parent_window=self))

    
    def _is_board_exists(self):
        return is_board_file_exists()


    def _get_board_config(self):
        return read_board_file()


    def _get_cached_values(self):
        return read_input_file()


    def accept(self):
        self.board.save_princesses_count()

        moves_coords = self.board.get_moves_coords()
        princesses_coords = self.board.get_princesses_coords()

        write_input_file(self.board.values)
        write_board_file(princesses_coords, moves_coords)

        super().accept()


    def reject(self):
        super().reject()
