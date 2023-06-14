def sum_edge_weights(graph, root):
    # Initialize a set to keep track of visited vertices
    visited = set()

    # Define a recursive helper function to sum edge weights
    def helper(node):
        # Add the current node to the visited set
        visited.add(node)
        # Initialize the total weight to the weights of edges connected to the current node
        total_weight = sum(w for _, w in graph[node] if not visited.__contains__(_))
        # Recursively sum the weights of edges connected to the descendants of the current node
        for v, w in graph[node]:
            if not visited.__contains__(v):
                total_weight += helper(v)
        # Return the total weight
        return total_weight

    # Call the helper function with the root node
    return helper(root)


if __name__ == "__main__":
    graph = {
    0: [(1, 3), (2, 2)],
    1: [(3, 1), (4, 2)],
    2: [(5, 4)],
    3: [],
    4: [(6, 1)],
    5: [],
    6: []
    }
    root = 0
    result = sum_edge_weights(graph, root)
    print(result)
