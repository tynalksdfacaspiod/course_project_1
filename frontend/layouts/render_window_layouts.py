from PySide6.QtWidgets import (
    QHBoxLayout, QVBoxLayout, QFrame,
    QListWidget, QListWidgetItem,
    QPushButton
)



class MainLayout(QHBoxLayout):
    def __init__(self, parent_window=None):
        super().__init__()
        self.parent_window = parent_window

        self.chess_board = self.parent_window.board
        self.list_widget = QListWidget()

        self.chess_board.setFrameShape(QFrame.Shape.StyledPanel)
        self.list_widget.setFrameShape(QFrame.Shape.StyledPanel)

        self.addWidget(self.chess_board, 2)
        self.addWidget(self.list_widget, 1)

        self.setSpacing(0)
        self.setContentsMargins(0,0,0,0)



class RenderWindowLayout(QVBoxLayout):
    def __init__(self, parent_window=None):
        super().__init__()
        self.parent_window = parent_window

        self.addLayout(MainLayout(self.parent_window))
        self.addWidget(QPushButton("Save data"))
