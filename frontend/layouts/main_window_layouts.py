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
        self.line_edits = set()

        n_line_edit = IntLineEdit()
        self.n_line_edit_controller = IntLineEditController()
        self.n_line_edit_controller.connect_to_line_edit(n_line_edit)
        self.line_edits.add(n_line_edit)

        k_line_edit = IntLineEdit()
        self.k_line_edit_controller = IntLineEditController()
        self.k_line_edit_controller.connect_to_line_edit(k_line_edit)
        self.line_edits.add(k_line_edit)

        self.addRow("Введите размер доски N:", n_line_edit)
        self.addRow("Введите кол-во фигур, которые нужно расставить L:", k_line_edit)



class ButtonLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()
        self.buttons = set()

        exit_button = QPushButton("Выйти")
        self.exit_button_controller = ExitButtonController()
        self.exit_button_controller.connect_to_button(exit_button)

        arrange_button = QPushButton("Расставить фигуры")
        arrange_button.setEnabled(False)
        self.arrange_button_controller = ArrangeButtonController(arrange_window=ArrangeWindow())
        self.arrange_button_controller.connect_to_button(arrange_button)
        self.buttons.add(arrange_button)

        render_button = QPushButton("Отрисовать доску")
        render_button.setEnabled(False)
        self.buttons.add(render_button)

        self.addWidget(exit_button)
        self.addWidget(arrange_button)
        self.addWidget(render_button)



class MainLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()

        self.line_edit_layout = LineEditLayout()
        self.button_layout = ButtonLayout()
        
        self.addLayout(self.line_edit_layout)
        self.addLayout(self.button_layout)

        self.keys_timer = QTimer(self) 
        self.keys_timer.timeout.connect(self._toggle_buttons)
        self.keys_timer.start(50)

    
    def _toggle_buttons(self):
        for button in self.button_layout.buttons:
            if self._is_line_edits_full():
                button.setEnabled(True)
            else:
                button.setEnabled(False)


    def _is_line_edits_full(self):
        for line_edit in self.line_edit_layout.line_edits:
            if line_edit.is_empty:
                return False
        return True
