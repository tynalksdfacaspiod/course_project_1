from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import QIntValidator 


class IntLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setValidator(QIntValidator(0, 20))
        self.is_empty = True
