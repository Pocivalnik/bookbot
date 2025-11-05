#finds the book in the designated file path and returns it as a string
def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
#splits the book string into a list and returns it's lenght, getting a count of every word 
def word_count(text_from_book):
    return len(text_from_book.split())

#counts all characters in the book string, converts them to lowecase as to not have repeats 
def count_characters(text_from_book):
    counts = {}
    for ch in text_from_book.lower():
        counts[ch] = counts.get(ch, 0) + 1
    return counts


def _by_num(d):
    return d["num"]

def chars_dict_to_sorted_list(count):

    items = [{"char": ch, "num": n} for ch, n in count.items()]
    items.sort(key=_by_num, reverse=True)
    return items