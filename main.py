from stats import count_words
from stats import count_char
from stats import sorted_char_frequency

def get_book_text(file_path):
    with open(file_path) as book:
        book_content = book.read()
    return book_content

def main():
    path_to_book = "books/frankenstein.txt"
    text = get_book_text(path_to_book)
    num_words = count_words(text)    
    frequency = sorted_char_frequency(count_char(text))

    print(f"Found {num_words} total words")
    print(f"{frequency}")

if __name__ == "__main__":  
    main()