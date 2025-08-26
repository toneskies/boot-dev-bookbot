def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents



if __name__ == "__main__":
    relative_path = "books/frankenstein.txt"
    text = get_book_text(relative_path)
    print(text)