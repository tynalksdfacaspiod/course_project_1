def get_moves(princess_coords) -> set:
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


def get_initial_free_squares(princesses_coords, empty_board: set()):
    occupied_squares = set()
    for princess_coords in princesses_coords:
        occupied_squares.add(princess_coords)
        occupied_squares |= get_moves(princess_coords)
    
    return empty_board - occupied_squares


def init_empty_board():
    board = set()
    for y in range(N):
        for x in range(N):
            board.add((x,y))
    return board

def get_free_squares(princess_coords, free_squares):
    occupied_squares = get_moves(princess_coords)
    occupied_squares.add(princess_coords)
    return free_squares.copy() - occupied_squares


def is_result(princesses_coords):
    return len(princesses_coords) == K-1


def solve(initial_free_squares: set, princesses_coords: set = None):
    if princesses_coords is None:
        princesses_coords = set()

    while initial_free_squares:
        root_free_square = initial_free_squares.pop()
        new_princesses_coords = princesses_coords.copy()
        new_princesses_coords.add(root_free_square)


        next_free_squares = get_free_squares(root_free_square, initial_free_squares)

        if is_result(new_princesses_coords):
            return new_princesses_coords, next_free_squares

        result = solve(next_free_squares.copy(), new_princesses_coords.copy())
        if not result is None:
            return result

    
    return None


N = 8
K = 3 
initial_princesses_coords = {(0,1), (6,0), (5,7)}


empty_board = init_empty_board()
initial_free_squares = get_initial_free_squares(initial_princesses_coords, empty_board) 
print(solve(initial_free_squares))
