def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
def num_words(book_text):
    words = book_text.split()
    return len(words)

def letters_in_book(book_text):
    words = book_text.lower().split()
    word_dict = {}
    for word in words:
        for letter in word:
            if letter in word_dict:
                word_dict[letter] += 1
            else:
                word_dict[letter] = 1
    return word_dict

def sort_on(items):
    return(items["num"])

def sort_dict(dict):
    list = []
    for item in dict:
        new_dict = {
            "char": item,
            "num": dict[item]
        }
        list.append(new_dict)
    list.sort(reverse=True, key=sort_on)
    return list
