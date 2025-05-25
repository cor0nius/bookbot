from stats import word_count, char_count, sort_dict
import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    print("Usage: python3 main.py <path_to_book>")
    words = word_count(text)
    chars = char_count(text)
    chars = sort_dict(chars)
    print(f"""============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------
Found {words} total words
--------- Character Count -------""")
    for i in range(len(chars)):
        print(chars[i]["char"] + ": " + str(chars[i]["num"]))
    print("============= END ===============")
    
main()