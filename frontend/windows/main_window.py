from PySide6.QtWidgets import QMainWindow, QWidget
from layouts.main_window_layouts import MainLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chess")

        central_widget = QWidget()
        central_widget.setLayout(MainLayout())
        self.setCentralWidget(central_widget)
