from abc import ABC, abstractmethod
from PySide6.QtCore import QCoreApplication


class AbstractButtonController(ABC):
    def __init__(self, parent_window=None):
        super().__init__()
        self.parent_window = parent_window

    @abstractmethod
    def handle_click(self):
        pass

    def connect_to_button(self, button):
        button.clicked.connect(self.handle_click)


class ExitButtonController(AbstractButtonController):
    def __init__(self, parent_window=None):
        super().__init__(parent_window)

    def handle_click(self):
        QCoreApplication.quit()



class ArrangeButtonController(AbstractButtonController):
    def __init__(self, arrange_window, parent_window=None):
        super().__init__(parent_window)
        self.arrange_window = arrange_window

    def handle_click(self):
        self.arrange_window.exec()



class ConfirmButtonController(AbstractButtonController):
    def __init__(self, parent_window=None):
        super().__init__(parent_window)

    
    def handle_click(self):
        self.parent_window.accept()



class CloseButtonController(AbstractButtonController):
    def __init__(self, parent_window=None):
        super().__init__(parent_window)


    def handle_click(self):
        self.parent_window.reject()
