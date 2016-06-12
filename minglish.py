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
    in_degree = { u : 0 for u in graph }     # determine in-degree
    for u in graph:                          # of each node
        for v in graph[u]:
            in_degree[v] += 1

    Q = deque()                 # collect nodes with zero in-degree
    for u in in_degree:
        if in_degree[u] == 0:
            Q.appendleft(u)

    L = []     # list for order of nodes

    while Q:
        u = Q.pop()          # choose node of zero in-degree
        L.append(u)          # and 'remove' it from graph
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                Q.appendleft(v)

    if len(L) == len(graph):
        return L
    else:                    # if there is a cycle,
        return []
