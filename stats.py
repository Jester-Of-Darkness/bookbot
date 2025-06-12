def count_words():
    from main import get_book_text
    word_list = get_book_text().split()
    word_count = len(word_list)
    return word_count
