from PySide6.QtWidgets import QListWidgetItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QColor



class PrincessListItem(QListWidgetItem):
    """ Строка списка, хранящая координаты результирующих координат фигур """ 
    def __init__(self, princesses_coords: set):
        super().__init__(str(princesses_coords))
        
        self.princesses_coords = princesses_coords

        # Установка текста по центру
        self.setTextAlignment(Qt.AlignCenter)
        


class NoResultListItem(QListWidgetItem):
    """ Строка для вывода сообщения об отсутствии результатов """ 
    def __init__(self, text: str):
        super().__init__(text)

        # Установка текста красного цвета по центру
        self.setTextAlignment(Qt.AlignCenter)
        self.setForeground(QBrush(QColor("red")))
