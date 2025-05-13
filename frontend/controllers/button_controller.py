from abc import ABC, abstractmethod
from PySide6.QtCore import QCoreApplication


class AbstractButtonController(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def handle_click(self):
        pass

    def connect_to_button(self, button):
        button.clicked.connect(self.handle_click)


class ExitButtonController(AbstractButtonController):
    def __init__(self):
        super().__init__()

    def handle_click(self):
        QCoreApplication.quit()
