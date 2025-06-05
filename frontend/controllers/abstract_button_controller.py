from typing import Optional, Union
from abc import ABC, abstractmethod



class AbstractButtonController(ABC):
    """ Абстрактный контроллер для кнопок """
    def __init__(self, parent_window: Optional[Union['MainWindow', 'ArrangeWindow', 'RenderWindow']] = None):
        super().__init__()
        self.parent_window = parent_window

    @abstractmethod
    def handle_click(self):
        """ Абстрактный метод для отработки клика по кнопке """
        pass

    def connect_to_button(self, button: 'QPushButton'):
        """ Метод для подключения кнопки к контроллеру """
        button.clicked.connect(self.handle_click)
