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
counter = range(0,100)

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
           0 0 0 0 1 0 0 1 0 0 0 0 0 0 0 0;\
           0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0;\
           0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
           0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
           0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
           0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')

counter[5] = \
np.matrix('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
           0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0;\
           0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0;\
           0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0;\
           0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0;\
           0 0 0 0 0 0 1 1 1 0 0 0 0 0 0 0;\
           0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
           0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')

counter[6] = \
np.matrix('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
           0 0 0 0 1 1 1 1 1 1 0 0 0 0 0 0;\
           0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 0;\
           0 0 0 0 1 1 1 0 0 1 0 0 0 1 1 0;\
           0 0 0 0 0 0 1 0 0 1 0 0 0 1 1 0;\
           0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 0;\
           0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0;\
           0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')

counter[7] = \
     np.matrix('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
                0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
                0 0 0 0 0 1 1 0 0 1 1 0 0 0 0 0;\
                0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0;\
                0 0 0 0 0 1 1 0 0 1 1 0 0 0 0 0;\
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



def test34():

    for mat in v:
        sig = pathSig(mat)
        print( longestSublist(sig) )


def test101():

    for mat in v:
        sig = pathSig(mat)
        long = longestSublist(sig)
        print( identityContinuity(long), listContinuity(identityContinuity(long)) )


def test304():
    long1 = longestSublist(pathSig(v[0]))
    long2 = longestSublist(pathSig(counter[5]))

    print(long1,listContinuity(long1))
    print(long2,listContinuity(long2))

    print(simContinuity(listContinuity(long1),listContinuity(long2)))


def dfsTest():
    outMat, nNodes = MIT(v[0])
    acn, edgeValMat = ACN_D(outMat, nNodes)
    lst = []
    print(outMat)
    print( dfs(acn,str(1),set(),lst) )
    print(lst)


def test933():
    outMat, nNodes = MIT(v[0])
    acn, edgeValMat1 = ACN_D(outMat, nNodes)

    print(edgeValMat1)

    outMat, nNodes = MIT(v[1])
    acn, edgeValMat2 = ACN_D(outMat, nNodes)

    outMat, nNodes = MIT(v[2])
    acn, edgeValMat3 = ACN_D(outMat, nNodes)




def testBestFromThisPoint():
    #MIT: Takes in a binary matrix and returns a matrix with a unique id for every position that has a 1.
    #also returns number of unique nodes.
    outMat, nNodes = MIT(v[2])

    print(outMat)

    # Matrix dfs. Given:
    # MIT matrix
    # number of unique nodes,
    # and our starting position.
    # We get:
    # A DFS walk ( which can be discontinuous )
    # An ajacency connected nodes dictionary.
    # A matrix describing the weights between all nodes.
    walk,acn,edgeVals = matDFS(outMat, nNodes, 9)

    print(walk)
    #The walk we get back from DFS may be discontinuous. Fix discontinuities in the walk
    #making the good walk = the longest path.
    goodWalk = verifyWalk(walk,acn)

    print(goodWalk)
    # Assign weights to the paths
    weightedPath = assignPathWeights(goodWalk,edgeVals)
    print(weightedPath)

    #Getting only the edge weights that characterize the walk.
    weights = compressList(annotateWeightedPathVect(weightedPath,EDGE_WEIGHTS,LABELD_EDGE_WEIGHTS), 2)
    print( weights )

    print( listContinuity(weights) )

    print( identityContinuity(weights) )

def testCompareVMat():
    for mat in v:
        outMat, nNodes = MIT(mat)
        walk, acn, edgeVals = matDFS(outMat, nNodes, 1)
        goodWalk = verifyWalk(walk, acn)
        weightedPath = assignPathWeights(goodWalk, edgeVals)
        weights = compressList(annotateWeightedPathVect(weightedPath, EDGE_WEIGHTS, LABELD_EDGE_WEIGHTS), 2)

        print(listContinuity(weights))
        print(identityContinuity(weights))


def longestPathTest():

    for elm in range(7):
        v.append( counter[elm] )

    for mat in v:
        outMat, nNodes = MIT(mat)
        print(outMat)
        print( longestPath(outMat,nNodes) )


def longestPathTest2():
    outMat, nNodes = MIT(counter[6])
    print(outMat)
    print(longestPath(outMat, nNodes))


def pathSigTest():
    #print([17, 16, 15, 14, 12, 10, 6, 4, 1, 2, 3, 5, 7, 8, 9, 11, 13, 18, 19, 20, 21, 24, 25, 29, 28, 27, 23, 22, 26])
    outMat, nNodes = MIT(counter[6])
    print(outMat)

    walk, acn, edgeVals = matDFS(outMat, nNodes, 17 )

    print(walk)
    #for i in range(1,nNodes):
        #walk, acn, edgeVals = matDFS(outMat, nNodes, i)
        #print(walk)
        #subWalks = connectedSubWalks(walk, acn)
        #lens = [ len(x) for x in subWalks]

        #if(lens[0] >=10):
            #print(subWalks)


def shortTest():
    outMat, nNodes = MIT(counter[6])
    print(outMat)
    drawBinMatrix(outMat)

    #for subList in longestSublists(pathSig(counter[6])):
        #print(subList,len(subList))

#longestPathTest2()

#testCompareVMat()

#longestPathTest2()

shortTest()
