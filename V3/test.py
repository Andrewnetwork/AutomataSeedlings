# test.py
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


from GraphFN import *
from matrixDiff import *

A_unnamed = np.matrix('0 1 0 0;\
               1 1 1 1;\
               0 1 0 1')

B_unnamed = np.matrix('0 1 1;\
               1 1 0')

A_named = np.matrix('0 2 0 0;\
                     1 3 5 6;\
                     0 4 0 7')

B_named = np.matrix('0 2 4;\
                     1 3 0')

v = [0, 1, 2, 3, 4, 5]
counter = [0, 1, 2, 3, 4, 5]

v[0] = \
        np.matrix('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
                   0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
                   0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
                   0 1 1 1 1 0 0 1 0 0 0 0 0 0 0 0;\
                   0 0 0 0 1 0 0 1 0 0 0 0 0 0 0 0;\
                   0 0 0 0 1 0 0 1 0 0 0 0 0 0 0 0;\
                   0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0;\
                   0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')
v[1] = \
        np.matrix('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
                   0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
                   0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
                   0 0 0 0 0 0 0 0 1 0 0 1 1 1 1 0;\
                   0 0 0 0 0 0 0 0 1 0 0 1 0 0 0 0;\
                   0 0 0 0 0 0 0 0 1 0 0 1 0 0 0 0;\
                   0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0;\
                   0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')

v[2] = \
            np.matrix('0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0;\
                       0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0;\
                       0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0;\
                       0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0;\
                       0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0;\
                       0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0;\
                       0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0;\
                       0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')

v[3] = \
             np.matrix('0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 0;\
                       0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0;\
                       0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0;\
                       0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 0;\
                       0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0;\
                       0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0;\
                       0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0;\
                       0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')
v[4] = \
    np.matrix('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
               0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0;\
               0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0;\
               0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0;\
               0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 0;\
               0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0;\
               0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0;\
               0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 0')

v[5] = \
    np.matrix('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
               0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0;\
               0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0;\
               0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0;\
               0 0 0 0 0 0 0 0 0 0 1 1 1 1 0 0;\
               0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0;\
               0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0;\
               0 0 0 0 0 0 0 0 0 0 1 1 1 1 0 0')

counter[0] = \
    np.matrix('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
               0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0;\
               0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0;\
               0 0 0 0 0 0 1 1 1 0 0 0 0 0 0 0;\
               0 0 0 0 0 0 0 0 1 1 1 0 0 0 0 0;\
               0 0 0 0 0 0 0 0 1 1 1 0 0 0 0 0;\
               0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0;\
               0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')

counter[1] = \
       np.matrix('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
                  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
                  0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0;\
                  0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0;\
                  0 0 0 0 0 0 0 0 0 0 1 1 1 1 0 0;\
                  0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0;\
                  0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0;\
                  0 0 0 0 0 0 0 0 0 0 1 1 1 1 0 0')
counter[2] = \
np.matrix('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
           0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
           0 0 0 0 0 0 0 0 1 1 1 0 1 0 0 0;\
           0 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0;\
           0 0 0 0 0 0 0 0 0 0 1 1 1 0 0 0;\
           0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
           0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
           0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')

counter[3] = \
np.matrix('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
           0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
           0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
           0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
           0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
           0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
           0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
           0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')

counter[4] = \
np.matrix('0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0;\
           0 0 0 0 1 0 0 1 0 0 0 0 0 0 0 0;\
           0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0;\
           0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0;\
           0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
           0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
           0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
           0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')

def simp():
    outMat, nNodes = MIT( v[0] )
    acn, edgeValMat = ACN_D(outMat, nNodes)

    print(outMat)

    tmp = list( dfs_paths(acn, str(1), str(10) ) )

    print(edgeValMat)

    annotatedPath = assignPathWeights(tmp[0], edgeValMat)
    pathWithWeights = annotateWeightedPathVect(annotatedPath ,EDGE_WEIGHTS,LABELD_EDGE_WEIGHTS)
    print("Unlabled Annotated Paths: ",annotatedPath)
    print("Annotated Labeled Paths: ", pathWithWeights )
    print("Weight Signature: ", compressList(annotatedPath,2) )
    print("Annotated Weight Sig: ", compressList(pathWithWeights,2))

def testN1():
    pathSizesCollect = []

    for mat in v:
        outMat,nNodes= MIT(mat)
        acn,edgeValMat = ACN_D(outMat,nNodes)


        print(edgeValMat)

        paths = []

        for nodeID in range(2, len(acn) + 1):
            tmp = list(dfs_paths(acn, str(1), str(nodeID)))
            for path in tmp:
                annotatedPath = assignPathWeights(path, edgeValMat)
                print( "Annotated Paths: ",compressList( annotateWeightedPathVect(annotatedPath ,EDGE_WEIGHTS,LABELD_EDGE_WEIGHTS),2) )

            paths.append(tmp)

        pathSizes = []

        for p in paths:
            pathSizes.append(len(p))

        print(pathSizes);
        pathSizesCollect.append(pathSizes)


def matching(l1,l2):

    match = 0
    for elm1 in l1:
        for elm2 in l2:
            if(elm1 == elm2):
                match+=1

    return float(match)/min(len(l1),len(l2))





def pathSig(mat):
    LABELD_EDGE_WEIGHTS = ["LT", "LM", "LB", "MT", "MB", "RT", "RM", "RB"]
    EDGE_WEIGHTS = [1, 2, 3, 4, 5, 6, 7, 8]

    outMat, nNodes = MIT(mat)
    acn, edgeValMat = ACN_D(outMat, nNodes)

    paths = []
    visited = set()

    for outerNodeID in range(1,len(acn)+1):
        for nodeID in range(2, len(acn) + 1):
            if outerNodeID != nodeID and not( (outerNodeID,nodeID)  in visited ):
                tmp = list(dfs_paths(acn, str(outerNodeID), str(nodeID)))
                for path in tmp:
                    annotatedPath = assignPathWeights(path, edgeValMat)
                    paths.append( compressList(annotateWeightedPathVect(annotatedPath, EDGE_WEIGHTS, LABELD_EDGE_WEIGHTS), 2) )

                visited.add( (outerNodeID,nodeID) )
                visited.add( (nodeID, outerNodeID) )

    return paths

def getSubListsOfLenOrGreater(superList, length):
    nl = []

    for lst in superList:
        if len(lst) >= length:
            nl.append(lst)

    return nl

def identityContinuity(path):
    deriv = []
    prev = path[0]
    prevSwitch = 0

    for elm
    for elm in path:
        if elm == prev:
            deriv.append(prevSwitch)
        else:
            prevSwitch = int(not prevSwitch)
            deriv.append(prevSwitch)

        prev = elm

    return deriv

def listContinuity(path):
    deriv = []
    prev = path[0]
    prevSwitch = 0

    for elm in path:
        if elm == prev:
            deriv.append(prevSwitch)
        else:
            prevSwitch = int(not prevSwitch)
            deriv.append(prevSwitch)

        prev = elm

    return deriv

def testCMP():
    mat1 = v[0]
    mat2 = v[3]

    paths = [[],[]]
    pathCounter = 0

    l = 13
    while l > 2:
        print("========= Length of walk: %i ============" % l)
        for mat in v:
            sig = pathSig(mat)
            listsOfLenL = getSubListsOfLenOrGreater(sig,l)
            print( listsOfLenL )
            print ([listContinuity(x) for x in listsOfLenL] )

        l -= 1

        raw_input("KEEP GOING?")


    #print(matching(pathSig(mat1),pathSig(mat2)))


def randGenTest():

    sig = [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]

    print("Running...")
    while True:
        rand = generateRandomConnectedBinaryMatrix(v[0].shape, 13)

        pSig = pathSig(rand)

        listsOfLenL = getSubListsOfLenOrGreater(pSig,12)

        if( len(listsOfLenL) > 0 ):
            cont = listContinuity(listsOfLenL[0])
            print(cont)
            if cont == sig:
                print(rand)


def longestSublist(lsts):
    longest = []

    for lst in lsts:
        if( len(lst) > len(longest)):
            longest = lst

    return longest

def test34():

    for mat in v:
        sig = pathSig(mat)
        print( longestSublist(sig) )


def test101():

    for mat in v:
        sig = pathSig(mat)
        print( longestSublist(sig) )


test34()
test101()
