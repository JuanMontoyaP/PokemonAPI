import sys

def concat_strings(string_list):
    """Return a string resulting from joining a list of strings."""
    return "".join(string_list)

def key_value_json(json_file, key):
    """Returns the key value of a json file."""
    try:
        return json_file[key]
    except KeyError as error:
        print(f'The key: {error} does not exist.')
        sys.exit()


def times_word_in_substring(word: str, substring: str) -> int:
    """Return how many times a substring is in a word."""
    count = 0
    index = -1
    while True: 
        try: 
            index = word.index(substring, index+1)
        except ValueError:
            break

        count += 1
    return count


def word_containing_substring(word: str, substring: str, times: int = 1, max_times: int = None) -> bool:
    """Return True if a word contains a substring n times or between an interval of times, otherwise return False."""
    count_times = times_word_in_substring(word, substring)

    if (max_times):
        if (count_times >= times and count_times <= max_times):
            return True
        else:
            return False
    else :
        if (count_times == times):
            return True
        else:
            return False

def words_containing_substring(words, substring, times, max_times=None):
    """Return a list of filtered words that contains n times a substring or an interval of times."""
    return list(filter(lambda word: word_containing_substring(word, substring, times, max_times), words))


def main():
    print(word_containing_substring("aaa", "a", 1, 3))

if __name__ == '__main__':
    main()