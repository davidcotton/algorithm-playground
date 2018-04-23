import argparse
import matplotlib.pyplot as plt
import sys
from time_method import time_method
from graphs.bfs import bfs_search, bfs
from graphs.adjacencylist import AdjacencyListGraph, get_graph
from graphs.dijkstra import dijkstra
from graphs.graph import Vertex, Graph
from typing import List

TIMEOUT = 5

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--steps', type=int, default=20, help='The fibonacci sequence index to calculate to')
    parser.add_argument('--verbose', help='Verbose output', action='store_true')
    args = parser.parse_args()
    steps = args.steps
    verbose = args.verbose

    graph: Graph = get_graph()
    vertices: List[Vertex] = graph.vertices()
    shortest_path = bfs_search(vertices[0], vertices[4])
    print('shortest_path', shortest_path)
    paths = bfs(vertices[0])
    print('paths', paths)

    # algorithms = {}
    # to_skip = []
    # module = sys.modules[__name__]
    # time = 0
    # result = 0
    # for i in range(3, steps + 1):
    #     try:
    #         for fn in algorithms.keys():
    #             if fn not in to_skip:
    #                 _, time, result = time_method(getattr(module, fn), i)
    #                 algorithms[fn].append(time)
    #             if time > TIMEOUT:
    #                 print(f'skipping {fn} with time {time:.4f}')
    #                 to_skip.append(fn)
    #     except AttributeError:
    #         print(f'Method {fn} does not exist')
    #         break
    #     if verbose:
    #         print(f'{i}: {result}')
    #
    # print(f'final iteration time {time:.5f}')
    # plt.title('Search Algorithm Performance')
    # for name, values in algorithms.items():
    #     plt.plot(values)
    # plt.ylabel('time (seconds)')
    # plt.xlabel('steps')
    # plt.legend(algorithms.keys(), loc='upper left')
    # plt.show()
