import json 
import os

def cleanup():
    catalog_path = "backend/data"
    files = os.listdir(catalog_path)
    for file in files:
        os.remove(catalog_path + "/" + file)


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

    formatted_data = dict()
    for key, value in data.items():
        formatted_data[key] = set(map(tuple, value))

    return formatted_data.values()


def is_board_file_exists():
    return os.path.exists("backend/data/board.json")
