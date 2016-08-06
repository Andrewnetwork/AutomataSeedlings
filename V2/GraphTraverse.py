

from GraphMaker import *

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)

    return visited


# Depth first search path frequency.
def DFS_PF( mat ):
    acn = ACN_D(MIT(mat))

    paths = []

    for nodeID in range(2, len(acn) + 1):
        tmp = list(dfs_paths(acn, str(1), str(nodeID)))
        paths.append(tmp)

    pathSizes = []

    for p in paths:
        pathSizes.append(len(p))

    return pathSizes;


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        print( [x.source for x in graph[vertex] ] )
        print(path)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))