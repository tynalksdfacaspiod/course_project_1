from abc import ABC, abstractmethod
from backend.chess_calculator import get_moves


class AbstractPrincess:
    """ Абстрактный класс для фигуры """
    def __init__(self, board: 'ChessBoard', x: int, y: int):
        self.board = board
        self.x = x
        self.y = y

        # Получение ходов фигуры и их добавление на доску
        self.moves = get_moves((self.x,self.y), self.board.params["N"])
        self._add_moves_to_board()


    @abstractmethod
    def _add_moves_to_board(self):
        """ Абстрактный метод для добавления ходов на доску """
        pass


    @abstractmethod
    def on_pop(self):
        """ Абстрактный метод для отработки удаления фигуры с доски """
        pass



class UserPrincess(AbstractPrincess):
    """ Пользовательская фигура """
    def __init__(self, board: 'ChessBoard', x: int, y: int):
        super().__init__(board, x, y)


    def _add_moves_to_board(self):
        """ Метод для добавления пользовательских ходов на доску """
        self.board.user_moves |= self.moves


    def on_pop(self):
        """ Метод для удаления пользовательских ходов с доски """
        self.board.user_moves -= self.moves
        self.board.fetch_moves()



class BotPrincess(AbstractPrincess):
    """ Фигура, просчитанная алгоритмом """
    def __init__(self, board: 'ChessBoard', x: int, y: int):
        super().__init__(board, x, y)


    def _add_moves_to_board(self):
        """ Метод для добавления ходов на доску """
        self.board.bot_moves |= self.moves


    def on_pop(self):
        """ Метод для удаления ходов с доски """
        self.board.bot_moves -= self.moves
        self.board.fetch_moves()
