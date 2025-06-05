from typing import Optional
from frontend.controllers.abstract_button_controller import AbstractButtonController



class SaveButtonController(AbstractButtonController):
    """ Контроллер для кнопки сохранения результатов """
    def __init__(self, parent_window: Optional['RenderWindow'] = None):
        super().__init__(parent_window)


    def handle_click(self):
        self.parent_window.accept()
        

class CloseButtonController(AbstractButtonController):
    """ Контроллер для кнопки закрытия окна результатов """
    def __init__(self, parent_window: Optional['RenderWindow'] = None):
        super().__init__(parent_window)


    def handle_click(self):
        self.parent_window.reject()
