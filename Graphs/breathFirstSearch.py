graph = {
    "a": ["c", "b"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}

# Hello
def breathFirstSearch(graph, source):
    queue = [source]
    breath_search = []
    while len(queue) > 0:
        current = queue.pop(0)
        print(f"Neighbors of {current} are: {graph[current]}")
        breath_search.append(current)

        # # Add neighbors to the queue
        # queue.extend(graph[current])

        # Alternative method:
        for neighbors in graph[current]:
            queue.append(neighbors)
    print(breath_search)


breathFirstSearch(graph, "a")
