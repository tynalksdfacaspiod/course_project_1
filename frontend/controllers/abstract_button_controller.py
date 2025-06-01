from abc import ABC, abstractmethod



class AbstractButtonController(ABC):
    def __init__(self, parent_window=None):
        super().__init__()
        self.parent_window = parent_window

    @abstractmethod
    def handle_click(self):
        pass

    def connect_to_button(self, button):
        button.clicked.connect(self.handle_click)
