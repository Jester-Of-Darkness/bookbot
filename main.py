from stats import count_words
from stats import get_chars_report

def get_book_text():
    with open("books/frankenstein.txt") as f:
        book_content = f.read()

    return book_content

if __name__ == "__main__":
    book_text = get_book_text()
    word_count_result = count_words()
    char_report_list = get_chars_report(book_text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count_result} total words")
    print("--------- Character Count -------")
    for item in char_report_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
