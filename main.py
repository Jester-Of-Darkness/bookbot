import sys
from stats import count_words, get_chars_report


def get_book_text(path_to_book):
    with open(path_to_book) as f:
        book_content = f.read()

    return book_content

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:Python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    word_count_result = count_words(book_text)
    char_report_list = get_chars_report(book_text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count_result} total words")
    print("--------- Character Count -------")
    for item in char_report_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
