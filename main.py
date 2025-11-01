from stats import count_words
from stats import count_char
from stats import sorted_char_frequency
from sys import argv
from sys import exit

def get_book_text(file_path):
    with open(file_path) as book:
        book_content = book.read()
    return book_content

def main():

    if  len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    path_to_book = argv[1]

    text = get_book_text(path_to_book)
    num_words = count_words(text)    
    frequency = sorted_char_frequency(count_char(text))
    print_report(path_to_book, num_words, frequency)
    

def print_report(path_to_book, num_words, frequency):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for key in frequency:
        if key["char"].isalpha():
            print(f"{key["char"]}: {key["num"]}")
    print("============= END ===============")

if __name__ == "__main__":  
    main()