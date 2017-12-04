import json
import sys
from pprint import pprint


def load_data(filepath):
    with open(filepath) as file_handler:
        shops_list = json.load(file_handler)
    return shops_list


def pretty_print_json(shops_list):
    pprint(shops_list)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit("Usage: python3 pprint_json.py <path_to_json>")
    filepath = sys.argv[1]
    sjson = load_data(filepath)
    pretty_print_json(sjson)
