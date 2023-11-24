graph = {
    "a": ["c", "b"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}


def depthFirstPrint(graph, source):
    stack = [source]  # Start with the source node

    final_graph = []
    print(stack)

    while len(stack) > 0:
        current = stack.pop()
        print(f"Neighbors of {current} are: {graph[current]}")
        final_graph.append(current)

        # Add neighbors to the stack:
        for neighbors in graph[current]:
            stack.append(neighbors)

        # # Alternative methods:
        # stack.extend(graph[current])

    print(final_graph)


# Call the function with the correct source node
depthFirstPrint(graph, "a")
