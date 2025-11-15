from stats import count_num_words, get_num_times_in_string, sort_dict
import sys

def get_book_text(filepath) -> str:
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_contents = get_book_text(sys.argv[1])
    num_words = count_num_words(file_contents)
    num_times_in_string = get_num_times_in_string(file_contents)
    sorted_dict = sort_dict(num_times_in_string)

    print()
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for char_count in sorted_dict:
        print(f"{char_count["char"]}: {char_count["num"]}")

    print("============= END ===============")

main()