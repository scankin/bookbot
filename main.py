import sys
from stats import get_book_text, num_words, letters_in_book, sort_dict

def __main__():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print('----------- Word Count ----------')
    word_count = num_words(book_text)
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')
    characters_in_book = letters_in_book(book_text)
    character_count = sort_dict(characters_in_book)
    for i in character_count:
        if i['char'].isalpha():
            print(f'{i["char"]}: {i["num"]}')
        else:
            continue
    print('============= END ===============')


__main__()