from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __eq__(self, node: object) -> bool:
        return self.val == node.val and self.neighbors == node.neighbors

    def __repr__(self) -> str:
        return f'Node(val={self.val}, neighbors={self.neighbors})'


class Graph:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, neighbors: list[list[int, int]]) -> 'Node':
        if node is None:
            return node

        return self.dfs(node)

    def dfs(self, node: 'Node') -> 'Node':
        if node in self.visited:
            return self.visited[node]

        clone = Node(node.val, [])
        self.visited[node] = clone

        for neighbor in node.neighbors:
            clone.neighbors.append(self.dfs(neighbor))

        return clone


def main() -> None:
    adjList = [[2,4],[1,3],[2,4],[1,3]]
    graph = Graph()
    cloned_graph = graph.cloneGraph(adjList)

    assert cloned_graph == [[2,4],[1,3],[2,4],[1,3]], f'output={cloned_graph}'
    print('Accepted')

if __name__ == '__main__':
    main()
