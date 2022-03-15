def get_pokemon_url(pokemon_name):
    """Returns the url of the pokemon API."""
    url = "https://pokeapi.co/api/v2/pokemon/"
    return url + pokemon_name

def main():
    pokemon = "raichu"
    print(get_pokemon_url(pokemon))

if __name__ == '__main__':
    main()