from rich import print

# Grafo como lista de adyacencia
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}

print(grafo)

# Grafo como matriz de adyacencia
grafo = [
    [0, 1, 1, 0, 0, 0],  # A
    [1, 0, 0, 1, 1, 0],  # B
    [1, 0, 0, 0, 0, 1],  # C
    [0, 1, 0, 0, 0, 0],  # D
    [0, 1, 0, 0, 0, 1],  # E
    [0, 0, 1, 0, 1, 0],  # F
]

print(grafo)

graph = """
A -- B -- D -- E
|    |
|    C
|
F -- G
"""

grafo_matrix = [
    [0, 1, 0, 0, 0, 1, 0]  # A
    [1, 0, 1, 1, 0, 0, 0]  # B
    [0, 1, 0, 0, 0, 0, 0]  # C
    [0, 1, 0, 0, 1, 0, 0]  # D
    [0, 0, 0, 1, 0, 0, 0]  # E
    [1, 0, 0, 0, 0, 0, 1]  # F
    [0, 0, 0, 0, 0, 1, 0]  # G
]

grafo = {
    'A': ['B', 'F'],
    'B': ['A', 'D', 'C'],
    'C': ['B'],
    'D': ['B', 'E'],
    'E': ['D'],
    'F': ['A', 'G'],
    'G': ['F']
}

