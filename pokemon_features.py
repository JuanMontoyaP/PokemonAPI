from functions import key_value_json
from read_api import read_api
import sys

def get_pokemon_features(pokemons, feature="name"):
    """Return a list of features from different pokemons. Pokemons must be a dictionary or a json"""
    try :
        return [pokemon[feature] for pokemon in pokemons]
    except KeyError as error:
        print(f'The key {error} does not exist in the dictionary.')
        sys.exit()

def main():
    url = "https://pokeapi.co/api/v2/pokemon/"
    response = read_api(url)

    pokemons = key_value_json(response, 'results')

    print(get_pokemon_features(pokemons))

if __name__ == "__main__":
    main()