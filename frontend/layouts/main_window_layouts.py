from PySide6.QtWidgets import (
    QFormLayout, QHBoxLayout, QVBoxLayout,
    QPushButton
)
from PySide6.QtCore import QTimer

from widgets.line_edit import IntLineEdit
from controllers.button_controller import ExitButtonController, ArrangeButtonController
from controllers.line_edit_controller import IntLineEditController
from windows.arrange_window import ArrangeWindow


class LineEditLayout(QFormLayout):
    def __init__(self):
        super().__init__()
        self.line_edits = {
            "n_line_edit": None,
            "k_line_edit": None
        }

        n_line_edit = IntLineEdit()
        self.n_line_edit_controller = IntLineEditController()
        self.n_line_edit_controller.connect_to_line_edit(n_line_edit)
        self.line_edits["n_line_edit"] = n_line_edit

        k_line_edit = IntLineEdit()
        self.k_line_edit_controller = IntLineEditController()
        self.k_line_edit_controller.connect_to_line_edit(k_line_edit)
        self.line_edits["k_line_edit"] = k_line_edit

        self.addRow("Введите размер доски N:", n_line_edit)
        self.addRow("Введите кол-во фигур, которые нужно расставить L:", k_line_edit)



class ButtonLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()
        self.buttons = {
            "arrange_button": None,
            "render_button": None
        }

        exit_button = QPushButton("Выйти")
        self.exit_button_controller = ExitButtonController()
        self.exit_button_controller.connect_to_button(exit_button)

        arrange_button = QPushButton("Расставить фигуры")
        arrange_button.setEnabled(False)
        self.arrange_button_controller = ArrangeButtonController(arrange_window=ArrangeWindow())
        self.arrange_button_controller.connect_to_button(arrange_button)
        self.buttons["arrange_button"] = arrange_button

        render_button = QPushButton("Отрисовать доску")
        render_button.setEnabled(False)
        self.buttons["render_button"] = render_button

        self.addWidget(exit_button)
        self.addWidget(arrange_button)
        self.addWidget(render_button)



class MainLayout(QVBoxLayout):
    def __init__(self, parent_window=None):
        super().__init__()
        self.parent_window = parent_window

        self.line_edit_layout = LineEditLayout()
        self.button_layout = ButtonLayout()
        
        self.addLayout(self.line_edit_layout)
        self.addLayout(self.button_layout)

        self.timer = QTimer(self) 
        self.timer.timeout.connect(self._toggle_buttons)
        self.timer.timeout.connect(self._set_values)
        self.timer.start(50)

    

    def _toggle_buttons(self):
        value_n = self.parent_window.values["n"]
        value_k = self.parent_window.values["k"]

        arrange_button = self.button_layout.buttons["arrange_button"]
        render_button = self.button_layout.buttons["render_button"]

        if value_n != 0:
            if value_k == 0:
                arrange_button.setEnabled(False)
                render_button.setEnabled(True)
            else:
                arrange_button.setEnabled(True)
                render_button.setEnabled(True)
        else:
            arrange_button.setEnabled(False)
            render_button.setEnabled(False)
    

    def _set_values(self):
        n_line_edit_value = self.line_edit_layout.line_edits["n_line_edit"].text()
        k_line_edit_value = self.line_edit_layout.line_edits["k_line_edit"].text()

        if n_line_edit_value:
            self.parent_window.values["n"] = int(n_line_edit_value)
        else:
            self.parent_window.values["n"] = 0
            

        if k_line_edit_value:
            self.parent_window.values["k"] = int(k_line_edit_value)
        else:
            self.parent_window.values["k"] = 0
