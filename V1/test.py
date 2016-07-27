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
from MatrixSim import *

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

def B():
    print(B_named )

    b= ACN(B_named)

    print( "Length of : "+ str( len(b) ) );

    for node in b:
        print("Parent Node Identity: "+str( node.identity ) )
        for chld in node.children:
            print chld.identity

    print("Frquency list: ", freqCountAdjacencyList(b) )


def A():
    print(A_named)
    a = ACN(A_named)

    print( "Length of : "+ str( len(a) ) );

def test1():
    print("========= Test 1 =========")

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

    a = ACN(A_named)
    b = ACN(B_named)
    c = ACN(A_unnamed)


    print("Frquency list: ", FCAL(a))
    print("Frquency list: ", FCAL(b))
    print("Frquency list: ", FCAL( c ) )

def test2():
    print("========= Test 2 =========")

    zeroes = \
    np.matrix('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
               0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
               0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
               0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
               0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
               0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
               0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
               0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')

    first= \
        np.matrix('0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0;\
                   0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0;\
                   0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0;\
                   0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0;\
                   0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0;\
                   0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0;\
                   0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0;\
                   0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')

    second = \
        np.matrix('0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 0;\
                   0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0;\
                   0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0;\
                   0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 0;\
                   0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0;\
                   0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0;\
                   0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0;\
                   0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')

    print("First: ", FCAL( ACN(first) ) )
    print("Second: ", FCAL(ACN(second)))
    print("......")
    print("First: ", FCAL(ACN(first)))
    print("Second Reversed: ",list(reversed(FCAL(ACN(second)))) )

    print(".....SFCAL_N.....")

    r = SFCAL_N( FCAL( ACN(first) ), FCAL(ACN(second))  )
    r2 = SFCAL_N( FCAL( ACN(first) ), list(reversed(FCAL(ACN(second)))))

    print("Result: ",r)
    print("Result Reversed: ",r2)
    print("Sum: ", (r+r2) )
    print("Difference: ", np.abs( (r-r2) ) )
    print("Genuine Difference: ", (r+r2)-1)
    print("Difference - Genuine Diff: ",np.abs( np.abs( (r-r2) ) - ((r+r2)-1) ))


def test3():
    print("========= Test 3 =========")
    print("     The HOOK analysis    ")
    print("===========================")


    t = [0,1]

    t[0] = \
    np.matrix('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
               0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0;\
               0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0;\
               0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0;\
               0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0;\
               0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0;\
               0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0;\
               0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0')

    t[1] = \
    np.matrix('0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0;\
               0 0 1 1 1 0 0 0 1 0 0 0 0 0 0 0;\
               0 0 0 1 0 0 0 1 1 0 0 0 0 0 0 0;\
               0 0 0 0 0 0 0 0 1 1 1 0 0 0 0 0;\
               0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0;\
               0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0;\
               0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
               0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')

    v = [0,1,2,3,4,5]

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



    print("FCAL of Tests")
    for idx, test in enumerate(t):
        print("Test: ", idx, FCAL(ACN(test)))

    print("FCAL of Variations")
    for idx, variation in enumerate(v):
        print("Variation: ",idx,FCAL(ACN(variation)) )

    simResults    =  np.zeros((len(v),len(v)))
    simResultsRev =  np.zeros((len(v),len(v)))
    for idx1, variation1 in enumerate(v):
        for idxTest, tst in enumerate(t):
            r = SFCAL_N(FCAL(ACN(variation1)), FCAL(ACN(t[idxTest])))
            print("->SIM of:         ", idx1, "and", "test",idxTest,r)

            b = SFCAL_N(list(reversed(FCAL(ACN(variation1)))), FCAL(ACN(t[idxTest])))
            print("->REVERSE SIM of: ", idx1, "and", "test",idxTest, b)


        for idx2, variation2 in enumerate(v):
            r = SFCAL_N( FCAL(ACN(variation1)), FCAL(ACN(variation2) ) )
            simResults[idx1,idx2] = r
            print("SIM of:         ",idx1,"and",idx2, r )

            b = SFCAL_N( list(reversed( FCAL(ACN(variation1)) )), FCAL(ACN(variation2) ) )
            simResultsRev[idx1,idx2] = b
            print("REVERSE SIM of: ", idx1, "and", idx2, b)

    print(simResults)
    print("----------------")
    print (simResultsRev)


def test4():
    print("========= Test 4 =========")

    v = [0,1]

    v[0] = \
    np.matrix('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
               0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
               0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0;\
               0 0 0 0 1 1 1 1 1 1 1 1 1 0 0 0;\
               0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0;\
               0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
               0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
               0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')

    v[1] = \
        np.matrix('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
                   0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
                   0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
                   0 1 1 1 1 0 0 1 0 0 0 0 0 0 0 0;\
                   0 0 0 0 1 0 0 1 0 0 0 0 0 0 0 0;\
                   0 0 0 0 1 0 0 1 0 0 0 0 0 0 0 0;\
                   0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0;\
                   0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')

    vFCAL = FCAL(ACN(v[0]))

    predictionThreshold = 0.7

    print("Running...")
    # 13 bits.
    while(True):
        rand = generateRandomConnectedBinaryMatrix(v[0].shape, 13)
        rFCAL = FCAL( ACN(rand) )

        normal = SFCAL_LCS(vFCAL,rFCAL)
        rev    = SFCAL_LCS(list(reversed(vFCAL)),rFCAL)

        if( rev > predictionThreshold or normal > predictionThreshold ):
            print("Reference:      ", vFCAL,normal)
            print("Generation:     ", rFCAL)
            print("Generation Rev: ", list(reversed(vFCAL)),rev)

            print(rand)
            drawBinMatrix(rand)

            l = raw_input("WAIT")
            print("Running...")

# TODO: Finding the perfect similarity matrix.

def test5():
    a = [2, 3, 1, 6]
    b = [4, 2 ,3, 5]

    print( lcs(a,b) )
    print( SFCAL_LCS(a,b) )



def test6():
    tst = \
        np.matrix('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
                   0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
                   0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
                   0 1 1 1 1 0 0 1 0 0 0 0 0 0 0 0;\
                   0 0 0 0 1 0 0 1 0 0 0 0 0 0 0 0;\
                   0 0 0 0 1 0 0 1 0 0 0 0 0 0 0 0;\
                   0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0;\
                   0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')

    imgplot = plt.imshow(tst,interpolation="nearest", cmap="hot")
    plt.axis("off")
    plt.show()


def test7():
    v = [0, 1, 2, 3, 4, 5]

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


    pathSizesCollect = []

    for mat in v:
        acn = ACN_D(MIT(mat))

        paths = []

        for nodeID in range(2,len(acn)+1):
            tmp = list( dfs_paths( acn,str(1),str(nodeID) ) )
            paths.append(tmp)

        pathSizes = []

        for p in paths:
           pathSizes.append( len(p) )

        print(pathSizes)
        pathSizesCollect.append(pathSizes)

    compMatrix = np.zeros( (6,6) )
    for idx1,elm1 in enumerate(pathSizesCollect):
        for idx2,elm2 in enumerate(pathSizesCollect):
            compMatrix[idx1,idx2] = SFCAL_LCS(elm1,elm2)
            print(idx1,idx2,"---:",compMatrix[idx1,idx2] )

    print(compMatrix)

def test8():

    v = [0, 1]

    v[0] = \
           np.matrix('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
                      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
                      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
                      0 1 1 1 1 0 0 1 0 0 0 0 0 0 0 0;\
                      0 0 0 0 1 0 0 1 0 0 0 0 0 0 0 0;\
                      0 0 0 0 1 0 0 1 0 0 0 0 0 0 0 0;\
                      0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0;\
                      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')


    vdf = DFS_PF( v[0] )

    predictionThreshold = 0.7

    print("Running...")
    # 13 bits.
    while (True):
        rand = generateRandomConnectedBinaryMatrix(v[0].shape, 13)
        rdf = DFS_PF( rand )

        normal = SFCAL_N(vdf, rdf)
        rev = SFCAL_N(list(reversed(vdf)), rdf)

        if (rev > predictionThreshold or normal > predictionThreshold):
            print("Reference:      ", vdf, normal)
            print("Generation:     ", rdf)
            print("Generation Rev: ", list(reversed(vdf)), rev)

            print(rand)
            saveBinMatrixIMG(rand,"OutImages/HookTest1/",str(datetime.datetime.now()))
            print("Running...")


def test9():
    v = [0, 1, 2, 3, 4, 5]

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

    vdf = []

    for mat in v:
        vdf.append(DFS_PF(mat))

    for result in vdf:
        print sorted( result )


def test10():
    lst = v
    lst.append(counter[0])
    lst.append(counter[1])

    for variant in lst:
        graph = ACN_D(MIT(variant))

        nNodes = len(graph)

        topRange = range(1,nNodes+1)

        innerRange = range(1,nNodes+1)
        innerRange.pop(0)

        paths = []

        for i in topRange:
            for j in innerRange:
                paths.append( list(dfs_paths(graph, str(i), str(j))) )

            if(len(innerRange) > 0 ):
                innerRange.pop(0)

        #print(paths[0])

        lenOfPaths = sorted([len(x) for x in paths ])

        print(lenOfPaths)

def test11():
    print( matrixSim(v[0],v[2]) )



test11()