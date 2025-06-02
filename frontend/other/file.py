import json 


def write_input_file(values: dict):
    with open("backend/data/input.json", "w") as fp:
        json.dump(values, fp)


def read_input_file():
    with open("backend/data/input.json", "r") as fp:
        values = json.load(fp)
    return values

