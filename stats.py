def get_num_words(book):
    n_words = book.split()
    return len(n_words)

def get_num_letter_count(book):
    dict_letter_count = {}
    book_words = book.split()
    for word in book_words:
        for letter in word:
            if letter.lower() in dict_letter_count:
                dict_letter_count[letter.lower()] += 1
            else:
                dict_letter_count[letter.lower()] = 1
    return dict_letter_count

def sort_on(items):
    return items["num"]

def get_sorted_dictionaries(dict):
    list_of_dicts = []
    for key, value in dict.items():
        dict_to_add = {"char": key, "num": value}
        list_of_dicts.append(dict_to_add)
        list_of_dicts.sort(reverse=True, key=sort_on)
    for dict in list_of_dicts:
        if dict["char"].isalpha():
            print(f'{dict["char"]}: {dict["num"]}')
            