from stats import get_num_words, get_num_letter_count, get_sorted_dictionaries
import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

if __name__ == "__main__":
    # PART 5: Use sys to take user input for book to read
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    relative_path = sys.argv[1]
    # PART 1: Read the book contents into a string and print it.
    # relative_path = "books/frankenstein.txt"
    text = get_book_text(relative_path)
    # # print(text)
    # # PART 2: Split the string into words and print to console the number of words.
    num_words = get_num_words(text)
    # print(f'{num_words} words found in the document.')
    # # PART 3: Get count of letters in book, print out dictionary.
    letter_count_dict = get_num_letter_count(text)
    # PART 4: Sort Dictionaries and print them out in a list
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f'Found {num_words} total words')
    print("--------- Character Count -------")
    get_sorted_dictionaries(letter_count_dict)
    print("============= END ===============")
