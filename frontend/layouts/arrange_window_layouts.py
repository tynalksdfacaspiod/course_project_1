from PySide6.QtWidgets import (
    QHBoxLayout, QVBoxLayout,
    QPushButton
)

from widgets.chess_board import ChessBoard
from controllers.button_controller import ConfirmButtonController, CloseButtonController

class ButtonsLayout(QHBoxLayout):
    def __init__(self, parent_window=None):
        super().__init__()
        self.parent_window = parent_window

        confirm_button = QPushButton("Подтвердить")
        self.confirm_button_controller = ConfirmButtonController(self.parent_window)
        self.confirm_button_controller.connect_to_button(confirm_button)
        
        close_button = QPushButton("Закрыть окно")
        self.close_button_controller = CloseButtonController(self.parent_window)
        self.close_button_controller.connect_to_button(close_button)

        self.addWidget(confirm_button)
        self.addWidget(close_button)


class ArrangeWindowLayout(QVBoxLayout):
    def __init__(self, parent_window=None):
        super().__init__()
        self.parent_window = parent_window

        self.chess_board = ChessBoard()
        self.addWidget(self.chess_board)
        self.addLayout(ButtonsLayout(parent_window))
