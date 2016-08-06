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
import itertools

from matDFS import *
from graphHelpers import *


#Psudo Enum
LABELD_EDGE_WEIGHTS = ["LT","LM","LB","MT","MB","RT","RM","RB"]
EDGE_WEIGHTS        = [   1,   2,   3,   4,   5,   6,   7,   8]





# Flips adjacent nodes that are out of place.
def verifyWalk(walkIn,acnDict):
    walk = list(walkIn)
    walkLen = len(walk)
    walkPos = 0
    changed = False

    while walkPos+1 < walkLen:
        # Swap positions if this walk doesn't belong
        if not ( walk[walkPos] in acnDict[walk[walkPos+1]] ):
            #print(walk, walk[walkPos], acnDict[walk[walkPos + 1]])
            tmp = walk[walkPos-1]
            walk[walkPos-1] = walk[walkPos]
            walk[walkPos] = tmp

        walkPos += 1

    return walk

def longestPath(mat,nNodes):
    acn, edgeValMat = ACN_D(mat, nNodes)

    for pos in range(1,nNodes):

        walk = matDFS(mat,nNodes,pos,acn,edgeValMat)[0]
        print(walk)
        #print(connectedSubWalks(walk,acn) )
        #raw_input("E")

        if(connectedWalk(walk,acn)):
            return walk

    return None

def connectedSubWalks(walkIn,acnDict):
    walk = list(walkIn)
    walkLen = len(walk)
    walkPos = 0

    nodeQueue = []
    subConnected = []

    while walkPos + 1 < walkLen:
        if not (walk[walkPos] in acnDict[walk[walkPos + 1]]):
            nodeQueue.append(walk[walkPos])
            subConnected.append(nodeQueue)
            nodeQueue = []
        else:
            nodeQueue.append(walk[walkPos])


        walkPos += 1

    return subConnected

def connectedWalk(walkIn,acnDict):
    walk = list(walkIn)
    walkLen = len(walk)
    walkPos = 0

    while walkPos + 1 < walkLen:
        if not (walk[walkPos] in acnDict[walk[walkPos + 1]]):
          return False

        walkPos+=1

    return True



