from typing import Optional
from PySide6.QtWidgets import (
    QFormLayout, QHBoxLayout, QVBoxLayout,
    QPushButton
)
from PySide6.QtCore import QTimer

from frontend.widgets.line_edit import IntLineEdit
from frontend.controllers.main_window.button_controller import ExitButtonController, ArrangeButtonController, RenderButtonController
from frontend.controllers.main_window.line_edit_controller import IntLineEditController
from frontend.windows.arrange_window import ArrangeWindow



class LineEditLayout(QFormLayout):
    """  Layout для LineEdit'ов """
    def __init__(self):
        super().__init__()
        self.line_edits = {
            "n_line_edit": None,
            "l_line_edit": None
        }

        # Создание LineEdit'а для N
        n_line_edit = IntLineEdit()
        self.n_line_edit_controller = IntLineEditController()
        self.n_line_edit_controller.connect_to_line_edit(n_line_edit)
        self.line_edits["n_line_edit"] = n_line_edit

        # Создание LineEdit'а для L
        l_line_edit = IntLineEdit()
        self.l_line_edit_controller = IntLineEditController()
        self.l_line_edit_controller.connect_to_line_edit(l_line_edit)
        self.line_edits["l_line_edit"] = l_line_edit

        # Добавление LineEdit'ов в Layout
        self.addRow("Введите размер доски N:", n_line_edit)
        self.addRow("Введите кол-во фигур, которые нужно расставить L:", l_line_edit)



class ButtonsLayout(QHBoxLayout):
    """ Layout для кнопок """
    def __init__(self, parent_window: Optional['MainWindow'] = None):
        super().__init__()
        self.parent_window = parent_window
        self.buttons = {
            "arrange_button": None,
            "render_button": None
        }

        # Создание кнопки для вызова окна расстановки фигур
        arrange_button = QPushButton("Расставить фигуры")
        arrange_button.setEnabled(False)
        self.arrange_button_controller = ArrangeButtonController(self.parent_window)
        self.arrange_button_controller.connect_to_button(arrange_button)
        self.buttons["arrange_button"] = arrange_button

        # Создание кнопки для вызова окна отрисовки результатов 
        render_button = QPushButton("Отрисовать доску")
        render_button.setEnabled(False)
        self.render_button_controller = RenderButtonController(self.parent_window)
        self.render_button_controller.connect_to_button(render_button)
        self.buttons["render_button"] = render_button

        # Создание кнопки для выхода из приложения
        exit_button = QPushButton("Выйти")
        self.exit_button_controller = ExitButtonController()
        self.exit_button_controller.connect_to_button(exit_button)

        # Добавление кнопок в Layout
        self.addWidget(arrange_button)
        self.addWidget(render_button)
        self.addWidget(exit_button)



class MainLayout(QVBoxLayout):
    """ Основной Layout для главного окна """
    def __init__(self, parent_window: Optional['MainWindow'] = None):
        super().__init__()
        self.parent_window = parent_window

        # Создание layout'ов
        self.line_edit_layout = LineEditLayout()
        self.button_layout = ButtonsLayout(self.parent_window)

        # Добавление layout'ов в общий layout
        self.addLayout(self.line_edit_layout)
        self.addLayout(self.button_layout)

        # Таймер для проверки заполения LineEdit'ов, переключения кнопок и установки значений для доски
        self.timer = QTimer(self) 
        self.timer.timeout.connect(self._toggle_buttons)
        self.timer.timeout.connect(self._set_values)
        self.timer.start(50)

    

    def _toggle_buttons(self):
        """ Метод для переключения состояний кнопок """
        N = self.parent_window.board_config["params"]["N"]
        L = self.parent_window.board_config["params"]["L"]

        for button in self.button_layout.buttons.values():
            if N > 0 and L > 0:
                button.setEnabled(True)
            else:
                button.setEnabled(False)


    def _set_values(self):
        """ Метод для установки значений в конфиг доски """
        n_line_edit_value = self.line_edit_layout.line_edits["n_line_edit"].text()
        l_line_edit_value = self.line_edit_layout.line_edits["l_line_edit"].text()

        # Если есть значение N, то выставляем его, иначе 0
        if n_line_edit_value:
            self.parent_window.board_config["params"]["N"] = int(n_line_edit_value)
        else:
            self.parent_window.board_config["params"]["N"] = 0
            

        # Если есть значение L, то выставляем его, иначе 0
        if l_line_edit_value:
            self.parent_window.board_config["params"]["L"] = int(l_line_edit_value)
        else:
            self.parent_window.board_config["params"]["L"] = 0
