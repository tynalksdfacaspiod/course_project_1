def get_moves(princess_coords, N) -> set:
    """ Функция возвращает ходы переданной фигуры """
    x = princess_coords[0]
    y = princess_coords[1]

    def get_vertical_moves() -> set:
        vertical_moves = set()
        for move in range(1,4):
            if y-move >= 0:
                vertical_moves.add((x,y-move))
            if y+move < N:
                vertical_moves.add((x,y+move))
        return vertical_moves

    def get_horizontal_moves() -> set:
        horizontal_moves = set()
        for move in range(1,4):
            if x-move >= 0:
                horizontal_moves.add((x-move,y))
            if x+move < N:
                horizontal_moves.add((x+move,y))
        return horizontal_moves
    
    def get_diagonal_moves() -> set:
        diagonal_moves = set()
        for move in range(1,4):
            # Диагональные ходы "\": с левого верхнего угла к правому нижнему
            if x-move >= 0 and y-move >= 0:
                diagonal_moves.add((x-move,y-move))
            if x+move < N and y+move < N:
                diagonal_moves.add((x+move,y+move))

            # Диагональные ходы "/": с левого нижнего угла к правому верхнему
            if x-move >= 0 and y+move < N:
                diagonal_moves.add((x-move,y+move))
            if x+move < N and y-move >= 0:
                diagonal_moves.add((x+move,y-move))
        return diagonal_moves

    moves = get_vertical_moves() | get_horizontal_moves() | get_diagonal_moves()
    return moves
