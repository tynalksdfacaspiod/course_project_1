from typing import Optional
from PySide6.QtWidgets import (
    QHBoxLayout, QVBoxLayout, QFrame,
    QPushButton
)

from PySide6.QtCore import Qt

from frontend.widgets.chess_board import ChessBoard
from frontend.controllers.arrange_window.button_controller import ConfirmButtonController, CloseButtonController


class ButtonsLayout(QHBoxLayout):
    """ Layout для кнопок """
    def __init__(self, parent_window: Optional['ArrangeWindow'] = None):
        super().__init__()
        self.parent_window = parent_window

        # Создание кнопки подтверждения расстановки фигур и её привязка к контроллеру
        confirm_button = QPushButton("Подтвердить")
        self.confirm_button_controller = ConfirmButtonController(self.parent_window)
        self.confirm_button_controller.connect_to_button(confirm_button)
        
        # Создание кнопки закрытия окна и её привязка к контроллеру
        close_button = QPushButton("Закрыть окно")
        self.close_button_controller = CloseButtonController(self.parent_window)
        self.close_button_controller.connect_to_button(close_button)

        # Добавление кнопок в Layout
        self.addWidget(confirm_button)
        self.addWidget(close_button)


class ArrangeWindowLayout(QVBoxLayout):
    """ Главный Layout для окна расстановки фигур """
    def __init__(self, parent_window: Optional['ArrangeWindow'] = None):
        super().__init__()
        self.parent_window = parent_window

        # Расположение доски в Layoutе
        self.chess_board = self.parent_window.board
        self.chess_board.setFrameShape(QFrame.Shape.StyledPanel)

        # Добавление доски и кнопок в Layout
        self.addWidget(self.chess_board)
        self.addLayout(ButtonsLayout(parent_window))
