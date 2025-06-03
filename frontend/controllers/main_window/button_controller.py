from PySide6.QtCore import QCoreApplication
from frontend.controllers.abstract_button_controller import AbstractButtonController
from frontend.windows.arrange_window import ArrangeWindow
from frontend.windows.render_window import RenderWindow



class ExitButtonController(AbstractButtonController):
    def __init__(self, parent_window=None):
        super().__init__(parent_window)

    def handle_click(self):
        QCoreApplication.quit()



class ArrangeButtonController(AbstractButtonController):
    def __init__(self, parent_window=None):
        super().__init__(parent_window)

    def handle_click(self):
        self.arrange_window = ArrangeWindow(self.parent_window.values)
        self.arrange_window.exec()



class RenderButtonController(AbstractButtonController):
    def __init__(self, parent_window=None):
        super().__init__(parent_window)
    

    def handle_click(self):
        self.render_window = RenderWindow(self.parent_window.values)
        self.render_window.exec()
