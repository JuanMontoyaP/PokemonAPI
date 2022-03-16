from read_api import read_api
from functions import key_value_json

def get_pokemon_weight(url_pokemon):
    pokemon = read_api(url_pokemon)
    return key_value_json(pokemon, "weight")

def main():
    url = "https://pokeapi.co/api/v2/pokemon/1"
    print(get_pokemon_weight(url))

if __name__ == '__main__':
    main()