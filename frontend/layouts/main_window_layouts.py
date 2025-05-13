from PySide6.QtWidgets import (
    QFormLayout, QHBoxLayout, QVBoxLayout,
    QPushButton
)
from widgets.line_edit import IntLineEdit
from controllers.button_controller import ExitButtonController
from controllers.line_edit_controller import IntLineEditController


class LineEditLayout(QFormLayout):
    def __init__(self):
        super().__init__()

        n_line_edit = IntLineEdit()
        self.n_line_edit_controller = IntLineEditController()
        self.n_line_edit_controller.connect_to_line_edit(n_line_edit)
        k_line_edit = IntLineEdit()
        self.k_line_edit_controller = IntLineEditController()
        self.k_line_edit_controller.connect_to_line_edit(k_line_edit)

        self.addRow("Введите размер доски N:", n_line_edit)
        self.addRow("Введите кол-во фигур, которые нужно расставить L:", k_line_edit)



class ButtonLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()

        exit_button = QPushButton("Выйти")
        self.exit_controller = ExitButtonController()
        self.exit_controller.connect_to_button(exit_button)
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
