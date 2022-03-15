from pokemon_features import get_pokemon_url
from read_api import read_api
from functions import key_value_json

def get_pokemon_specie_url(pokemon_name):
    """Retrun the specie url API which the pokemon belongs to"""
    url = get_pokemon_url(pokemon_name)
    
    pokemon = read_api(url)

    pokemon_specie = key_value_json(pokemon, "species")

    return pokemon_specie['url']

def get_egg_group(pokemon_name):
    """Reads a pokemon name and returns a list of dictionary of egg groups that the pokemon belongs to"""
    specie_url = get_pokemon_specie_url(pokemon_name)

    specie = read_api(specie_url)
    
    egg_groups = key_value_json(specie, "egg_groups")

    return egg_groups

def main():
    # pokemon = "raichu"
    # url = get_pokemon_url(pokemon)

    # poke = read_api(url)

    # print(poke.keys())

    # print(poke['name'])

    # print(get_pokemon_specie_url("raichu"))

    print(get_egg_group("raichu"))
    

if __name__ == "__main__":
    main()