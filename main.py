def main ():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(word_count(text))
    print(char_count(text))

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
    
main()