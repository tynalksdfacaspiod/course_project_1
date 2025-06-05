from PySide6.QtCore import QThread, QCoreApplication
from PySide6.QtWidgets import QDialog, QListWidgetItem

from frontend.layouts.render_window_layouts import RenderWindowLayout
from frontend.widgets.chess_board import ChessBoard
from frontend.widgets.list_item import PrincessListItem, NoResultListItem
from frontend.workers.worker import Worker

from backend.other.file import read_board_file, is_board_config_exists, write_results
from backend.chess_calculator import get_moves



class RenderWindow(QDialog):
    def __init__(self, board_config: dict):
        super().__init__()
        
        # Установка конфига доски из главного окна
        self.board_config = board_config 

        # Если уже существует доска с расставленными фигурами, то загрузить её конфиг
        if is_board_config_exists():
            self.board_config = self._get_board_config()

        # Установка названия, размеров и разметки окна
        self.setWindowTitle("Окно отрисовки результатов")
        self.setFixedSize(1000,700)
        self.setLayout(RenderWindowLayout(self))

        self.setup_thread()

    
    def render_board(self, item: 'QListWidgetItem'):
        """ Метод отрисовки доски с результатами """

        # Установка конфига для доски
        N = self.board_config["params"]["N"]
        board_config = self.board_config.copy()

        board_config["princesses"]["bot_princesses_coords"] = set()
        board_config["moves"]["bot_moves"] = set()

        # Установка фигур и их ходов
        for princess_coords in item.princesses_coords:
            
            # Если нет пользовательских фигур, то расставлять только те, что рассчитаны алгоритмом
            if board_config["princesses"]["user_princesses_coords"] is None:
                board_config["princesses"]["bot_princesses_coords"].add(princess_coords)
                board_config["moves"]["bot_moves"] |= get_moves(princess_coords,N)
                continue
            

            if princess_coords not in board_config["princesses"]["user_princesses_coords"]:
                board_config["princesses"]["bot_princesses_coords"].add(princess_coords)
                board_config["moves"]["bot_moves"] |= get_moves(princess_coords,N)



        # Создание новой доски на основе конфига
        new_board = ChessBoard(board_config, clickable_enabled=False)

        # Получение MainLayout'а в котором хранится доска и замена этой доски на новую
        main_layout = self.layout().itemAt(0).layout()
        main_layout.replaceWidget(self.board, new_board)

        # Установка новой доски в качестве свойства
        self.board = new_board

    
    def _unlock_save_button(self):
        """ Метод для разблокировки кнопки сохранения результатов """
        self.save_button.setEnabled(True)


    def _add_result_to_list(self, princesses_coords: set):
        """ Метод для добавление результата в список """
        self.list_widget.addItem(PrincessListItem(princesses_coords))
    
    
    def _no_result(self):
        """ Метод для обработки ситуации, когда невозможно расставить фигуры """
        self.list_widget.addItem(NoResultListItem("Невозможно расставить фигуры"))
    

    def _get_board_config(self) -> dict:
        """ Получение конфига доски из файла """
        return read_board_file()

    
    def setup_thread(self):
        """ Метод для установки работы с потоками и Worker'а """

        # Установка потоков и Worker'а
        self.thread = QThread()
        self.worker = Worker(self.board_config)
        self.worker.moveToThread(self.thread)
        
        # Подключение сигналов
        self.worker.item_ready.connect(self._add_result_to_list)
        self.worker.no_result.connect(self._no_result)
        self.thread.finished.connect(self._unlock_save_button)
        self.worker.finished.connect(self.thread.quit)
        self.thread.finished.connect(self.thread.deleteLater)
        
        # Запуск
        self.thread.started.connect(self.worker.run)
        self.thread.start()



    def accept(self):
        """ Метод для отработки нажатия по кнопке записи результатов """
        
        # Сбор резульзатов в список и их запись в файл. При успешной записи завершение работы приложения
        results = [self.list_widget.item(i) for i in range(self.list_widget.count())]
        if write_results(results):
            QCoreApplication.quit()


    def reject(self):
        """ Метод для отработки нажатия по кнопке записи результатов """

        # Закрытие окна без действий
        super().reject()
