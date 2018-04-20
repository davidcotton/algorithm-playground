from graphs.graph import get_graph


class DepthFirstSearch:

    def __init__(self):
        pass

    def visit(self, V, adj, s):
        parent = {'s': None}
        for v in adj[s]:
            if v not in self.parent:
                self.parent[v] = s
                self.visit(V, adj, s)


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
    graph = get_graph()
    search = DepthFirstSearch()
    result = search.visit(graph.get_root(), None, None)
    print(result)
