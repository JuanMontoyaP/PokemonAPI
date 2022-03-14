import sys

def key_value_json(json_file, key):
    """Returns the key value of a json file"""
    try:
        return json_file[key]
    except KeyError as error:
        print(f'The key: {error} does not exist.')
        sys.exit()