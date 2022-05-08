def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # print(f"Sorry, the file {filename} does not exist.")
        pass
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


filenames = ['text_files/alice.txt', 'text_files/Captain_John_Crane.txt', "text_files/The_Devil's_Motor.txt",
             'somewhere.txt']
for filename in filenames:
    count_words(filename)