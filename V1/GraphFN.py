# GraphFN.py
# Andrew Ribeiro
# July 20, 2016
#    _           _
#   /_\  _ _  __| |_ _ _____ __ __
#  / _ \| ' \/ _` | '_/ -_) V  V /
# /_/ \_\_||_\__,_|_| \___|\_/\_/
#
# Note:
# This software is provided to you on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied.

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from NodeTree import *
import datetime
import itertools
import os



# mapIdentityTopology( MIT )
# Given a binary matrix, number every 1 uniquely.
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


def makePermLists(lenOfList):
    return list(itertools.permutations(range(1,lenOfList+1)))


#all matrix identity combinations.
#Combinatorically explosive.
def AMI(matrix):
    maxRows = matrix.shape[0]
    maxCols = matrix.shape[1]
    uniqueCounter = 0

    #TODO: Find more elegant way.
    for col in range(maxCols):
        for row in range(maxRows):
            if (matrix[row, col] > 0):
                # matrixOut[row, col] = int(idCounter)
                uniqueCounter += 1



    allMatrixOut = []
    perms = makePermLists( uniqueCounter )
    uniqueCounter = 0

    for perm in perms:
        matrixOut = matrix.copy
        for col in range(maxCols):
            for row in range(maxRows):
                if (matrix[row, col] > 0):
                    matrixOut[row, col] = perm[uniqueCounter]
                    uniqueCounter += 1
        allMatrixOut.append(matrixOut)


    return allMatrixOut

#
def adjacentNodes( matrix, location ):

    element = matrix[location]

    row = location[0]
    col = location[1]

    maxRows = matrix.shape[0]
    maxCols = matrix.shape[1]


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


def adjacentNodes_D( matrix, location ):

    element = matrix[location]

    row = location[0]
    col = location[1]

    maxRows = matrix.shape[0]
    maxCols = matrix.shape[1]


    t = set()
    ## Find Adjacency ##

    # Left
    if (col-1) >= 0  and (row-1) >= 0 and matrix[row-1,col-1] > 0:
        # Left Top
        t.add( str(int(matrix[row-1,col-1])) )
    if (col-1) >= 0 and matrix[row,col-1] > 0:
        # Left Middle
        t.add(str(int(matrix[row,col-1] )))
    if (col-1) >= 0 and (row+1) < maxRows and matrix[row+1,col-1] > 0:
        # Left Bottom
        t.add( str(int(matrix[row+1,col-1] ) ))

    # Middle
    if (row-1) >=0 and matrix[row-1,col] > 0:
        # Up
        t.add( str(int(matrix[row-1,col])) )
    if (row+1) < maxRows and matrix[row+1,col] > 0:
        # Down
        t.add( str(int(matrix[row+1,col] )) )

    # Right
    if  (col+1) < maxCols  and (row-1) >= 0 and matrix[row-1,col+1] > 0:
        # Right Top
        t.add( str( int(matrix[row-1,col+1]) ) )
    if  (col+1) < maxCols and matrix[row,col+1] > 0:
        # Right Middle
        t.add( str( int(matrix[row,col+1]) ))
    if (col+1) < maxCols and (row+1) < maxRows and matrix[row+1,col+1] > 0:
        # Right Bottom
        t.add( str( int(matrix[row+1,col+1]) ) )

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

def ACN_D( matrix ):
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
                out[str(int(element))] = adjacentNodes_D(matrix, (row,col))
    return out

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

def generateRandomBinaryMatrix( shape, bits ):
    nRow = shape[0]
    nCol = shape[1]

    outMat = np.zeros(shape)

    for i in range(bits):
        uniqueRandFound = False
        while not uniqueRandFound:
            rRow = np.random.randint(nRow)
            rCol = np.random.randint(nCol)
            if outMat[rRow,rCol] != 1:
                outMat[rRow,rCol] = 1
                uniqueRandFound = True


    return outMat


def generateRandomConnectedBinaryMatrix( shape, bits ):
    nRow = shape[0]
    nCol = shape[1]

    outMat = np.zeros(shape)

    # Start Cell
    rRow = np.random.randint(nRow)
    rCol = np.random.randint(nCol)

    outMat[rRow, rCol] = 1


    for i in range(bits-1):
        uniqueRandFound = False
        while not uniqueRandFound:
            rRow = np.random.randint(nRow)
            rCol = np.random.randint(nCol)

            AN = adjacentNodes(outMat, (rRow,rCol))

            if outMat[rRow,rCol] != 1 and len(AN.children) > 0:
                outMat[rRow,rCol] = 1
                uniqueRandFound = True



    return outMat


# Largest common set SFCAL
# similarFrequencyCountAdjacencyList_LCS
def SFCAL_LCS( fcal1, fcal2 ):

    smallestLEN = len(fcal1)

    if(len(fcal1) >= len(fcal2)):
        len(fcal2)

    return len(lcs(fcal1, fcal2))/ float(smallestLEN)


def lcs(S,T):
    m = len(S)
    n = len(T)
    counter = [[0]*(n+1) for x in range(m+1)]
    longest = 0
    lcs_set = []
    for i in range(m):
        for j in range(n):
            if S[i] == T[j]:
                c = counter[i][j] + 1
                counter[i+1][j+1] = c
                if c > longest:
                    lcs_set = []
                    longest = c
                    lcs_set.append(S[i-c+1:i+1])
                elif c == longest:
                    lcs_set.append(S[i-c+1:i+1])

    return lcs_set[0]

def cropContBinaryMatrix( mat ):
    nRows = mat.shape[0]
    nCols = mat.shape[1]

    # Top Crop
    topRowStart = 0

    for row in range(nRows):
        foundNonEmptyRow = False
        for col in range(nCols):
            if(mat[row,col] != 0 ):
                foundNonEmptyRow = True
                break

        if( foundNonEmptyRow ):
            topRowStart = row
            break
    #TODO Rest

def drawBinMatrix( mat ):
    imgplot = plt.imshow(mat, interpolation="nearest", cmap="hot")
    plt.axis("off")
    win = plt.show()
    raw_input()
    plt.close()

def saveBinMatrixIMG( mat , path, name ):
    imgplot = plt.imshow(mat, interpolation="nearest", cmap="hot")
    plt.axis("off")
    plt.savefig(path+name+'.png')

def traverse( acn, startIndex ):
    return acn[startIndex]

def findNumbering(matrix):
    outMatrix = matrix.copy()

    maxRows = matrix.shape[0]
    maxCols = matrix.shape[1]

    for col in range(maxCols):
        for row in range(maxRows):
            if (matrix[row, col] > 0):
                findNumRec(outMatrix, (row, col), 1)
                return outMatrix


def findNumRec(matrix,startLoc, idCounter=1):
    matrix[startLoc] = -idCounter
    element = matrix[startLoc]

    row = startLoc[0]
    col = startLoc[1]

    maxRows = matrix.shape[0]
    maxCols = matrix.shape[1]

    t = set()
    ## Find Adjacency ##

    # Left
    if (col - 1) >= 0 and (row - 1) >= 0 and matrix[row - 1, col - 1] > 0 :
        # Left Top
        idCounter += 1
        idCounter += findNumRec(matrix,(row - 1, col - 1),idCounter)
    if (col - 1) >= 0 and matrix[row, col - 1] > 0:
        # Left Middle
        idCounter += 1
        idCounter += findNumRec(matrix, (row, col - 1), idCounter)
    if (col - 1) >= 0 and (row + 1) < maxRows and matrix[row + 1, col - 1] > 0:
        # Left Bottom
        idCounter += 1
        idCounter += findNumRec(matrix, (row + 1, col - 1), idCounter)

    # Middle
    if (row - 1) >= 0 and matrix[row - 1, col] > 0:
        # Up
        idCounter += 1
        idCounter += findNumRec(matrix, (row - 1, col), idCounter)
    if (row + 1) < maxRows and matrix[row + 1, col] > 0:
        # Down
        idCounter += 1
        idCounter += findNumRec(matrix, (row + 1, col), idCounter)

    # Right
    if (col + 1) < maxCols and (row - 1) >= 0 and matrix[row - 1, col + 1] > 0:
        # Right Top
        idCounter += 1
        idCounter += findNumRec(matrix, (row - 1, col + 1), idCounter)
    if (col + 1) < maxCols and matrix[row, col + 1] > 0:
        # Right Middle
        idCounter += 1
        idCounter += findNumRec(matrix, (row, col + 1), idCounter)
    if (col + 1) < maxCols and (row + 1) < maxRows and matrix[row + 1, col + 1] > 0:
        # Right Bottom
        idCounter += 1
        idCounter += findNumRec(matrix, (row + 1, col + 1), idCounter)

    print(idCounter)

    return idCounter



def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)

    return visited

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

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