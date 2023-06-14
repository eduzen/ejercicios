from bsf import breadth_first_search, person_is_seller, breadth_first_search_list
from faker import Faker
import random

fake = Faker()

def random_friend_graph(num_nodes: int) -> dict:
    """Genera un gráfico de amigos aleatorios con el número especificado de nodos."""
    friend_graph = {}
    names = [fake.first_name() for _ in range(num_nodes)]

    for name in names:
        num_friends = random.randint(1, num_nodes)
        friends = random.sample(names, num_friends)
        friends = [friend if friend != name else friend + 'm' for friend in friends]
        friend_graph[name] = friends

    return friend_graph

def test_breadth_first_search():
    graph_of_friends = {
        "you": ["alice", "bob", "claire"],
        "bob": ["anuj", "peggy"],
        "alice": ["peggy"],
        "claire": ["thom", "jonny"],
        "anuj": [],
        "peggy": [],
        "thom": [],
        "jonny": []
    }

    assert breadth_first_search(graph_of_friends, "you") == "thom"
    assert breadth_first_search(graph_of_friends, "bob") == None

def test_person_is_seller():
    assert person_is_seller("thom") == True
    assert person_is_seller("bob") == False


def test_breadth_first_search(benchmark):
    graph_of_friends = random_friend_graph(10000)  # Generate a graph with 10,000 nodes

    # Use the benchmark fixture
    result = benchmark(breadth_first_search, graph_of_friends)

    assert result is not None


def test_breadth_first_search_list(benchmark):
    graph_of_friends = random_friend_graph(10000)  # Generate a graph with 10,000 nodes

    # Use the benchmark fixture
    result = benchmark(breadth_first_search_list, graph_of_friends)

    assert result is not None
