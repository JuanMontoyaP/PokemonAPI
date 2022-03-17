from read_api import read_api
from read_pokemons import read_pokemons
from functions import words_containing_substring, number_betwen_limits, item_in_list
from pokemon_features import get_pokemon_features, get_pokemon_id, get_pokemon_type

def filtering_pokemons_names(pokemons):
    """Return a list of filtered pokemons names that contains 'at' and two 'a' in it."""
    pokemon_names_with_at = words_containing_substring(pokemons, 'at', 1, 2) # If there is more thant two "at" there will be more than two "a"
    pokemon_names_filtered = words_containing_substring(pokemon_names_with_at, 'a', 2)
    return pokemon_names_filtered
    
def filtering_pokemon_id(pokemon_url, min_id, max_id):
    """Filter the pokemons between min_id and max_id."""
    pokemon_id = get_pokemon_id(pokemon_url)
    return number_betwen_limits(pokemon_id, min_id, max_id)

def filter_pokemon_list_id(pokemons_urls, min_id, max_id):
    """Filter a list of pokemons between min_id and max_id."""
    return list(filter(lambda pokemon: filtering_pokemon_id(pokemon, min_id, max_id), pokemons_urls))

def main():
    url = "https://pokeapi.co/api/v2/pokemon/"
    pokemons = read_pokemons(url)

    pokemons_urls = get_pokemon_features(pokemons, 'url')

    # url = ['https://pokeapi.co/api/v2/pokemon/bulbasaur', "https://pokeapi.co/api/v2/pokemon/56"]
    # url1 = "https://pokeapi.co/api/v2/pokemon/56"
    # url2 = ["https://pokeapi.co/api/v2/pokemon/56"]

    # print(filtering_pokemon_id(url, 0, 22))

    # print(pokemons_urls)
    # print(filtering_pokemons_names(pokemons_urls))

    # first_gen_poke = filter_pokemon_list_id(pokemons_urls, 0, 151)

if __name__ == '__main__':
    main()