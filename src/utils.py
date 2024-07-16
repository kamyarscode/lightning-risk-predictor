import json


# Open and parse JSON file for contents.
def open_parse_json(filepath):
    with open(filepath, "r") as f:
        json_file_contents = json.load(f)
    f.close()

    return json_file_contents
