def main():
    book = "frankenstein.txt"
    
    file_contents = get_book(book)

    words = count_words(file_contents)

    char_apparitions = count_characters(file_contents)

    print(f"--- Begin report of books/{book} ---")
    print(f"{words} words found in the document")
    for charachter in char_apparitions:
        print(f"The '{charachter}' character was found {char_apparitions[charachter]} times")
    print("--- End report ---")


def get_book(book):
    with open("books/"+book) as f:
        return f.read()
    
def count_words(book):
    return len(book.split())

def count_characters(text):
    apparitions= {}
    alpha = "abcdefghijklmnopqrstuvwxyz"
    string = text.lower()
    for c in alpha:
        apparitions[c] = string.count(c)

    return apparitions




main()

