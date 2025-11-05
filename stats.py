def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    

def word_count(text_from_book):
    return len(text_from_book.split())

def count_characters(text_from_book):
    lower_case = text_from_book.lower()
    characters ={}
    for ch in set(lower_case):
        characters[ch] = lower_case.count(ch)
    return characters 