from PySide6.QtWidgets import QDialog

from frontend.layouts.arrange_window_layouts import ArrangeWindowLayout
from frontend.widgets.chess_board import ChessBoard
from frontend.other.file import write_input_file, read_input_file

class ArrangeWindow(QDialog):
    def __init__(self, values):
        super().__init__()
        self.values = values
        self.board = ChessBoard(self.values)
        
        self.setWindowTitle("Окно расстановки фигур")
        self.setFixedSize(1000, 700)
        self.setLayout(ArrangeWindowLayout(parent_window=self))
        

    def accept(self):
        write_input_file(self.values)
        print("Accepted")
        res = read_input_file() 
        print(res)
        super().accept()


    def reject(self):

        print("Rejected")
        super().reject()
