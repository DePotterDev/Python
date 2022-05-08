filename = 'text_files/The Space Flame.txt'

print("Counting a particular word in a text file.")
with open(filename) as book:
    lines = book.read()
    word = 'flame'
    words = lines.lower().count(word)
    print(f"The word '{word}' counts in the text '{filename}', {words} times.")