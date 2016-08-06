def verifyWalk(walkIn,acnDict):
    walk = list(walkIn)
    walkLen = len(walk)
    walkPos = 0
    changed = False

    while walkPos+1 < walkLen:
        # Swap positions if this walk doesn't belong
        if not ( walk[walkPos] in acnDict[walk[walkPos+1]] ):
            print(walk, walk[walkPos], acnDict[walk[walkPos + 1]])
            tmp = walk[walkPos-1]
            walk[walkPos-1] = walk[walkPos]
            walk[walkPos] = tmp
            walkPos = 0

            raw_input("T")
        else:
            walkPos += 1

    return walk
def matDFS(mat,nNodes,start):
    acn, edgeValMat = ACN_D(mat, nNodes)

    currentNode = str(start)
    next = []
    visited = set()
    done = False
    depth = 1
    walk = []

    while not done:
        walk.append(currentNode)

        visited.add(currentNode)

        for elm in acn[currentNode]:
            next.append(elm)

        top = next.pop(0)
        while top in visited and len(top) > 0:
            if(len(next) > 0):
                top = next.pop(0)
            else:
                done = True
                break

        if len(top) == 0:
            done = True

        currentNode = top


    return (walk,acn,edgeValMat)


def matDFS(mat,nNodes,start, acn =None, edgeValMat=None):
    if( acn==None and edgeValMat==None):
        acn, edgeValMat = ACN_D(mat, nNodes)


    currentNode = str(start)
    next = []
    visited = set()
    done = False
    walk = []

    while not done:
        walk.append(currentNode)

        visited.add(currentNode)

        nextCounter = 0
        while nextCounter < len(next):
            if(next[nextCounter] in visited):
                next.pop(nextCounter)
            else:
                nextCounter+=1

        currentACN = acn[currentNode]

        for elm in currentACN:
            if not (elm in visited):
                next.append(elm)

        # Decide which node to make the current node.
        if(len(next) != 0):
            nextCounter = 0
            nextSize = len(next)
            candidates = []
            while nextCounter < nextSize:
                top = next.pop(0)
                if top in currentACN:
                    candidates.append(top)
                else:
                    next.append(top)

                nextCounter +=1

            # We have to make a branch.
            if(len(candidates) >= 2):
                top = candidates[0]
            else:
                top = candidates[0]


        else:
            done = True


        # We want the next node to be connnected to the last node if possible.


        if len(top) == 0:
            done = True

        currentNode = top


        #Modify decision structure


    return (walk,acn,edgeValMat)



def decisionStructurePerms(boundaries):
    # Ex: Given- 3,2,2
    # Out: [0,0,0][1,0,0][2,0,0][0,1,0][0,0,1][1,1,0][1,0,1][2,1,0],[2,1,1]
    perms = []
    lengthOfCounter = len(boundaries)
    perm=np.zeros(lengthOfCounter,dtype=np.int)

    maxPerm = [x-1 for x in boundaries]

    loc = 0

    print(perm)

    overflowCount = 0

    while not np.array_equal(perm,maxPerm):
        if (perm[loc]+1 < boundaries[loc]):
            perm[loc] += 1 + overflowCount
        else:
            #Overflow
            perm[loc] = 0

            if loc + 1 > loc:
                #Reached end of number.
                overflowCount += 1
                loc[0]
            else:
                loc += 1

        print(perm)



    print(perm)

# Given an identified matrix.
def walkMatrixPath(mat, start):
    matCPY = mat.copy()

    #Find location of starting node.
    rowCounter = 0
    colCounter = 0

    matRows = mat.shape[0]
    matCols = mat.shape[1]
    found = False
    startLoc = (0,0)

    while rowCounter < matRows and not found:

        while colCounter < matCols and not found:
            if( mat[rowCounter][colCounter] == start ):
                startLoc=(rowCounter,colCounter)
                found = True
            else:
                colCounter+=1

        colCounter = 0
        rowCounter += 1

    print(startLoc)