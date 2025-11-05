def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    

def word_count(text_from_book):
    return len(text_from_book.split())
