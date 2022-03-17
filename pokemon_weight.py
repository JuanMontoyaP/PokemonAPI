from read_api import read_api
from functions import key_value_json, max_min_in_list
from pokemon_types import get_pokemons_belong_to_type
from pokemon_features import get_pokemon_features
from filtering_pokemons import filter_pokemon_list_id

def get_pokemon_weight(url_pokemon):
    pokemon = read_api(url_pokemon)
    return key_value_json(pokemon, "weight")

def get_pokemon_weights_list(urls_pokemon):
    """Return a list of the weights of the pokemons"""
    return list(map(get_pokemon_weight, urls_pokemon))

def get_max_min_weight(type="fighting", min_id=0, max_id=151):
    """Get max and min weight for a group of pokemons (pokemon type and its id)"""
    same_type_pokemons = get_pokemons_belong_to_type(type)
    same_type_pokemons_urls = get_pokemon_features(same_type_pokemons, 'url')
    same_type_id = filter_pokemon_list_id(same_type_pokemons_urls, min_id, max_id)
    weights = get_pokemon_weights_list(same_type_id)
    return list(max_min_in_list(weights))

def main():
    url = "https://pokeapi.co/api/v2/pokemon/1"
    print(get_pokemon_weight(url))

    print(get_max_min_weight())

if __name__ == '__main__':
    main()