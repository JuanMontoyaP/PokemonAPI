import sys

from read_api import read_api
from functions import concat_strings, key_value_json, item_in_list
from pokemon_features import get_pokemon_features

def get_pokemon_types(url = "https://pokeapi.co/api/v2/type/"):
    """Get all the pokemon types."""
    return get_pokemon_features(key_value_json(read_api(url), "results"))

def get_url_type(type, url = "https://pokeapi.co/api/v2/type/"):
    """Return the API url of the pokemon type."""
    types = get_pokemon_types()
    try: 
        if (item_in_list(type, types)):
            type_url = concat_strings([url, type])
        else: 
            raise ValueError
    except ValueError as ve:
        print(f'The type: {type} is not valid')
        sys.exit()
    
    return type_url

def get_pokemons_belong_to_type(type="fighting"):
    """Get all the pokemons that belongs to a certain type."""
    url = get_url_type(type)
    pokemons = get_pokemon_features(key_value_json(read_api(url), 'pokemon'), 'pokemon')
    return pokemons

def main():
    # print(get_pokemon_types())
    print(get_pokemons_belong_to_type("fighting"))

if __name__ == '__main__':
    main()