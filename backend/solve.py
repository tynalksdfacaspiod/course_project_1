def get_forward_moves(princess_coords):
    x = princess_coords[0]
    y = princess_coords[1]

    moves = set()
    for move in range(1,4):
        # Vertical moves
        if y+move < N:
            moves.add(x,y+move)

        # Horizontal moves
        if x+move < N:
            moves.add(x+move,y)
            
            
        # Diagonal moves
        if x+move < N and y+move < N:
            moves.add(x+move,y+move)

        if x-move >= 0 and y+move < N:
            moves.add(x-move,y+move)


    return moves


def get_free_squares(princess_coords, free_squares):
    moves = get_forward_moves(princess_coord)
    occupied_squares = moves
    occupied_squares.add(princess_coords)
    return free_squares.copy() - occupied_squares


def solve(initial_free_squares, L):
    def is_result():
        return len(princesses_coords) == L

    
    def get_childs(princesses_coords: list, current_princess_coords: tuple, moves: set) -> list:
        """ Функция возвращает координаты клеток, в которые можно поставить последующие фигуры """
        childs = []

        # Начинаем с чётвертой по счёту клетки, так как принцесса ходит на три
        x = current_princess_coords[0]+4
        y = current_princess_coords[1]


        # Перебираем координаты на наличие свободных клеток, не находящихся под боем других фигур
        while y < N:

            if x >= N: # Доходим до правого края доски
                x = 0
                y += 1
                continue

            if is_safe((y,x), princesses_coords, moves):
                childs.append(princesses_coords + [(y,x)])

            x+=1
        return childs

        
    def is_safe(cell: tuple, princesses_coords: list, moves: set) -> bool:
        """ Функция проверяет, находится ли клетка под боем других фигур и не занята ли она """
        if (cell in princesses_coords) or (cell in moves):
            return False
        return True


    def solve_childs(current_princesses: list, parent_moves: set) -> None:
        """ Функция расставляет фигуры по безопасным клеткам """
        nonlocal result
        current_moves = get_all_moves([current_princesses[-1]]) | parent_moves
        childs = get_childs(current_princesses, current_princesses[-1], current_moves)

        for child in childs:
            if is_result(child):
                # Если один из "детей" является решением, значит и все остальные являются решением
                # Так как за один раз выставляется только одна фигура
                result += childs
                break
            else:
                # Если "ребёнок" не является решением, то расставляем фигуры дальше
                solve_childs(child, current_moves)
