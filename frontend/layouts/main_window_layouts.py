from PySide6.QtWidgets import (
    QFormLayout, QHBoxLayout, QVBoxLayout,
    QPushButton
)
from widgets.line_edit import IntLineEdit


class LineEditLayout(QFormLayout):
    def __init__(self):
        super().__init__()

        lineEdit_for_n = IntLineEdit()
        lineEdit_for_k = IntLineEdit()

        self.addRow("Введите размер доски N:", lineEdit_for_n)
        self.addRow("Введите кол-во фигур, которые нужно расставить L:", lineEdit_for_k)



class ButtonLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()

        exit_button = QPushButton("Выйти")
        arrange_button = QPushButton("Расставить фигуры")
        render_button = QPushButton("Отрисовать доску")

        self.addWidget(exit_button)
        self.addWidget(arrange_button)
        self.addWidget(render_button)



class MainLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()

        self.addLayout(LineEditLayout())
        self.addLayout(ButtonLayout())
