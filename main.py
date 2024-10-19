def main():
   book_path = "books/frankenstein.txt"
   text = read_book(book_path)
   #print(text)
   words= word_count(text)
   print(f"There are {words} in {book_path}.  Below is the breakdown of letters:")
   
   character_count(text)
   


def read_book(path):
    with open("books/frankenstein.txt") as f:
        return f.read()

def word_count(book):
    word_count = []
    words = book.split()
    for word in words:
        word_count.append(word)
    return len(word_count)  


def character_count(book):
    lower_words = book.lower()
    count ={}

    for letter in set(lower_words):
        if letter.isalpha():
            count[letter] = lower_words.count(letter)
    sorted_count = dict(sorted(count.items()))
    
    for key in sorted_count.keys():
        print(f"The letter {key} appears {sorted_count[key]} times.")

    
    

    

main()
        
