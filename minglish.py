from collections import deque

def answer(words):
    graph = build_graph(words)
    graph = build_edges(words, graph)

    return "".join(topological_sort(graph))

#build graph
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
        else:
            graph[(words[i])[n]] += (words[i + 1])[n]
            n = 0

    return graph

def topological_sort(graph):
    degree = { u : 0 for u in graph }
    for u in graph:
        for v in graph[u]:
            degree[v] += 1

    nodes = deque()

    for u in degree:
        if degree[u] == 0:
            nodes.appendleft(u)

    output = []

    while nodes:
        u = nodes.pop()
        output.append(u)
        for v in graph[u]:
            degree[v] -= 1
            if degree[v] == 0:
                nodes.appendleft(v)

    return output
