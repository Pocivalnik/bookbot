def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    

def word_count(text_from_book):
    return len(text_from_book.split())



def main():
    
    #First lesson get the contents of the book 
   
    book_string = get_book_text("books/frankenstein.txt")
    
    
    #Second lesson get the word count of the book 

    number_of_words = word_count(book_string)
    print(f"Found {number_of_words} total words")

main()