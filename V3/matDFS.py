from graphHelpers import *
import GraphFN as GFN
import numpy as np

def matDFS(mat,nNodes,start, acn =None, edgeValMat=None):

    if( acn==None and edgeValMat==None):
        acn, edgeValMat = ACN_D(mat, nNodes)


    currentNode = str(start)
    next = []
    visited = set()
    done = False
    walk = []
    branchCounter = 0

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
            for indx in range(nextSize):
                if next[indx] in currentACN:
                    candidates.append(indx)


            # We have to make a branch.
            if(len(candidates) >= 2):
                #print(currentNode, candidates,walk)
                #choice = raw_input("Select path: ")
                branchCounter+=1
                #print(branchCounter)
                top = next.pop(candidates[0])

            elif(len(candidates) >= 1):
                top = next.pop(candidates[0])
            else:
                top = next.pop(0)


        else:
            done = True

        # We want the next node to be connnected to the last node if possible.


        if len(top) == 0:
            done = True

        currentNode = top


        #Modify decision structure


    return (walk,acn,edgeValMat)



def matShortestPath(mat,nNodes,start, acn =None, edgeValMat=None):

    if( acn==None and edgeValMat==None):
        acn, edgeValMat = ACN_D(mat, nNodes)

    choiceChains = []
    walks = []


    while True:
        currentNode = str(start)
        next = []
        visited = set()
        done = False
        walk = []
        branchCounter = 0
        choices = []

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
                for indx in range(nextSize):
                    if next[indx] in currentACN:
                        candidates.append(indx)


                # We have to make a branch.
                if(len(candidates) >= 2):
                    branchCounter+=1

                    choice = np.random.randint(0, len(candidates) - 1, size=1)[0]

                    choices.append(choice)

                    top = next.pop(candidates[choice])

                elif(len(candidates) >= 1):
                    top = next.pop(candidates[0])
                else:
                    top = next.pop(0)


            else:
                done = True

            # We want the next node to be connnected to the last node if possible.


            if len(top) == 0:
                done = True

            currentNode = top

        choiceChains.append(choices)
        walks.append(walk)

        if(GFN.connectedWalk(walk,acn) ):
            print("Connected? ",GFN.connectedWalk(walk,acn) )
            print(walk)
            raw_input("T")

        #print(choices)




    return (walk,acn,edgeValMat)