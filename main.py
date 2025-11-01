from stats import count_words
from stats import count_char

def get_book_text(file_path):
    with open(file_path) as book:
        book_content = book.read()
    return book_content

def main():
    path_to_book = "books/frankenstein.txt"
    text = get_book_text(path_to_book)
    print(f"Found {count_words(text)} total words")
    print(count_char(text))

if __name__ == "__main__":  
    main()