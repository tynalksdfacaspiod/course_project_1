from PySide6.QtCore import QThread, Signal, QObject
from PySide6.QtWidgets import QListWidgetItem

from backend.princesses_generator import PrincessesGenerator

class Worker(QObject):
    """ Worker для обработки результатов алгоритма """ 

    # Создание сигналов
    item_ready = Signal(set)
    finished = Signal()
    no_result = Signal()
    

    def __init__(self, board_config: dict):
        super().__init__()
        self.board_config = board_config
        

    def run(self):
        """ Метод для запуска Worker'а """

        # Создание генератора результатирующих расстановок фигур
        princesses_generator = PrincessesGenerator(self.board_config)
        results = princesses_generator.start_solving()
        
        # Создание переменной для отслеживания наличия хотя бы одного результата
        found_any = False

        try:
            # Проходимся по результатам и поочерёдно отправляем их для добавления в список
            for result in results:
                found_any = True
                self.item_ready.emit(result)
        
            # Если не нашлось ни одного результата, то сообщаем об этом
            if not found_any:
                self.no_result.emit()

        finally:
            # Завершаем работу Worker'а
            self.finished.emit()
