import json 
import os

def cleanup():
    catalog_path = "backend/data"
    files = os.listdir(catalog_path)
    for file in files:
        os.remove(catalog_path + "/" + file)


def write_input_file(values: dict, free_squares_coords):
    data = values.copy()
    data["free_squares_coords"] = tuple(free_squares_coords)
    with open("backend/data/input.json", "w") as fp:
        json.dump(data, fp)


def read_input_file():
    with open("backend/data/input.json", "r") as fp:
        data = json.load(fp)
    return data


def write_board_file(princesses_coords: dict, moves_coords: dict):
    data = {
        "princesses": princesses_coords,
        "moves": moves_coords
    }

    with open("backend/data/board.json", "w") as fp:
        json.dump(data, fp)


def read_board_file():
    with open("backend/data/board.json", "r") as fp:
        data = json.load(fp)
    
    princesses = data["princesses"]
    moves = data["moves"]


    return formatted_data(princesses), formatted_data(moves)


def formatted_data(data: dict):
    for key, value in data.items(): 
        data[key] = set(map(tuple, value))
    return data 


def is_board_file_exists():
    return os.path.exists("backend/data/board.json")
