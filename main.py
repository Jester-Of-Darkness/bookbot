from stats import count_words

def get_book_text():
    with open("books/frankenstein.txt") as f:
        book_content = f.read()

    return book_content

if __name__ == "__main__":
    print(f"{count_words()} words found in the document")