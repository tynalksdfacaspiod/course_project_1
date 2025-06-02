from PySide6.QtWidgets import (
    QHBoxLayout, QVBoxLayout,
    QPushButton
)

from PySide6.QtCore import Qt

from frontend.widgets.chess_board import ChessBoard
from frontend.controllers.arrange_window.button_controller import ConfirmButtonController, CloseButtonController


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

        self.chess_board = ChessBoard(self.parent_window.n)
        self.addWidget(self.chess_board, 0, Qt.AlignCenter)
        self.addLayout(ButtonsLayout(parent_window))
