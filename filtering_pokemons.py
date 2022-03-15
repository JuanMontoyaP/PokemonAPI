from read_api import read_api
from functions import key_value_json, words_containing_substring
from pokemon_features import get_pokemon_features

def filtering_pokemons_names(pokemons):
    """Return a list of filtered pokemons names that contains 'at' and two 'a' in it."""
    pokemon_names_with_at = words_containing_substring(pokemons, 'at', 1, 2) # If there is more thant two "at" there will be more than two "a"
    pokemon_names_filtered = words_containing_substring(pokemon_names_with_at, 'a', 2)
    return pokemon_names_filtered
    

def main():
    url = "https://pokeapi.co/api/v2/pokemon/"
    response = read_api(url, 0, 1000)

    pokemons = key_value_json(response, 'results')

    pokemon_names = get_pokemon_features(pokemons)

    print(filtering_pokemons_names(pokemon_names))

if __name__ == '__main__':
    main()