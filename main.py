def get_book_text():
    with open("books/frankenstein.txt") as f:
        book_content = f.read()

    return book_content
    
print(get_book_text())