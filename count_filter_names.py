from read_api import read_api
from count_pokemons import total_number_pokemons
from functions import key_value_json
from filtering_pokemons import get_pokemon_features, filtering_pokemons_names

def count_filter_names(url):
    """Count the number of names that have 'at' and two 'a's"""
    content = read_api(url)
    total_pokemons = total_number_pokemons(content)

    content = read_api(url, 0, total_pokemons) # Updates the API for reading all the pokemons at once
    
    pokemons = key_value_json(content, 'results') # Get pokemons from API 
    pokemon_names = get_pokemon_features(pokemons, feature="name") # Get all the pokemon names 

    filtered_names = filtering_pokemons_names(pokemon_names) # Filter all the names 

    return len(filtered_names)

def main():
    url = "https://pokeapi.co/api/v2/pokemon/"
    print(count_filter_names(url))

if __name__ == '__main__':
    main()