from typing import Optional
from PySide6.QtCore import QCoreApplication
from frontend.controllers.abstract_button_controller import AbstractButtonController
from frontend.windows.arrange_window import ArrangeWindow
from frontend.windows.render_window import RenderWindow



class ExitButtonController(AbstractButtonController):
    """ Контроллер для кнопки выхода из приложения """
    def __init__(self, parent_window: Optional['MainWindow'] = None):
        super().__init__(parent_window)

    def handle_click(self):
        """ Выход из приложения """
        QCoreApplication.quit()



class ArrangeButtonController(AbstractButtonController):
    """ Контроллер для кнопки вызова окна расстановки фигур """
    def __init__(self, parent_window: Optional['MainWindow'] = None):
        super().__init__(parent_window)

    def handle_click(self):
        """ Создание окна расстановки фигур с передачей в него конфига доски """
        self.arrange_window = ArrangeWindow(self.parent_window.board_config)
        self.arrange_window.exec()



class RenderButtonController(AbstractButtonController):
    """ Контроллер для кнопки вызова окна отрисовки результатов """
    def __init__(self, parent_window: Optional['MainWindow'] = None):
        super().__init__(parent_window)
    

    def handle_click(self):
        """ Создание окна отрисовки результатов с передачей в него конфига доски """
        self.render_window = RenderWindow(self.parent_window.board_config)
        self.render_window.exec()
