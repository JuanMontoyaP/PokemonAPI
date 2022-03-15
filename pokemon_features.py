from functions import key_value_json
from read_api import read_api
import sys

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


def get_pokemon_specie_url(pokemon_name):
    """Retrun the specie url API which the pokemon belongs to"""
    url = get_pokemon_url(pokemon_name)
    
    pokemon = read_api(url)

    pokemon_specie = key_value_json(pokemon, "species")

    return pokemon_specie['url']

def get_egg_group(pokemon_name):
    pass


def main():
    # url = "https://pokeapi.co/api/v2/pokemon/"
    # response = read_api(url)

    # pokemons = key_value_json(response, 'results')

    # print(get_pokemon_features(pokemons))

    # pokemon = "raichu"
    # url = get_pokemon_url(pokemon)

    # poke = read_api(url)

    # print(poke.keys())

    # print(poke['name'])

    print(get_pokemon_specie_url("raichu"))
    

if __name__ == "__main__":
    main()