import json 


def write_input_file(values: dict):
    with open("backend/data/input.json", "w") as fp:
        json.dump(values, fp)


def read_input_file():
    with open("backend/data/input.json", "r") as fp:
        values = json.load(fp)
    return values


def write_board_file(princesses_coords: set, moves_coords: set):
    data = {
        "princesses": princesses_coords,
        "moves": moves_coords
    }
    with open("backend/data/board.json", "w") as fp:
        json.dump(data, fp)


def read_board_file():
    with open("backend/data/board.json", "r") as fp:
        data = json.load(fp)
    return data.values()
