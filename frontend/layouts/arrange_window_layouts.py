from PySide6.QtWidgets import (
    QHBoxLayout, QVBoxLayout,
    QPushButton
)

from widgets.chess_board import ChessBoard


class ButtonsLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()

        confirm_button = QPushButton("Подтвердить")
        close_button = QPushButton("Закрыть окно")

        self.addWidget(confirm_button)
        self.addWidget(close_button)


class ArrangeWindowLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()

        self.chess_board = ChessBoard()
        self.addWidget(self.chess_board)
        self.addLayout(ButtonsLayout())
