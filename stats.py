def sort_on(dict_item):
    return dict_item["num"]

def get_chars_report(text_content):
    character_count = {}
    for char in text_content.lower():
        if char.isalpha():
            if char not in character_count:
                character_count[char] = 1
            else:
                character_count[char] += 1
    report_list = []
    for char, count in character_count.items():
        report_list.append({"char": char, "num": count})
    sorted_report = sorted(report_list, key=sort_on, reverse=True)
    return sorted_report

def count_words():
    from main import get_book_text
    word_list = get_book_text().split()
    word_count = len(word_list)
    return word_count


