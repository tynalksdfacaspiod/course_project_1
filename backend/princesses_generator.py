from backend.chess_calculator import get_moves

class PrincessesGenerator:
    def __init__(self, board_config):
        self._load_config(board_config)


    def _load_config(self, config):
        self.N = config["params"]["N"]
        self.L = config["params"]["L"]

        if config["free_squares_coords"] is None:
            self.initial_free_squares = set((x,y) for y in range(self.N) for x in range(self.N))
        else:
            self.initial_free_squares = config["free_squares_coords"]

        if config["princesses"]["user_princesses_coords"] is None:
            self.initial_princesses_coords = set()
        else:
            self.initial_princesses_coords = config["princesses"]["user_princesses_coords"]


    def get_free_squares(self, princess_coords, free_squares):
        occupied_squares = get_moves(princess_coords, self.N)
        occupied_squares.add(princess_coords)
        return free_squares.copy() - occupied_squares


    def is_result(self, princesses_coords):
        return len(princesses_coords) == self.L - 1


    def start_solving(self, initial_free_squares = None, princesses_coords: set = None):

        if initial_free_squares is None:
            initial_free_squares = self.initial_free_squares

        if princesses_coords is None:
            princesses_coords = set()

        if self.L == 1:
            for free_square in initial_free_squares:
                yield {free_square}
            return

        while initial_free_squares:
            root_free_square = initial_free_squares.pop()
            new_princesses_coords = princesses_coords.copy()
            new_princesses_coords.add(root_free_square)


            next_free_squares = self.get_free_squares(root_free_square, initial_free_squares.copy())

            if not next_free_squares and len(new_princesses_coords) < self.L-1:
                continue

            if self.is_result(new_princesses_coords.copy()):
                for next_free_square in next_free_squares:
                    result = self.initial_princesses_coords | new_princesses_coords | {next_free_square}
                    yield result
                continue


            # Рекурсивный вызов через yield from для поддержки генератора
            yield from self.start_solving(next_free_squares.copy(), new_princesses_coords.copy())
        return
