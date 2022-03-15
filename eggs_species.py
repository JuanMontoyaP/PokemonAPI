from pokemon_features import get_pokemon_features, get_pokemon_url
from read_api import read_api
from functions import key_value_json, concat_strings

def get_pokemon_specie_url(pokemon_name):
    """Retrun the specie url API which the pokemon belongs to"""
    url = get_pokemon_url(pokemon_name)
    pokemon = read_api(url)
    pokemon_specie = key_value_json(pokemon, "species")
    return pokemon_specie['url']

def get_egg_group(pokemon_name):
    """Reads a pokemon name and returns a list of dictionaries of egg groups that the pokemon belongs to"""
    specie_url = get_pokemon_specie_url(pokemon_name)
    specie = read_api(specie_url)
    egg_groups = key_value_json(specie, "egg_groups")
    egg_groups_names = get_pokemon_features(egg_groups)
    return egg_groups_names

def get_egg_group_url(egg_group):
    """Return the API url of the egg group"""
    url = "https://pokeapi.co/api/v2/egg-group/"
    egg_url = concat_strings([url, egg_group])
    return egg_url

def get_species_per_egg_group(egg_group):
    url = get_egg_group_url(egg_group)
    egg_characteristics = read_api(url)
    egg_species = key_value_json(egg_characteristics, "pokemon_species")
    egg_species_names = get_pokemon_features(egg_species)
    return egg_species_names

def main():
    # pokemon = "raichu"
    # url = get_pokemon_url(pokemon)

    # poke = read_api(url)

    # print(poke.keys())

    # print(poke['name'])

    # print(get_pokemon_specie_url("raichu"))

    print(get_egg_group("raichu"))

    # print(get_species_per_egg_group("monster"))
    

if __name__ == "__main__":
    main()
