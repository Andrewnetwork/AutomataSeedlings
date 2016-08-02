

import numpy as np
from Edge import *

def ACN( matrix ):
    # Itterate through by column.

    maxRows = matrix.shape[0]
    maxCols = matrix.shape[1]

    out = dict()

    for col in range( maxCols ):
        for row in range( maxRows ):

            element = matrix[row,col]

            # Make sure it's not a blank cell"and matrix[row,col] > 0"
            # Add adjacent nodes from top left to bottom right.
            if element > 0:
                ## Find Adjacency ##
                out[str(int(element))] = adjacencyEdges( matrix, (row,col) )
    return out


# AdjacencyEdges
def adjacencyEdges( matrix, location ):

    element = int( matrix[location] )

    row = location[0]
    col = location[1]

    maxRows = matrix.shape[0]
    maxCols = matrix.shape[1]


    t = set()
    ## Find Adjacency ##

    # Left
    if (col-1) >= 0  and (row-1) >= 0 and matrix[row-1,col-1] > 0:
        # Left Top
        t.add( Edge( element, int(matrix[row-1,col-1]), "LT" ) )
    if (col-1) >= 0 and matrix[row,col-1] > 0:
        # Left Middle
        t.add(Edge(element, int(matrix[row,col-1] ), "LM"))
    if (col-1) >= 0 and (row+1) < maxRows and matrix[row+1,col-1] > 0:
        # Left Bottom
        t.add(Edge(element, int(matrix[row+1,col-1] ), "LB"))

    # Middle
    if (row-1) >=0 and matrix[row-1,col] > 0:
        # Up
        t.add(Edge(element, int(matrix[row-1,col]), "MT"))
    if (row+1) < maxRows and matrix[row+1,col] > 0:
        # Down
        t.add(Edge(element, int(matrix[row+1,col] ), "MB"))

    # Right
    if  (col+1) < maxCols  and (row-1) >= 0 and matrix[row-1,col+1] > 0:
        # Right Top
        t.add(Edge(element, int(matrix[row-1,col+1]), "RT"))
    if  (col+1) < maxCols and matrix[row,col+1] > 0:
        # Right Middle
        t.add(Edge(element, int(matrix[row,col+1]), "RM"))
    if (col+1) < maxCols and (row+1) < maxRows and matrix[row+1,col+1] > 0:
        # Right Bottom
        t.add(Edge(element, int(matrix[row+1,col+1]), "RB"))

    return t

def MIT( matrix ):

    maxRows = matrix.shape[0]
    maxCols = matrix.shape[1]

    matrixOut = np.zeros( matrix.shape )

    idCounter = 1

    for col in range(maxCols):
        for row in range(maxRows):
            if(matrix[row,col] > 0):
                matrixOut[row,col] = int(idCounter)
                idCounter += 1

    return matrixOut


def edgeTypeFrequencies( matrix ):
    edges = ACN(MIT(matrix))
    freqCount = dict()

    for weight in EdgeWeights:
        freqCount[weight] = 0

    for elm in edges:
        for edge in edges[elm]:
            freqCount[edge.weight] += 1


    return freqCount

# edgeTypeProportionalityMatrix
def ETPM( matrix ):
    etf = edgeTypeFrequencies(matrix)
    propMatrix = np.zeros((8,8))
    order = ["LT","LM","LB","MT","MB","RT","RM","RB"]

    tc = 0
    sc = 0

    for t in order:
        for s in order:
            if(t == s):
                propMatrix[tc][sc] = etf[t]
            else:
                try:
                    propMatrix[tc][sc] = etf[t]/float(etf[s])
                except:
                    # Division by zero.
                    propMatrix[tc][sc] = None

            sc += 1
        sc = 0
        tc += 1


    return (order,propMatrix)


def graphMaker(matrix):

    edges = ACN( MIT(matrix) )

    return edges


def vectorSimDiff(v1, v2):
    sim = 0
    diff = 0

    for v1E, v2E in zip(v1,v2):
        if v1E == v2E or (np.isnan(v1E) and np.isnan(v2E)):
            sim += 1
        else:
            diff += 1

    return (sim,diff)
