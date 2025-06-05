from typing import Any
from abc import ABC, abstractmethod



class AbstractLineEditController(ABC):
    """ Абстрактный класс контролллера для IntLineEdit'а """
    def __init__(self):
        super().__init__()

    @abstractmethod
    def on_text_changed(self, text: str) -> Any:
        """ Абстрактный метод для отработки изменения текста внутри IntLineEdit'а """
        pass

    def connect_to_line_edit(self, line_edit: 'IntLineEdit'):
        """ Метод для подключения IntLineEdit'а к контроллеру """ 
        self.line_edit = line_edit
        self.line_edit.textChanged.connect(self.on_text_changed)



class IntLineEditController(AbstractLineEditController):
    """ Контроллер для IntLineEdit'а """
    def __init__(self):
        super().__init__()

    def on_text_changed(self, text: str) -> bool:
        """ Метод изменяет свойство is_empty при наличии/отсутсвии текста в IntLineEdit'е """
        if text:
            self.line_edit.is_empty = False
        else:
            self.line_edit.is_empty = True
