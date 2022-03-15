from count_filter_names import count_filter_names

def main():
    url = "https://pokeapi.co/api/v2/pokemon/"
    print(count_filter_names(url))

if __name__ == '__main__':
    main()