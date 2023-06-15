
# BFS

Este archivo implementa el algoritmo de búsqueda en amplitud (Breadth-First Search - BFS)
para encontrar un vendedor de mangos en una red de amigos. La red se representa como
un gráfico, y cada persona se considera un nodo. Si el último carácter del nombre de la
persona es 'm', entonces se considera que esa persona es un vendedor de mangos.

## Ejercicio

1. Finding a Path in a Grid using Breadth-First Search (BFS):

Problem Statement:

Given a grid of size n x m, zeros representing open areas and ones representing blocked areas.
You start at the top left corner (0,0) and you want to reach the bottom right corner (n-1, m-1) where n is the number
of rows and m is the number of columns. You can only move right or down.
Write a function that determines whether there's a path from the start to the end.

```python

def is_reachable(grid):
    # implement BFS here
    pass

# Test
grid = [[0, 0, 1, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 1],
        [0, 0, 0, 0]]

print(is_reachable(grid))  # Should print True
```

In this grid, a path is available. So, is_reachable should return True. You can move right two steps, down three steps,
and then right one step to reach the bottom right corner.

The BFS algorithm can be implemented by maintaining a queue of cells to visit and continuously visiting the cell at the
front of the queue as long as there's something in the queue. You should start by adding the start cell to the queue.
In each step, consider the current cell and if it is the destination, return true.
If it's not, add any neighbouring cells which are 0 (unblocked) and not already visited to the queue.

Remember to ensure you don't visit cells multiple times by marking them as visited after they're added to the queue.
You can do this by either modifying the input grid (e.g. setting the cell value to a special value)
or using a separate visited data structure.

If you reach the point where there's nothing left in the queue and you haven't returned true then there's
no possible path, so you should return false.
