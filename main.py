def get_num_words(book):
    return len(book.split())

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the doucment")
    for char in chars_dict:
        print(f"The '{char}' character was found {chars_dict[char]} times")

main()
