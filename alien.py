from collections import deque

def answer(words):
    if len(words) == 1: #Guarding against one word dictionaries
        return words[0]

    graph = build_graph(words) #Building nodes of graph
    graph = build_edges(words, graph) #Building edges

    return "".join(topological_sort(graph)) #Sort graph, return formatted output

def build_graph(words):
    characters = []
    graph = {}

    for word in words: #Creating an list of characters from the list of words
        characters += list(word)

    for char in characters: #Creating the graph of one node per unique character
        if not any(char in a for a in graph):
            graph[char] = []

    return graph

def build_edges(words, graph):
    graph = graph

    length = len(words)

    for i in range(length -1): #Iterating over the words list
        a = words[i]
        b = words[i+1]

        min_length = min(len(a), len(b))

        for n in range(min_length): #Comparing word n with word n + 1 for mistmatched characters
            if a[n] != b[n]:
                graph[a[n]] += b[n] #Creating edges with the mistmatched characters
                break

    return graph

def topological_sort(graph): #Peforming a topological sort sort of the graph
    degree = { u : 0 for u in graph }
    for u in graph:
        for v in graph[u]:
            degree[v] += 1 #Finding vertices

    nodes = deque()

    for u in degree: #Appending 0 vertex nodes
        if degree[u] == 0:
            nodes.appendleft(u)

    output = []

    while nodes:
        u = nodes.pop() #Putting 0 vertex nodes onto output
        output.append(u)
        for v in graph[u]: #Find edge
            degree[v] -= 1 #Minus route taken
            if degree[v] == 0: #Append if possible routes remaining == 0
                nodes.appendleft(v)

    return output
