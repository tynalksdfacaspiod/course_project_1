from PySide6.QtWidgets import QDialog, QWidget

from layouts.arrange_window_layouts import ArrangeWindowLayout

class ArrangeWindow(QDialog):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Окно расстановки фигур")
        self.setFixedSize(1000, 700)
        self.setLayout(ArrangeWindowLayout())
        
