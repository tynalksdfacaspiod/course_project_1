from PySide6.QtWidgets import QMainWindow, QWidget
from frontend.layouts.main_window_layouts import MainLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.values = {
            "n": 0,
            "l": 0
        }

        self.setWindowTitle("Chess")

        central_widget = QWidget()
        central_widget.setLayout(MainLayout(self))
        self.setCentralWidget(central_widget)


    def set_n(value):
        self.values[0] = value


    def set_k(value):
        self.values[1] = value
