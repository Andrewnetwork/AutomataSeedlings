
from GraphMaker import *
import pandas as pd
import datetime as datetime
from GraphTraverse import *

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
                0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
                0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 0;\
                0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0;\
                0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 0;\
                0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0;\
                0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0')


def tst1():
    print(graphMaker(B_named))

    print( edgeTypeFrequencies( B_named ) )


    for m in v:

        (names, mat) = ETPM(m)
        df = pd.DataFrame(mat, index=names, columns=names)
        print(df)

        (names, mat2) = ETPM(counter[2])
        df = pd.DataFrame(mat2, index=names, columns=names)
        print(df)

        diffMat = np.abs(mat-mat2)
        df = pd.DataFrame(diffMat, index=names, columns=names)
        print(df)


        print(mat2.sum() / diffMat.sum() )


        #print(matrixDiff(v[5],m))



def generateSim():
    print("Running...")
    # 13 bits.

    predictionThreshold = 50
    sameThresh = 8

    while (True):
        rand = generateRandomConnectedBinaryMatrix(v[0].shape, 13)


        diff = matrixDiff(rand,v[0])

        if diff[0] <= sameThresh and  diff[1] <= predictionThreshold and diff[2][0] > diff[2][1]:
            saveBinMatrixIMG(rand,"tst/tst1",str(datetime.datetime.now()))
            print(diff)
            print("Running...")



def tst2():
    aDict = ACN(B_named)
    lst = list(dfs_paths(aDict, str(1), str(3)))
    print( lst  )


tst2()
