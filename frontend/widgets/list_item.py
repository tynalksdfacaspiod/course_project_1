from PySide6.QtWidgets import QListWidgetItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QColor



class PrincessListItem(QListWidgetItem):
    def __init__(self, princesses_coords):
        super().__init__(str(princesses_coords))
        
        self.princesses_coords = princesses_coords
        self.setTextAlignment(Qt.AlignCenter)
        


class NoResultListItem(QListWidgetItem):
    def __init__(self, text):
        super().__init__(text)

        self.setTextAlignment(Qt.AlignCenter)
        self.setForeground(QBrush(QColor("red")))
