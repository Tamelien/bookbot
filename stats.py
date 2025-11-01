def count_words(text):
    return len(text.split())

def count_char(text):
    char_frequency = {}
    for char in text:
        char = char.lower()

        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1 
    
    return char_frequency

def sort_on(items):
    return items["num"]

def sorted_char_frequency(char_frequency):
    sorted_list = []

    for key in char_frequency:
        sorted_list.append({"char": key, "num": char_frequency[key]})

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list