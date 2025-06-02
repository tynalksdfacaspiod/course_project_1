class Princess:
    def __init__(self, board, x, y):
        self.board = board
        self.x = x
        self.y = y
        self.moves = self.get_moves()
        self.board.moves |= self.moves

    
    def on_pop(self):
        self.board.moves -= self.moves
        self.board.fetch_moves() # Пересобрать ходы, чтобы не удалить пересекающиеся от других фигур

    def get_moves(self) -> set:
        """ Функция возвращает ходы переданной фигуры """

        def get_vertical_moves() -> set:
            vertical_moves = set()
            for move in range(1,4):
                if self.y-move >= 0:
                    vertical_moves.add((self.x,self.y-move))
                if self.y+move < self.board.N:
                    vertical_moves.add((self.x,self.y+move))
            return vertical_moves

        def get_horizontal_moves() -> set:
            horizontal_moves = set()
            for move in range(1,4):
                if self.x-move >= 0:
                    horizontal_moves.add((self.x-move,self.y))
                if self.x+move < self.board.N:
                    horizontal_moves.add((self.x+move,self.y))
            return horizontal_moves
        
        def get_diagonal_moves() -> set:
            diagonal_moves = set()
            for move in range(1,4):
                # Диагональные ходы "\": с левого верхнего угла к правому нижнему
                if self.x-move >= 0 and self.y-move >= 0:
                    diagonal_moves.add((self.x-move,self.y-move))
                if self.x+move < self.board.N and self.y+move < self.board.N:
                    diagonal_moves.add((self.x+move,self.y+move))

                # Диагональные ходы "/": с левого нижнего угла к правому верхнему
                if self.x-move >= 0 and self.y+move < self.board.N:
                    diagonal_moves.add((self.x-move,self.y+move))
                if self.x+move < self.board.N and self.y-move >= 0:
                    diagonal_moves.add((self.x+move,self.y-move))
            return diagonal_moves

        moves = get_vertical_moves() | get_horizontal_moves() | get_diagonal_moves()
        return moves
