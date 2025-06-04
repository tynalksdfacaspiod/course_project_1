from PySide6.QtWidgets import (
    QHBoxLayout, QVBoxLayout, QFrame,
    QListWidget, QListWidgetItem,
    QPushButton
)
from frontend.widgets.chess_board import ChessBoard
from frontend.controllers.render_window.button_controller import SaveButtonController, CloseButtonController

class MainLayout(QHBoxLayout):
    def __init__(self, parent_window=None):
        super().__init__()
        self.parent_window = parent_window

        self.chess_board = ChessBoard(self.parent_window.board_config, clickable_enabled=False)
        self.list_widget = QListWidget()

        self.chess_board.setFrameShape(QFrame.Shape.StyledPanel)
        self.list_widget.setFrameShape(QFrame.Shape.StyledPanel)
        self.list_widget.itemClicked.connect(lambda item: self.parent_window.render_board(item))

        self.parent_window.list_widget = self.list_widget
        self.parent_window.board = self.chess_board

        self.addWidget(self.chess_board, 2)
        self.addWidget(self.list_widget, 1)

        self.setSpacing(0)
        self.setContentsMargins(0,0,0,0)


class ButtonsLayout(QHBoxLayout):
    def __init__(self, parent_window=None):
        super().__init__()
        self.parent_window = parent_window

        self.save_button = QPushButton("Сохранить результат")
        self.save_button.setEnabled(False)
        self.save_button_controller = SaveButtonController(self.parent_window)
        self.save_button_controller.connect_to_button(self.save_button)

        self.parent_window.save_button = self.save_button

        self.close_button = QPushButton("Закрыть окно")
        self.close_button_controller = CloseButtonController(self.parent_window)
        self.close_button_controller.connect_to_button(self.close_button)

        self.addWidget(self.save_button)
        self.addWidget(self.close_button)

class RenderWindowLayout(QVBoxLayout):
    def __init__(self, parent_window=None):
        super().__init__()
        self.parent_window = parent_window

        self.addLayout(MainLayout(self.parent_window))
        self.addLayout(ButtonsLayout(self.parent_window))
