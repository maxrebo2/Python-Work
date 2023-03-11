def count_common_words(filename, word):
    """Count how many times word appears in the text."""
    # Note : This is a really simple approximation, and the number returned
    # will be higher than the actual count.
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(word)


        msg = f" '{word}' appears in {filename} about {word_count} times." 
        print(msg)


filename = 'alice_in_wonderland.txt'
count_common_words(filename, 'the')


filename = 'anne_of_green_gables.txt'
count_common_words(filename, 'avonlea')


filename = 'moby_dick.txt'
count_common_words(filename, 'whale')