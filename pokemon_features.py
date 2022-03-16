import sys

from read_api import read_api
from functions import key_value_json, concat_strings, delete_empty_strings_in_list

def get_pokemon_features(pokemons, feature="name"):
    """Return a list of features from different pokemons. Pokemons must be a dictionary list"""
    try :
        return [pokemon[feature] for pokemon in pokemons]
    except KeyError as error:
        print(f'The key {error} does not exist in the dictionary.')
        sys.exit()

def get_pokemon_url(pokemon_name):
    """Returns the url of the pokemon API."""
    url = "https://pokeapi.co/api/v2/pokemon/"
    pokemon_url = concat_strings([url, pokemon_name])
    return pokemon_url

def get_pokemon_id(pokemon_url):
    """Get the pokemon ID with the pokemon url"""
    split_url = pokemon_url.split(sep='/')
    split_url = delete_empty_strings_in_list(split_url)

    if (split_url[-1].isalpha()):
        pokemon = read_api(pokemon_url)
        return key_value_json(pokemon, "id")
    elif (split_url[-1].isnumeric()):
        return int(split_url[-1])

def get_pokemon_type(pokemon_url):
    """Get the pokemon type from the pokemon API url."""
    pokemon = read_api(pokemon_url)
    
    pokemon_types = get_pokemon_features(key_value_json(pokemon, "types"), "type")
    pokemon_types_names = get_pokemon_features(pokemon_types)
    return pokemon_types_names

def main():
    # url = "https://pokeapi.co/api/v2/pokemon/"
    # response = read_api(url)

    # pokemons = key_value_json(response, 'results')

    # # print(get_pokemon_features(pokemons))

    # # print(get_pokemon_url("raichu"))

    # print(get_pokemon_id(get_pokemon_url("bulbasaur")))
    # print(get_pokemon_id(get_pokemon_url("1")))

    url = "https://pokeapi.co/api/v2/pokemon/56/"
    print(get_pokemon_type(url))

if __name__ == "__main__":
    main()