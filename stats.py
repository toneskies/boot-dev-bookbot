def get_num_words(book):
    n_words = book.split()
    return len(n_words)

def get_num_letter_count(book):
    dict_letter_count = {}
    book_words = book.split()
    for word in book_words:
        for letter in word:
            if letter in dict_letter_count:
                dict_letter_count[letter] += 1
            else:
                dict_letter_count[letter] = 0
    print(dict_letter_count)
