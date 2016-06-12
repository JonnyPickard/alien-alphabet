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
    count = 0
    length = len(words)

    for i in range(len(words)):
        n = 0
        print i
        print (words[count])[n]

        while i != length -1:
            if (words[count])[n] == (words[count + 1])[n]:
                n += 1
                count += 1
                print "here"
            else:
                graph[(words[count])[n]] += (words[count + 1])[n]
                n = 0
                count += 1
                print "here now"

    print graph
