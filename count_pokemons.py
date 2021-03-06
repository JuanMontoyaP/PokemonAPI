from functions import key_value_json
from read_api import read_api

def total_number_pokemons(json_file, key="count"):
    """Returns the total number of Pokemons. Requires an API json file and the key that contains the total number of pokemons"""
    total_pokemons = key_value_json(json_file, key)
    assert (total_pokemons >= 0 and type(total_pokemons) == int), "Total pokemons must be a positive integer"
    return total_pokemons

def main():
    url = "https://pokeapi.co/api/v2/pokemon/"
    response = read_api(url)
    print(total_number_pokemons(response))

if __name__ == '__main__':
    main()