from abc import ABC, abstractmethod
from backend.chess_calculator import get_moves


class AbstractPrincess:
    def __init__(self, board, x, y):
        self.board = board
        self.x = x
        self.y = y

        self.moves = get_moves((self.x,self.y), self.board.params["N"])
        self._add_moves_to_board()


    @abstractmethod
    def _add_moves_to_board(self):
        pass


    @abstractmethod
    def on_pop(self):
        pass



class UserPrincess(AbstractPrincess):
    def __init__(self, board, x, y):
        super().__init__(board, x, y)


    def _add_moves_to_board(self):
        self.board.user_moves |= self.moves


    def on_pop(self):
        self.board.user_moves -= self.moves
        self.board.fetch_moves()



class BotPrincess(AbstractPrincess):
    def __init__(self, board, x, y):
        super().__init__(board, x, y)


    def _add_moves_to_board(self):
        self.board.bot_moves |= self.moves


    def on_pop(self):
        self.board.bot_moves -= self.moves
        self.board.fetch_moves()
