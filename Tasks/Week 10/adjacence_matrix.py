
def in_degree(k: int, m: list[list[int]]) -> int:
    """
    Calculates the in-degree of node k.
    :param k: Node index
    :param m: Adjacency matrix
    :return: In-degree of node k
    """
    # Sum the k-th column
    return sum(row[k] for row in m)


def out_degree(k: int, m: list[list[int]]) -> int:
    """
    Calculates the out-degree of node k.
    :param k: Node index
    :param m: Adjacency matrix
    :return: Out-degree of node k
    """
    # Sum the k-th row
    return sum(m[k])


def adjacent(k: int, m: list[list[int]]) -> list[int]:
    """
    Finds all adjacent nodes of node k.
    :param k: Node index
    :param m: Adjacency matrix
    :return: List of adjacent nodes
    """
    return [j for j, value in enumerate(m[k]) if value == 1]


def has_triangle(m: list[list[int]]) -> bool:
    """
    Checks if the graph contains any triangles (cycles of length 3).
    :param m: Adjacency matrix
    :return: True if a triangle exists, False otherwise
    """
    n = len(m)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                # Check if i -> j -> k -> i forms a triangle
                if m[i][j] and m[j][k] and m[k][i]:
                    print(f"Triangle found: {i} -> {j} -> {k} -> {i}")
                    return True
    return False


if __name__ == "__main__":
    # Adjacency matrix of the graph
    adjacency_matrix = [
        [0, 1, 0, 0, 1],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
    ]

    # Test in-degree
    print("In-Degree of node 1:", in_degree(1, adjacency_matrix))

    # Test out-degree
    print("Out-Degree of node 1:", out_degree(1, adjacency_matrix))

    # Test adjacent nodes
    print("Adjacent nodes of node 0:", adjacent(0, adjacency_matrix))

    # Test for triangles
    print("Does the graph have a triangle?", has_triangle(adjacency_matrix))
