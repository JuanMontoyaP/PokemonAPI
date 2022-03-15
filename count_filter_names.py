from read_pokemons import read_pokemons
from filtering_pokemons import get_pokemon_features, filtering_pokemons_names

def count_filter_names(url):
    """Count the number of names that have 'at' and two 'a's"""
    
    pokemons = read_pokemons(url)
    
    pokemon_names = get_pokemon_features(pokemons, feature="name") # Get all the pokemon names 

    filtered_names = filtering_pokemons_names(pokemon_names) # Filter all the names 

    return len(filtered_names)

def main():
    url = "https://pokeapi.co/api/v2/pokemon/"
    print(count_filter_names(url))

if __name__ == '__main__':
    main()