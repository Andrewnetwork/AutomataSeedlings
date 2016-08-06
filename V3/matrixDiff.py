from GraphFN import *

def matrixDiff(m1, m2):
    m1Sig = matrixSignature(m1)
    m2Sig = matrixSignature(m2)

    print(m1Sig)
    print(m2Sig)

    diff = 0
    match1 = 0
    match2 = 0
    intersect = sorted( list( set(m1Sig).intersection(set(m2Sig)) ) )

    for int in intersect:
        match1 +=  sum( sum( [m1Sig == int] ) )
        match2 +=  sum( sum( [m2Sig == int]) )
        diff += sum( sum( [m1Sig == int] ) ) - sum( sum( [m2Sig == int]) )

    return [diff , (len(m1Sig) - match1) +  (len(m2Sig) - match2) ]


def matrixSignature( mat ):
    graph = ACN_D(MIT(mat))

    nNodes = len(graph)

    topRange = range(1, nNodes + 1)

    innerRange = range(1, nNodes + 1)
    innerRange.pop(0)

    paths = []

    for i in topRange:
        for j in innerRange:
            pathIter = list(dfs_paths(graph, str(i), str(j)))
            for p in pathIter:
                paths.append( len(p) )
        if (len(innerRange) > 0):
            innerRange.pop(0)

    return np.array(sorted(paths))
