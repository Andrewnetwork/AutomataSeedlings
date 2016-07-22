import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from NodeTree import *

# mapIdentityTopology( MIT )
def MIT( matrix ):

    maxRows = matrix.shape[0]
    maxCols = matrix.shape[1]

    matrixOut = np.zeros( matrix.shape )

    idCounter = 1

    for col in range(maxCols):
        for row in range(maxRows):
            if(matrix(row,col) > 0):
                matrixOut[row,col] = idCounter
                idCounter += 1

    return matrixOut


def walkMatrix( matrix ,parentRow,parentCol, location):
    t = matrix[location]

    print( matrix[location] )

    return t

def adjacentNodes( matrix, location ):

    element = matrix[location]

    row = location[0]
    col = location[1]

    maxRows = matrix.shape[0]
    maxCols = matrix.shape[1]

    if element > 0:
        t = Node( element )
        ## Find Adjacency ##

        # Left
        if (col-1) >= 0  and (row-1) >= 0 and matrix[row-1,col-1] > 0:
            # Left Top
            t.addChild( matrix[row-1,col-1] )
        if (col-1) >= 0 and matrix[row,col-1] > 0:
            # Left Middle
            t.addChild( matrix[row,col-1] )
        if (col-1) >= 0 and (row+1) < maxRows and matrix[row+1,col-1] > 0:
            # Left Bottom
            t.addChild( matrix[row+1,col-1] )

        # Middle
        if (row-1) >=0 and matrix[row-1,col] > 0:
            # Up
            t.addChild( matrix[row-1,col] )
        if (row+1) < maxRows and matrix[row+1,col] > 0:
            # Down
            t.addChild( matrix[row+1,col] )

        # Right
        if  (col+1) < maxCols  and (row-1) >= 0 and matrix[row-1,col+1] > 0:
            # Right Top
            t.addChild( matrix[row-1,col+1] )
        if  (col+1) < maxCols and matrix[row,col+1] > 0:
            # Right Middle
            t.addChild( matrix[row,col+1] )
        if (col+1) < maxCols and (row+1) < maxRows and matrix[row+1,col+1] > 0:
            # Right Bottom
            t.addChild( matrix[row+1,col+1] )

        return t


# adjacencyConnectedNodes (ACN)
def ACN( matrix ):
    # Itterate through by column.

    maxRows = matrix.shape[0]
    maxCols = matrix.shape[1]

    nodes = []

    for col in range( maxCols ):
        for row in range( maxRows ):

            element = matrix[row,col]

            # Make sure it's not a blank cell"and matrix[row,col] > 0"
            # Add adjacent nodes from top left to bottom right.
            if element > 0:
                ## Find Adjacency ##
                nodes.append( adjacentNodes(matrix, (row,col)) )

    return nodes

# freqCountAdjacencyList( FCAL )
def FCAL( lst ):
    freqList = []

    for node in lst:
        freqList.append( len( node.children) )

    return freqList

# similarFrequencyCountAdjacencyList_Naive
def SFCAL_N( fcal1, fcal2 ):
    smallestLEN = len(fcal1)
    freq        = 0

    if(len(fcal1) >= len(fcal2)):
        len(fcal2)

    for idx in range(smallestLEN):
        if( fcal1[idx] == fcal2[idx] ):
            freq += 1.0

    return freq / smallestLEN



