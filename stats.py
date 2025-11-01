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