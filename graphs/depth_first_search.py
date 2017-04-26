from . import graphs


class DepthFirstSearch:

    def __init__(self):
        pass

    def visit(self, V, adj, s):
        parent = {'s': None}
        for v in adj[s]:
            if v not in self.parent:
                self.parent[v] = s
                self.visit(V, adj, s)


if __name__ == '__main__':
    graph = graphs.get_graph()
    search = DepthFirstSearch()
    result = search.visit(graph.get_root(), None, None)
    print(result)
