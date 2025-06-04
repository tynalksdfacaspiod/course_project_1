import json 
import os


def cleanup():
    catalog_path = "backend/data"
    files = os.listdir(catalog_path)
    for file in files:
        os.remove(catalog_path + "/" + file)


def write_board_file(params: dict, princesses_coords: dict, moves_coords: dict, free_squares_coords: set):
    data = {
        "params": params,
        "princesses": princesses_coords,
        "moves": moves_coords,
        "free_squares_coords": free_squares_coords
    }

    with open("backend/data/board.json", "w") as fp:
        json.dump(data, fp)


def read_board_file():
    with open("backend/data/board.json", "r") as fp:
        data = json.load(fp)
    
    params = data["params"]
    princesses = data["princesses"]
    moves = data["moves"]
    free_squares_coords = data["free_squares_coords"]

    formatted_data = {
        "params": params,
        "princesses": formatted_coords_dicts(princesses),
        "moves": formatted_coords_dicts(moves),
        "free_squares_coords": formatted_coords(free_squares_coords)
    }

    return formatted_data


def formatted_coords_dicts(data: dict):
    for key, value in data.items(): 
        data[key] = set(map(tuple, value))
    return data 


def formatted_coords(coords):
    return set(map(tuple, coords))


def is_board_config_exists():
    return os.path.exists("backend/data/board.json")
