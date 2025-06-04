from PySide6.QtCore import QThread, Signal, QObject
from PySide6.QtWidgets import QListWidgetItem

from backend.princesses_generator import PrincessesGenerator

class Worker(QObject):
    item_ready = Signal(set)
    finished = Signal()
    no_result = Signal()
    
    def __init__(self, board_config):
        super().__init__()
        self.board_config = board_config
        
    def run(self):
        princesses_generator = PrincessesGenerator(self.board_config)
        results = princesses_generator.start_solving()
        
        found_any = False

        try:
            for result in results:
                found_any = True
                self.item_ready.emit(result)
        
            if not found_any:
                self.no_result.emit()

        finally:
            self.finished.emit()
