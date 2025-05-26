import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)  # Exit with status code 1 (error)

book_path = sys.argv[1]

from stats import get_num_words, get_char_counts, get_sorted_char_counts

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    with open(book_path, "r", encoding="utf-8") as file:
        book_text = file.read()

    num_words = get_num_words(book_text)
    char_counts = get_char_counts(book_text)
    sorted_char_counts = get_sorted_char_counts(char_counts)

    print("=========== BOOKBOT ===========")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_char_counts:
        print(f"{entry['char']}: {entry['num']}")
    print("============ END ===============")

if __name__ == "__main__":
    main()

