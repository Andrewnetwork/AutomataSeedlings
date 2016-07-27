from GraphFN import *

def matrixSim(m1, m2):
    m1Sig = matrixSignature(m1)
    m2Sig = matrixSignature(m2)

    diff = 0

    intersect = sorted( list( set(m1Sig).intersection(set(m2Sig)) ) )

    for int in intersect:
        diff += np.abs( sum( sum( [m1Sig == int] ) ) - sum( sum( [m2Sig == int]) )  )

    return diff


def matrixSignature( mat ):
    graph = ACN_D(MIT(mat))

    nNodes = len(graph)

    topRange = range(1, nNodes + 1)

    innerRange = range(1, nNodes + 1)
    innerRange.pop(0)

    paths = []

    for i in topRange:
        for j in innerRange:
            paths.append(list(dfs_paths(graph, str(i), str(j))))

        if (len(innerRange) > 0):
            innerRange.pop(0)

    return np.array(sorted([len(x) for x in paths]))