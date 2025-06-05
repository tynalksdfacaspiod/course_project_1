from typing import Optional
from frontend.controllers.abstract_button_controller import AbstractButtonController



class ConfirmButtonController(AbstractButtonController):
    """ Контроллер для кнопки подтверждения """
    def __init__(self, parent_window: Optional['ArrangeWindow'] = None):
        super().__init__(parent_window)

    
    def handle_click(self):
        self.parent_window.accept()



class CloseButtonController(AbstractButtonController):
    """ Контроллер для кнопки, закрывающей окно """
    def __init__(self, parent_window: Optional['ArrangeWindow'] = None):
        super().__init__(parent_window)


    def handle_click(self):
        self.parent_window.reject()
