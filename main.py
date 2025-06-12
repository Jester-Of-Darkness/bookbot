from stats import count_words
from stats import get_chars_report

def get_book_text():
    with open("books/frankenstein.txt") as f:
        book_content = f.read()

    return book_content


book_text = get_book_text()
word_count_result = count_words(book_text)
