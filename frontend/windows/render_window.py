from PySide6.QtCore import QThread, QCoreApplication
from PySide6.QtWidgets import QDialog, QListWidgetItem

from frontend.layouts.render_window_layouts import RenderWindowLayout
from frontend.widgets.chess_board import ChessBoard
from frontend.widgets.list_item import PrincessListItem, NoResultListItem
from frontend.workers.worker import Worker

from backend.other.file import read_board_file, is_board_config_exists, write_results
from backend.chess_calculator import get_moves



class RenderWindow(QDialog):
    def __init__(self, board_config):
        super().__init__()
        
        self.board_config = board_config 

        if is_board_config_exists():
            self.board_config = self._get_board_config()

        self.setWindowTitle("Окно отрисовки результатов")
        self.setFixedSize(1000,700)
        self.setLayout(RenderWindowLayout(self))

        self.setup_thread()

    
    def render_board(self, item):
        N = self.board_config["params"]["N"]
        board_config = self.board_config.copy()

        board_config["princesses"]["bot_princesses_coords"] = set()
        board_config["moves"]["bot_moves"] = set()

        for princess_coords in item.princesses_coords:
            if princess_coords not in board_config["princesses"]["user_princesses_coords"]:
                board_config["princesses"]["bot_princesses_coords"] = item.princesses_coords
                board_config["moves"]["bot_moves"] |= get_moves(princess_coords,N)



        new_board = ChessBoard(board_config, clickable_enabled=False)
        main_layout = self.layout().itemAt(0).layout()
        main_layout.replaceWidget(self.board, new_board)

        self.board = new_board

    
    def _unlock_save_button(self):
        self.save_button.setEnabled(True)


    def _add_result_to_list(self, princesses_coords):
        self.list_widget.addItem(PrincessListItem(princesses_coords))
    
    
    def _no_result(self):
        self.list_widget.addItem(NoResultListItem("Невозможно расставить фигуры"))
    

    def _get_board_config(self):
        return read_board_file()


    def _get_input_data(self):
        return read_input_file()

    def setup_thread(self):
        self.thread = QThread()
        self.worker = Worker(self.board_config)
        self.worker.moveToThread(self.thread)
        
        self.worker.item_ready.connect(self._add_result_to_list)
        self.worker.no_result.connect(self._no_result)
        self.thread.finished.connect(self._unlock_save_button)
        self.worker.finished.connect(self.thread.quit)
        self.thread.finished.connect(self.thread.deleteLater)
        
        self.thread.started.connect(self.worker.run)
        self.thread.start()



    def accept(self):
        results = [self.list_widget.item(i) for i in range(self.list_widget.count())]
        if write_results(results):
            QCoreApplication.quit()


    def reject(self):
        super().reject()
