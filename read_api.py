import requests

def read_api(url, offset=0, limit=20):
    """This function returns the content of an API that uses query parameters offset and limit"""

    args = {"offset": offset, "limit": limit}
    try: 
        response = requests.get(url, params=args)
        response.raise_for_status()
    except requests.exceptions.HTTPError as error:
        print(error)

    return response.content

def main():
    url = "https://pokeapi.co/api/v2/pokemon/"
    print(read_api(url, 0, 1))

    url = "https://pokeapi.co/api/v2/pokemon/"
    print(read_api(url, 0, 1000))

    url = "https://pokeapi.co/api/v2/pokemon234234/"
    read_api(url, 0, 5)

    url = "https://pokeapi.co/api/v2/pokemon/"
    print(read_api(url, 0, 10))


if __name__ == '__main__':
    main()