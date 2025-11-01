from stats import count_words

def get_book_text(file_path):
    with open(file_path) as book:
        book_content = book.read()
    return book_content

def main():
    path_to_book = "books/frankenstein.txt"
    text = get_book_text(path_to_book)
    print(f"Found {count_words(text)} total words")

if __name__ == "__main__":  
    main()