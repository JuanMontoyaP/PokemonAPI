import sys

from read_api import read_api
from functions import key_value_json

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
    return url + pokemon_name


def main():
    url = "https://pokeapi.co/api/v2/pokemon/"
    response = read_api(url)

    pokemons = key_value_json(response, 'results')

    print(get_pokemon_features(pokemons))

if __name__ == "__main__":
    main()