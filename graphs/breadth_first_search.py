# from graphs import get_graph
# from .graphs import get_graph
from .graphs import AdjacencyListArray


# def bfs(g, v):
#     label v as discovered
#     q = Queue()
#     q.push(v)
#
#     while q is not empty:
#         v = q.pop()
#         if v is not discovered:
#             label v as discovered
#
#         for all e in g.adjacent_edges(v):
#             v = g.adjacent_vertex(g, e):
#             if v is not discovered:
#                 label v as discovered
#                 q.push(v)

def bfs(adj, s):
    """Breadth-first Search.
    Returns a tree describing every vertex that is reachable from the source vertex.

    Args:
        adj: The adjacency list to search
        s: The source vertex

    Returns: {}
    """
    level = {s: []}
    parent = {s: None}
    i = 1
    frontier = [s]
    while frontier:
        nxt = []
        for u in frontier:
            for v in adj[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    nxt.append(v)
        frontier = nxt
        i += 1
    return parent


def dfs(adj, vertices):
    parent = {}
    for s in vertices:
        if s not in parent:
            parent[s] = dfs_visit(adj, s)
    return parent


def dfs_visit(adj, s):
    """Depth-first Search.
    Returns a tree describing every vertex that is reachable from the source vertex.

        Args:
            adj: The adjacency list to search
            s: The source vertex

        Returns: {}
        """
    parent = {s: None}
    for v in adj[s]:
        if v not in parent:
            parent[v] = s
            dfs(adj, v)
    return parent


if __name__ == '__main__':
    # graph = get_graph()
    graph = AdjacencyListArray([[1, 2], [2, 3], [4], [4, 5], [5], []])
    result_bfs = bfs(graph, [1, 2])
    print('result_bfs: {}'.format(result_bfs))
    # result_dfs = dfs(graph, [1, 2])
    # print('result_dfs: {}'.format(result_dfs))
