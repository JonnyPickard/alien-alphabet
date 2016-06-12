def answer(words):
    graph = build_graph(words)

    build_edges(words, graph)


#size of alphabet
def build_graph(words):
    characters = []
    alphabet = {}

    for word in words:
        characters += list(word)

    for char in characters:
        if not any(char in a for a in alphabet):
            alphabet[char] = []

    return alphabet

#compare letters between words to build edges
def build_edges(words, graph):
    graph = graph
    length = len(words)

    for i in range(len(words) -1):
        n = 0
        print i

        while (words[i])[n] == (words[i + 1])[n]:
            n += 1
            print "here"
        else:
            graph[(words[i])[n]] += (words[i + 1])[n]
            n = 0
            print "here now"

    print graph
