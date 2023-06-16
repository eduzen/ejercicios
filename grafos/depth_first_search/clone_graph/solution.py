class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_node(node: Node) -> Node:
    old_to_new = {}

    def dfs_clone(node: Node) -> Node:
        if node in old_to_new:
            return old_to_new[node]

        copy = Node(node.val)
        old_to_new[node] = copy
        for neighbor in node.neighbors:
            copy.neighbors.append(dfs_clone(neighbor))
        return copy

    return dfs_clone(node) if node else None


