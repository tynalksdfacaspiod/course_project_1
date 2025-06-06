import json 
import os


def cleanup():
    """ Функция для очистки файла конфигурации """
    config_path = "backend/data/board.json"
    if is_board_config_exists():
        os.remove(config_path)


def write_board_file(params: dict, princesses_coords: dict, moves_coords: dict, free_squares_coords: set):
    """ Функция для записи конфига доски в файл """

    # Создание датасета
    data = {
        "params": params,
        "princesses": princesses_coords,
        "moves": moves_coords,
        "free_squares_coords": free_squares_coords
    }

    # Запись конфига в файл
    with open("backend/data/board.json", "w") as fp:
        json.dump(data, fp)


def read_board_file() -> dict:
    """ Функция для чтения конфига доски из файла """

    # Чтение конфига из файла
    with open("backend/data/board.json", "r") as fp:
        data = json.load(fp)
    
    # Разделение по переменным
    params = data["params"]
    princesses = data["princesses"]
    moves = data["moves"]
    free_squares_coords = data["free_squares_coords"]

    # Создание датасета с конфигом в нужном формате
    formatted_data = {
        "params": params,
        "princesses": formatted_coords_dicts(princesses),
        "moves": formatted_coords_dicts(moves),
        "free_squares_coords": formatted_coords(free_squares_coords)
    }

    # Возврат конфига
    return formatted_data


def formatted_coords_dicts(data: dict) -> dict:
    """ Функция для форматирования координат в словаре"""
    
    for key, value in data.items(): 
        data[key] = formatted_coords(value)
    return data 


def formatted_coords(coords: list) -> set:
    """ Функция для форматирования координат """
    return set(map(tuple, coords))


def write_results(results: list) -> bool:
    """ Функция для записи результатов в файл """

    with open("backend/data/output.txt", "w") as fp:
        for result in results:
            fp.write(str(result.princesses_coords) + "\n")
    return True


def is_board_config_exists() -> bool:
    """ Функция для проверки наличия конфигурационного файла """ 
    return os.path.exists("backend/data/board.json")
