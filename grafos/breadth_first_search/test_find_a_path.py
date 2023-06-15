from finding_a_path import is_reachable


def test_is_reachable():
    grid1 = [
        [0, 0, 1, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 1],
        [0, 0, 0, 0],
    ]
    assert is_reachable(grid1)


def test_is_not_reachable():
    grid2 = [
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 0],
    ]
    assert not is_reachable(grid2)


def test_is_reachable_edge_cases():
    # Test case 3: Only one cell and it is open
    grid3 = [[0]]
    assert is_reachable(grid3)


def test_is_not_reachable_edge_cases():
    # Test case 4: Only one cell and it is blocked
    grid4 = [[1]]
    assert not is_reachable(grid4)
