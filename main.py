from stats import get_num_words

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

if __name__ == "__main__":
    # PART 1: Read the book contents into a string and print it.
    relative_path = "books/frankenstein.txt"
    text = get_book_text(relative_path)
    # print(text)
    # PART 2: Split the string into words and print to console the number of words.
    num_words = get_num_words(text)
    print(f'{num_words} words found in the document.')