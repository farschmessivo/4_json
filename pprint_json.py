import json
import sys


def load_data(filepath):
    with open(filepath) as file_handler:
        json_content = json.load(file_handler)
    return json_content


def pretty_print_json(json_content):
    content = json.dumps(json_content, sort_keys=True, indent=4, ensure_ascii=False)
    print(content)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit("Usage: python3 pprint_json.py <path_to_json>")
    filepath = sys.argv[1]
    content = load_data(filepath)
    pretty_print_json(content)
