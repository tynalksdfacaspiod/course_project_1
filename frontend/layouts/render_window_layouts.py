from typing import Optional
from PySide6.QtWidgets import (
    QHBoxLayout, QVBoxLayout, QFrame,
    QListWidget, QListWidgetItem,
    QPushButton
)
from frontend.widgets.chess_board import ChessBoard
from frontend.controllers.render_window.button_controller import SaveButtonController, CloseButtonController



class MainLayout(QHBoxLayout):
    """ Layout для расплоложения доски со списком результатов """
    def __init__(self, parent_window: Optional['RenderWindow'] = None):
        super().__init__()
        self.parent_window = parent_window

        # Создание доски с некликабельными ячейками на основе конфига
        self.chess_board = ChessBoard(self.parent_window.board_config, clickable_enabled=False)

        # Создание виджета-списка
        self.list_widget = QListWidget()

        # Установка возможности растяжения виджетов
        self.chess_board.setFrameShape(QFrame.Shape.StyledPanel)
        self.list_widget.setFrameShape(QFrame.Shape.StyledPanel)

        # Привязка клика на элементы списка к функции рендера доски
        self.list_widget.itemClicked.connect(lambda item: self.parent_window.render_board(item))

        # Добавление ссылок на виджеты в свойства окна
        self.parent_window.list_widget = self.list_widget
        self.parent_window.board = self.chess_board

        # Добавление виджетов в Layout
        self.addWidget(self.chess_board, 2)
        self.addWidget(self.list_widget, 1)

        # Удаление отступов
        self.setSpacing(0)
        self.setContentsMargins(0,0,0,0)



class ButtonsLayout(QHBoxLayout):
    """ Layout кнопок """
    def __init__(self, parent_window: Optional['RenderWindow'] = None):
        super().__init__()
        self.parent_window = parent_window

        # Создание кнопки для сохранения результатов и её привязка к контроллеру
        self.save_button = QPushButton("Сохранить результаты")
        self.save_button.setEnabled(False)
        self.save_button_controller = SaveButtonController(self.parent_window)
        self.save_button_controller.connect_to_button(self.save_button)

        # Создание ссылки на кнопку в свойство окна
        self.parent_window.save_button = self.save_button

        # Создание кнопки для закрытия окна и её привязка к контроллеру
        self.close_button = QPushButton("Закрыть окно")
        self.close_button_controller = CloseButtonController(self.parent_window)
        self.close_button_controller.connect_to_button(self.close_button)

        # Добавление кнопок в Layout
        self.addWidget(self.save_button)
        self.addWidget(self.close_button)



class RenderWindowLayout(QVBoxLayout):
    """ Layout окна отрисовки результатов """
    def __init__(self, parent_window: Optional['RenderWindow'] = None):
        super().__init__()
        self.parent_window = parent_window

        self.addLayout(MainLayout(self.parent_window))
        self.addLayout(ButtonsLayout(self.parent_window))
