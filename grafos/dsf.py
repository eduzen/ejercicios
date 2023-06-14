from rich import print

# Se define el grafo como un diccionario
grafo = {
    'A': ['B', 'F'],
    'B': ['A', 'D', 'C'],
    'C': ['B'],
    'D': ['B', 'E'],
    'E': ['D'],
    'F': ['A', 'G'],
    'G': ['F']
}

# Se define la función para el recorrido en profundidad
def dfs(grafo, nodo_inicial):
    visitados = set()
    stack = [nodo_inicial]

    while stack:
        nodo = stack.pop()
        if nodo not in visitados:
            visitados.add(nodo)
            stack.extend(grafo[nodo] - visitados)
    return visitados

# Llamamos a la función dfs con el grafo y el nodo inicial
print(dfs(grafo, 'A'))
