def get_char_counts(text):
    text = text.lower()
    char_counts = {}
    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts
def get_num_words(text):
    return len(text.split())
def get_sorted_char_counts(char_counts):
    sorted_list = [
        {"char": char, "num": count}
        for char, count in char_counts.items()
        if char.isalpha()
    ]
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list

