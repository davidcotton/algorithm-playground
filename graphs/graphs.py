class AdjacencyListArray:
    def __init__(self, data):
        if len(data):
            for d in data:
                self.add_vertex(d)
        else:
            self.vertices = []

    def vertices(self):
        """Get all vertices."""
        return self.vertices

    def edges(self):
        """Get all edges."""
        edges = []
        for v in self.vertices:
            edges.append(v)
        return edges

    def add_vertex(self, v):
        """Insert a vertex v."""
        self.vertices.append(v)

    def remove_vertex(self, v):
        """Remove a vertex v and it's incident edges."""
        for vertex in self.vertices:
            if v == vertex:
                self.vertices.remove(v)

    def are_adjacent(self, v, w):
        """True if v and w are adjacent.

        Args:
            v: The first vertex to check
            w: The second vertex to check
        """
        return False

    def add_edge(self, e, v, w):
        """Insert an edge.

            Args:
                e: The edge to insert.
                v: The first vertex the edge is connected to
                w: The second vertex the edge is connected to
        """
        pass

    def remove_edge(self, e):
        """Remove an edge."""
        pass


def get_graph():
    graph = AdjacencyListArray([[1, 2], [2, 3], [4], [4, 5], [5], []])
    return graph
