"""
Este archivo implementa el algoritmo de búsqueda en amplitud (Breadth-First Search - BFS)
para encontrar un vendedor de mangos en una red de amigos. La red se representa como
un gráfico, y cada persona se considera un nodo. Si el último carácter del nombre de la
persona es 'm', entonces se considera que esa persona es un vendedor de mangos.

El algoritmo BFS comienza por el nodo de inicio (en este caso, 'you') y luego explora
los nodos vecinos a un nivel antes de pasar al siguiente nivel.
"""
try:
    from rich import print
except ImportError:
    pass

from collections import deque


def person_is_seller(name: str) -> bool:
    """
    Esta función verifica si una persona es vendedora de mangos.
    Una persona es considerada vendedora de mangos si el último carácter de su nombre es 'm'.
    """
    return name[-1] == 'm'

def breadth_first_search(graph_of_friends: dict[str, str], start: str = None) -> str:
    """Realiza una búsqueda en amplitud en el gráfico de amigos para encontrar un vendedor de mangos.
    Si no se proporciona un valor de inicio, la función utilizará la primera clave del gráfico de amigos.
    """
    if start is None:
        start = next(iter(graph_of_friends))

    search_queue = deque()
    search_queue += graph_of_friends[start]
    searched = set() # This array is how you keep track of which people you’ve searched before.
    while search_queue:  # While the queue isn’t empty ...
        person = search_queue.popleft()  # ... grabs the first person off the queue
        if person in searched:
            continue  # We’ve searched this person before

        if person_is_seller(person):  # Checks whether the person is a mango seller
            print(f"{person} is a mango seller!") # Yes, they’re a mango seller.
            return person
        else:
            search_queue += graph_of_friends[person] # No, they aren’t. Add all of this
            searched.add(person)  # Marks this person as searched
    return None

def breadth_first_search_list(graph_of_friends: dict[str, str], start: str = None) -> str:
    """Realiza una búsqueda en amplitud en el gráfico de amigos para encontrar un vendedor de mangos.
    Si no se proporciona un valor de inicio, la función utilizará la primera clave del gráfico de amigos.
    """
    if start is None:
        start = next(iter(graph_of_friends))

    search_queue = deque()
    search_queue += graph_of_friends[start]
    searched = [] # This array is how you keep track of which people you’ve searched before.
    while search_queue:  # While the queue isn’t empty ...
        person = search_queue.popleft()  # ... grabs the first person off the queue
        if person in searched:
            continue  # We’ve searched this person before

        if person_is_seller(person):  # Checks whether the person is a mango seller
            print(f"{person} is a mango seller!") # Yes, they’re a mango seller.
            return person
        else:
            search_queue += graph_of_friends[person] # No, they aren’t. Add all of this
            searched.append(person)  # Marks this person as searched
    return None


def main() -> None:
    graph_of_friends = {}
    graph_of_friends["you"] = ["alice", "bob", "claire"]
    graph_of_friends["bob"] = ["anuj", "peggy"]
    graph_of_friends["alice"] = ["peggy"]
    graph_of_friends["claire"] = ["thom", "jonny"]
    graph_of_friends["anuj"] = []
    graph_of_friends["peggy"] = []
    graph_of_friends["thom"] = []
    graph_of_friends["jonny"] = []

    print(graph_of_friends)
    person = breadth_first_search(graph_of_friends, "you")
    print(person)
    person = breadth_first_search(graph_of_friends)
    print(person)

if __name__ == "__main__":
    main()
