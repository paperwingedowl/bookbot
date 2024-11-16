def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print (f"Preparing report on {f.name}...")
        words = wordcount(file_contents)
        chars = charcount(file_contents)
        print(f"This file has {words} words!")
        
        for letter in chars:
            lcount = chars[letter]
            print(f"{letter}: {lcount} instances")

def wordcount(text):
    wordlist = text.split()
    count = len(wordlist)
    return count

def charcount(text):
    letters = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0
    }

    text = text.lower()

    for char in text:
        if char in letters:
            letters[char] += 1

    return letters

main()