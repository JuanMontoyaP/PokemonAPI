from count_filter_names import count_filter_names
from procreate_pokemons import how_many_species_can_procreate

def main():
    url = "https://pokeapi.co/api/v2/pokemon/"
    print(count_filter_names(url))

    print(how_many_species_can_procreate())

if __name__ == '__main__':
    main()