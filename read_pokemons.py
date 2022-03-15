from read_api import read_api
from count_pokemons import total_number_pokemons
from functions import key_value_json

def read_pokemons(url):
    content = read_api(url)
    total_pokemons = total_number_pokemons(content)

    content = read_api(url, 0, total_pokemons) # Updates the API for reading all the pokemons at once
    pokemons = key_value_json(content, 'results') # Get pokemons from API 
    return pokemons


def main():
    url = "https://pokeapi.co/api/v2/pokemon/"
    print(read_pokemons(url))

if __name__ == '__main__':
    main()