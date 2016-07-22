from GraphFN import *

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

    a = ACN(A_named)
    b = ACN(B_named)
    c = ACN(A_unnamed)


    print("Frquency list: ", freqCountAdjacencyList(a))
    print("Frquency list: ", freqCountAdjacencyList(b))
    print("Frquency list: ", freqCountAdjacencyList( c ) )

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


    t = [0]

    t[0] = \
    np.matrix('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\
               0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0;\
               0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0;\
               0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0;\
               0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0;\
               0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0;\
               0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0;\
               0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0')

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




    print("FCAL of Variations")
    for idx, variation in enumerate(v):
        print("Variation: ",idx,FCAL(ACN(variation)) )

    simResults    =  np.zeros((len(v),len(v)))
    simResultsRev =  np.zeros((len(v),len(v)))
    for idx1, variation1 in enumerate(v):
        r = SFCAL_N(FCAL(ACN(variation1)), FCAL(ACN(t[0])))
        print("->SIM of:         ", idx1, "and", "test",r)

        b = SFCAL_N(list(reversed(FCAL(ACN(variation1)))), FCAL(ACN(t[0])))
        print("->REVERSE SIM of: ", idx1, "and", "test", b)


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





test3()