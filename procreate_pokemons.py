from eggs_species import get_egg_group, get_species_per_different_groups

def how_many_species_can_procreate(pokemon="raichu"):
    """Return how many species can procreate with a pokemon."""
    egg_group = get_egg_group(pokemon) # Find pokemon's egg groups
    species = get_species_per_different_groups(egg_group)
    return len(species)

def main():
    
    print(how_many_species_can_procreate())

if __name__ == '__main__':
    main()