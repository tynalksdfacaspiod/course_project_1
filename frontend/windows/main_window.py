from PySide6.QtWidgets import QMainWindow, QWidget
from frontend.layouts.main_window_layouts import MainLayout


class MainWindow(QMainWindow):
    """ Основное окно приложения """
    def __init__(self):
        super().__init__()

        # Создание начального конфига доски
        self.board_config = {
            "params": {"N": 0, "L": 0, "K": 0},
            "princesses": {
                "user_princesses_coords": None,
                "bot_princesses_coords": None
            },
            "moves": {
                "user_moves": None,
                "bot_moves": None,
            },
            "free_squares_coords": None
        }

        
        # Установка названия окна
        self.setWindowTitle("Chess")

        # Установка разметки в качестве центрального виджета
        central_widget = QWidget()
        central_widget.setLayout(MainLayout(self))
        self.setCentralWidget(central_widget)
