from stats import get_book_text, word_count, count_characters, chars_dict_to_sorted_list
import sys
def main():
    
    if len(sys.argv) != 2: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1] 

    #First lesson get the contents of the book 
   
    book_string = get_book_text(book_path)
    
    
    #Second lesson get the word count of the book 

    number_of_words = word_count(book_string)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"- Found {number_of_words} total words")

    #Third lesson count each character 
    print("--------- Character Count -------")
    numer_of_characters = count_characters(book_string)
    sorted_chars = chars_dict_to_sorted_list(numer_of_characters)

    for item in sorted_chars:
        print(f"- {item['char']}: {item['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()