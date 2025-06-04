from frontend.controllers.abstract_button_controller import AbstractButtonController



class SaveButtonController(AbstractButtonController):
    def __init__(self, parent_window=None):
        super().__init__(parent_window)


    def handle_click(self):
        self.parent_window.accept()
        

class CloseButtonController(AbstractButtonController):
    def __init__(self, parent_window=None):
        super().__init__(parent_window)


    def handle_click(self):
        self.parent_window.reject()
