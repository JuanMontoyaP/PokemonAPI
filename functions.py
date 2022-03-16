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

def unique_items_in_list(my_list):
    """Return a list with the unique elements in a list."""
    return list(set(my_list))

def number_betwen_limits(number: int, min_limit: int, max_limit: int) -> bool:
    """Return True if the number is between the interval (limits included), otherwise return False."""
    if number >= min_limit and number <= max_limit:
        return True
    else:
        return False

def delete_empty_strings_in_list(my_list):
    """Delete empty strings in a list"""
    return list(filter(bool, my_list))

def item_in_list(item, my_list):
    """Return True if the item is in the list, otherwise return False."""
    return item in my_list

def main():
    # print(word_containing_substring("aaa", "a", 1, 3))

    my_list = [1, 2, 3, 4, 5, 5, 5, 5]
    print(unique_items_in_list(my_list))

    print(item_in_list(6, my_list))

if __name__ == '__main__':
    main()