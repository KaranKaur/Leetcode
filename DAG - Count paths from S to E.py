"""
Given a directed acyclic graph, count the number of ways to go from S to E

"""

def num_paths(G, S, E):
    """
    :type graph, Start Vertex S and End vertex E
    :rtype: int
    """

    if S == E:
        return 1
    else:
        if not S.paths:
            S.paths = sum(num_paths(child, E) for child in S.children)
    return S.paths