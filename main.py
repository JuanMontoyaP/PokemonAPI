from count_filter_names import count_filter_names
from procreate_pokemons import how_many_species_can_procreate
from pokemon_weight import get_max_min_weight

def main():
    print(count_filter_names()) # This function answer the first question of counting how many pokemons has "at" and two "a" in their names.

    print(how_many_species_can_procreate(pokemon="raichu")) # The second question. This function gets how many species a pokemon can procreate

    print(get_max_min_weight()) # This function gets the max and min weight of a group of pokemons belonging to the same type and and a groups of ids.

if __name__ == '__main__':
    main()