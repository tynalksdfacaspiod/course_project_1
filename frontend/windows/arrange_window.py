from PySide6.QtWidgets import QDialog, QWidget

from frontend.layouts.arrange_window_layouts import ArrangeWindowLayout

class ArrangeWindow(QDialog):
    def __init__(self, n):
        super().__init__()
        self.n = n
        
        self.setWindowTitle("Окно расстановки фигур")
        self.setFixedSize(1000, 700)
        self.setLayout(ArrangeWindowLayout(parent_window=self))
        
