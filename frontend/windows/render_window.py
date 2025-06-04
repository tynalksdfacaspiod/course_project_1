from PySide6.QtCore import QThread
from PySide6.QtWidgets import QDialog, QListWidgetItem

from frontend.layouts.render_window_layouts import RenderWindowLayout
from frontend.widgets.chess_board import ChessBoard
from frontend.widgets.list_item import PrincessListItem
from frontend.workers.worker import Worker
from backend.other.file import (
    read_board_file, is_board_config_exists
)



class RenderWindow(QDialog):
    def __init__(self, board_config):
        super().__init__()
        
        self.board_config = board_config 

        if is_board_config_exists():
            self.board_config = self._get_board_config()

        self.board = ChessBoard(self.board_config, clickable_enabled=False)

        self.setWindowTitle("Окно отрисовки результатов")
        self.setFixedSize(1000,700)
        self.setLayout(RenderWindowLayout(self))

        self.setup_thread()


    def _add_result_to_list(self, princesses_coords):
        self.list_widget.addItem(PrincessListItem(princesses_coords))
    

    def _get_board_config(self):
        return read_board_file()


    def _get_input_data(self):
        return read_input_file()

    def setup_thread(self):
        self.thread = QThread()
        self.worker = Worker(self.board_config)
        self.worker.moveToThread(self.thread)
        
        self.worker.item_ready.connect(self._add_result_to_list)
        self.worker.finished.connect(self.thread.quit)
        self.thread.finished.connect(self.thread.deleteLater)
        
        self.thread.started.connect(self.worker.run)
        self.thread.start()



    def accept(self):
        pass
