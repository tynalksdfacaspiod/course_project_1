from PySide6.QtWidgets import (
    QHBoxLayout, QVBoxLayout, QFrame,
    QListWidget, QListWidgetItem,
    QPushButton
)
from frontend.widgets.chess_board import ChessBoard


class MainLayout(QHBoxLayout):
    def __init__(self, parent_window=None):
        super().__init__()
        self.parent_window = parent_window

        self.chess_board = ChessBoard(self.parent_window.board_config, clickable_enabled=False)
        self.list_widget = QListWidget()

        self.chess_board.setFrameShape(QFrame.Shape.StyledPanel)
        self.list_widget.setFrameShape(QFrame.Shape.StyledPanel)
        self.list_widget.itemClicked.connect(lambda item: self.parent_window.render_board(item))

        self.addWidget(self.chess_board, 2)
        self.addWidget(self.list_widget, 1)

        self.setSpacing(0)
        self.setContentsMargins(0,0,0,0)



class RenderWindowLayout(QVBoxLayout):
    def __init__(self, parent_window=None):
        super().__init__()
        self.parent_window = parent_window

        layout = MainLayout(self.parent_window)
        self.parent_window.list_widget = layout.list_widget
        self.parent_window.board = layout.chess_board

        self.save_button = QPushButton("Save data")
        self.save_button.setEnabled(False)
        self.parent_window.save_button = self.save_button
        
        self.addLayout(layout)
        self.addWidget(self.save_button)
