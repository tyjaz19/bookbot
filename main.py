def main ():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    text_sorted_list = sort_dict(char_count(text))

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count(text)} words found in the document")
    print("")
    for text in text_sorted_list:
        if text.isalpha():
            print(f"The {text} character was found {char_count(get_book_text(book_path))[text]} times")
    print("")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    indvi_words = text.split()
    return len(indvi_words)

def char_count(book):
    chars = {}
    for c in book:
        lowered_text = c.lower()
        if lowered_text in chars:
            chars[lowered_text] += 1
        else:
            chars[lowered_text] = 1
    return chars
    
def sort_dict(dict):
    dict_list = []
    for i in dict:
        dict_list.append(i)
    dict_list.sort(reverse=False)
    return dict_list
    

main()