def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    char_counts(text)
    print("---End report ---")

def sort_on(dict):
    return dict["num"]


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def char_counts(text):
    lowered_string = text.lower()
    resault = {}
    for char in lowered_string:
        if char.isalpha():
            resault[char] = resault.get(char, 0) + 1
    list_of_dicts = [{'char': c, 'num': n} for c, n in resault.items()]
    list_of_dicts.sort(reverse=True, key=sort_on)
    for char in list_of_dicts:
        print(f"The '{char['char']}' character was found {char['num']} times")
    

main()
