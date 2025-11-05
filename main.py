from stats import get_book_text
from stats import word_count
from stats import count_characters
def main():
    
    #First lesson get the contents of the book 
   
    book_string = get_book_text("books/frankenstein.txt")
    
    
    #Second lesson get the word count of the book 

    number_of_words = word_count(book_string)
    print(f"Found {number_of_words} total words")

    #Third lesson count each character 

    numer_of_characters = count_characters(book_string)
    print(numer_of_characters)
main()