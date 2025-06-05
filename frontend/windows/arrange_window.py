from PySide6.QtWidgets import QDialog

from frontend.layouts.arrange_window_layouts import ArrangeWindowLayout
from frontend.widgets.chess_board import ChessBoard
from backend.other.file import (
    cleanup,
    write_board_file, read_board_file, is_board_config_exists
)



class ArrangeWindow(QDialog):
    """ Окно для расстановки фигур """
    def __init__(self, board_config: dict):
        super().__init__()

        # Установка конфига доски из главного окна
        self.board_config = board_config 

        # Если уже существует доска с расставленными фигурами, то загрузить её конфиг
        if is_board_config_exists():
            self.board_config = self._get_board_config()

        # Создание доски c кликабельными клетками
        self.board = ChessBoard(self.board_config, clickable_enabled=True)
        
        # Установка названия, размеров и разметки окна
        self.setWindowTitle("Окно расстановки фигур")
        self.setFixedSize(1000, 700)
        self.setLayout(ArrangeWindowLayout(parent_window=self))

    
    def _get_board_config(self) -> dict:
        """ Метод для получения конфига доски """
        return read_board_file()


    def accept(self):
        """ Метод для обработки нажатия по кнопке подтверждения """

        # Сохранения количества расставленных фигур
        self.board.save_princesses_count()

        # Получение параметров, координат с доски
        params = self.board.get_params()
        princesses_coords = self.board.get_princesses_coords()
        moves_coords = self.board.get_moves_coords()
        free_squares_coords = self.board.get_free_squares_coords()

        # Запись параметров, координат с доски в конфигурационный файл
        write_board_file(params, princesses_coords, moves_coords, free_squares_coords)

        super().accept()


    def reject(self):
        """ Метод для обработки нажатия по кнопке закрытия окна """

        # Закрытие окна без действий
        super().reject()
