def get_backward_moves(princess_coords):
    x = princess_coords[0]
    y = princess_coords[1]

    moves = set()
    for move in range(1,4):
        # Vertical moves
        if y-move >= 0:
            moves.add((x,y-move))

        # Horizontal moves
        if x-move >= 0:
            moves.add((x-move,y))
            
            
        # Diagonal moves
        if x-move >= 0 and y-move >= 0:
            moves.add((x-move,y-move))

        if x+move < N and y-move >= 0:
            moves.add((x+move,y-move))

    return moves


def get_forward_moves(princess_coords):
    x = princess_coords[0]
    y = princess_coords[1]

    moves = set()
    for move in range(1,4):
        # Vertical moves
        if y+move < N:
            moves.add((x,y+move))

        # Horizontal moves
        if x+move < N:
            moves.add((x+move,y))
            
            
        # Diagonal moves
        if x+move < N and y+move < N:
            moves.add((x+move,y+move))

        if x-move >= 0 and y+move < N:
            moves.add((x-move,y+move))

    return moves


def get_all_moves(princess_coords):
    all_moves = set()
    all_moves |= get_backward_moves(princess_coords) | get_forward_moves(princess_coords)
    
    return all_moves


def get_initial_free_squares(princesses_coords, empty_board: set()):
    occupied_squares = set()
    for princess_coords in princesses_coords:
        occupied_squares.add(princess_coords)
        occupied_squares |= get_all_moves(princess_coords)
    
    return empty_board - occupied_squares


def init_empty_board():
    board = set()
    for y in range(N):
        for x in range(N):
            board.add((x,y))
    return board

def get_free_squares(princess_coords, free_squares):
    occupied_squares = get_forward_moves(princess_coords)
    occupied_squares.add(princess_coords)
    return free_squares.copy() - occupied_squares


def is_result(princesses_coords):
    return len(princesses_coords) == K-1


def solve(initial_free_squares: set, princesses_coords: set = set()):
    while initial_free_squares:
        root_free_square = initial_free_squares.pop()
        princesses_coords.add(root_free_square)


        next_free_squares = get_free_squares(root_free_square, initial_free_squares)
        if is_result(princesses_coords):
            return princesses_coords, len(next_free_squares)
        solve(next_free_squares.copy(), princesses_coords.copy())
        



N = 8
K = 3 
initial_princesses_coords = {(0,1), (6,0), (5,7)}


empty_board = init_empty_board()
initial_free_squares = get_initial_free_squares(initial_princesses_coords, empty_board) 
print(solve(initial_free_squares))
