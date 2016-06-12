def answer(words):
    return alphabet_size(words)

#build graph
def alphabet_size(words):
    characters = []
    alphabet = []

    for word in words:
        characters += list(word)

    for char in characters:
        if not any(char in a for a in alphabet):
            alphabet += char

    return len(alphabet)
