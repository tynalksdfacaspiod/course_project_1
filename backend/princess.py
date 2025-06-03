from abc import ABC, abstractmethod
from PySide6.QtGui import QColor
from backend.chess_calculator import get_moves


class AbstractPrincess(ABC):
    def __init__(self, board, x, y):
        self.board = board
        self.x = x
        self.y = y
        self._set_colors()

        self.moves = get_moves((self.x,self.y), self.board.N)
        self._add_moves_to_board()


    def _add_moves_to_board(self):
        self.board.moves |= self.moves


    def on_pop(self):
        self.board.moves -= self.moves
        self.board.fetch_moves()


    @abstractmethod
    def _set_colors(self):
        pass


class UserPrincess(AbstractPrincess):
    def __init__(self, board, x, y):
        super().__init__(board, x, y)


    def _set_colors(self):
        self.figure_color = QColor("lime")
        self.moves_color = QColor("red")



class BotPrincess(AbstractPrincess):
    def __init__(self, board, x, y):
        super().__init__(board, x, y)

    
    def _set_colors(self):
        self.figure_color = QColor("cyan")
        self.figure_color = QColor("magenta")
