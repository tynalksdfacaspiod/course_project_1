from typing import Optional
from backend.chess_calculator import get_moves

class PrincessesGenerator:
    """ Генератор результирующих фигур """
    def __init__(self, board_config):
        # Установка конфига доски
        self._load_config(board_config)


    def _load_config(self, config: dict):
        """ Метод для установки конфига доски """
        self.N = config["params"]["N"]
        self.L = config["params"]["L"]

        # Если не указано свободных клеток, считать все клетки свободными, иначе записать клетки из конфига
        if config["free_squares_coords"] is None:
            self.initial_free_squares = set((x,y) for y in range(self.N) for x in range(self.N))
        else:
            self.initial_free_squares = config["free_squares_coords"]

        # Если нет пользовательских фигур, то оставить множество пустым, иначе записать фигуры из конфига
        if config["princesses"]["user_princesses_coords"] is None:
            self.initial_princesses_coords = set()
        else:
            self.initial_princesses_coords = config["princesses"]["user_princesses_coords"]


    def get_free_squares(self, princess_coords: tuple, free_squares: set) -> set:
        """ Метод для получения свободных клеток на основе расставленных фигур и их ходов """
        occupied_squares = get_moves(princess_coords, self.N)
        occupied_squares.add(princess_coords)
        return free_squares.copy() - occupied_squares


    def is_result(self, princesses_coords: set):
        """ Метод для проверки наличия нужного количества расставленных фигур """
        return len(princesses_coords) == self.L - 1


    def start_solving(self, initial_free_squares: Optional[set] = None, princesses_coords: Optional[set] = None) -> set:

        # Если не передано свободных клеток, взять их из конфига
        if initial_free_squares is None:
            initial_free_squares = self.initial_free_squares

        # Если не передано координат фигур, то считать их нераставленными
        if princesses_coords is None:
            princesses_coords = set()

        # Если нужно расставить одну фигуру, то вернуть пустые клетки
        if self.L == 1:
            for free_square in initial_free_squares:
                yield {free_square}
            return

        # Пока есть свободные клетки, алгоритм работает
        while initial_free_squares:
            
            # Получаем любую свободную клетку и ставим в неё фигуру
            root_free_square = initial_free_squares.pop()
            new_princesses_coords = princesses_coords.copy()
            new_princesses_coords.add(root_free_square)


            # Просчитываем свободные клетки
            next_free_squares = self.get_free_squares(root_free_square, initial_free_squares.copy())

            # Если нет свободных клеток и при этом не расставлено нужное количество фигур, то считаем эту ветку тупиковой
            if not next_free_squares and len(new_princesses_coords) < self.L-1:
                continue

            # Если есть решение, то возвращаем его
            if self.is_result(new_princesses_coords.copy()):
                for next_free_square in next_free_squares:
                    result = self.initial_princesses_coords | new_princesses_coords | {next_free_square}
                    yield result
                continue


            # Рекурсивный вызов через yield from для поддержки генератора
            yield from self.start_solving(next_free_squares.copy(), new_princesses_coords.copy())
        return
