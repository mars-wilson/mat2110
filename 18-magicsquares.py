

def getCandidate():
    """
It takes no parameters
It returns a list of lists

First examples.
Enter your square.
One line entries.
When you're done type a blank line.
> 1 3 fred
> 2
> <blank line>
should give back:
[ [1, 3, 'fred']   [ 2 ] ]


    :return:
    """

    candidate = []
    Done = False
    while not Done:
        # get a line
        line = input("> ")
        # see if the line is blank, if so, done
        line = line.strip()
        if line == "":
            Done = True
        else:
            # if not blank, split it on spaces
            # and stgore that in candidate
            splitLine = line.split()
            candidate.append(splitLine)

    return candidate

def test_getCandidate():
    print("Enter your candidate")
    candidate = getCandidate()
    print(candidate)

def isCandidateIntegers(something):
    try:
        for rownum in range(len(something)):
            row = something[rownum]
            for colnum in range(len(row)):
                something[rownum][colnum] = int(something[rownum][colnum])
        return True
    except:
        return False

def test_isCandidateIntegers():
    print("False", isCandidateIntegers( [["3","a"],[5]]))
    print("True", isCandidateIntegers( [["3","2"],["5"]]))

def isItSquare(cand):
    # the number of lists is the same as the number of numbers in each list
    numLists = len(cand)
    for lst in cand:
        if len(lst) != numLists:
            return False
    # [ [1,2], [4,5] ]
    return True


def test_isItSquare():
    print("TRUE", isItSquare([[1,2],[3,4]]))
    print("FALSE", isItSquare([[1, 2], [3]]))


def analyzeCandidate(c):
    result = True  # assume it is a magic square, prove otherwise
    if not isItSquare(c):
        result = False
        print("This is not square. No magic square here.")
    #magicSum = computeMagicSum(c)
    #if not allRowsSumToMagicSum(c, magicSum):
    #    result = False

    return result

def isMagicByRows(candidate, magicSum):
    """ step thru rows and see if they add up tomagicSum"""
    # candidate... might be [ [ 1,2 ], [3,4 ] ]
    # magicSum might be ... 3
    # step through each row

    for row in candidate:
        # row 0 is [ 1, 2 ]
        if sum(row) != magicSum:
            return False
    return True





def main():
    print("Welcome to ... MANGIC SUWARD!")
    print("Enter your candidate square.")
    print("I, your oracle, will analyze it and determine if yoiiu are stupid or not.")
    print("Type your square with ints seprated by spaces")
    print("And a bblank liine when yoiu are done")
    candidate = getCandidate()
    isInts = isCandidateIntegers(candidate)
    if not isInts:
        print("Oh dolt.  You cannot type the integer.  Must learn integer.")
        result= False
    else:
        result = analyzeCandidate(candidate)

    magicSum = get_magicNumber(candidate)
    if not isMagicByRows(candidate, magicSum):
        result = False
        print("A row does not sum to ", magicSum)

    if result:
        print("You are wise.  This is GOOD SQUARE.")
    else:
        print("You are stupid.  Go away.")



def get_magicNumber(someSquare):
    """ needs a list of lists maybe magic square, gives back an integer"""
    # someSquare may be ... [ [ 2,7,6],[9,5,1],[4,3,8]]
    topRow = someSquare[0]
    return sum(topRow)
    total = 0
    for num in topRow:
        total = total + num
    return total

def test_getMagicNumber():
    print("15", get_magicNumber( [ [ 2,7,6],[9,5,1],[4,3,8]]) )
    #print("Unknown", get_magicNumber( getCandidate() ) )

if __name__ == '__main__':
    main()
    #test_isItSquare()
    #test_getMagicNumber()
    #test_isCandidateIntegers()
