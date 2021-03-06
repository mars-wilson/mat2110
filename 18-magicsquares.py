

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


    :return: the candidate input by the user
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


def test_isMagicByRows():
    print("True ?", isMagicByRows([ [ 1 ]], 1 )) # is this a magic square?
    print("True ?", isMagicByRows([[4,9,2],[3,5,7],[8,1,6]], 15))  # magic square from wikipedia
    print("False ?", isMagicByRows([[4, 9, 1], [3, 5, 7], [8, 1, 6]], 15))  # bad square


def isMagicByForwardSlashDiag(c, magicNum):
    """
    4 9 *2
    3 *5 7
    *8 1 6
    """
    size = len(c[0])
    col = size - 1
    sum = 0
    for row in range(size):
        sum += c[row][col]
        col = col - 1
    if sum != magicNum:
        return False
    return True


def allNumbersUnique(c):
    """
    [ [ 1,2], [3, 4] ]   True
    [ [ 1, 1], [3, 4]]  False ... missing a 2.  1 is duplicated.
    [ [1, 3], [4, 5]]  True = 2 is missing. But unique
    [ [ 2, 1], [4, 3] ]  True

    """
    numbersSeen  = []
    # step through the square and see if I've seen any of the numbers before
    for row in range(len(c)):
        for col in range(len(c[row])):
            element = c[row][col]
            if element in numbersSeen:
                return False
            else:
                numbersSeen.append(element)
    return True

def test_allNumbersUnique():
    print("True? ", allNumbersUnique([ [ 1,2], [3, 4] ]) )
    print("False? ", allNumbersUnique([ [ 1, 1], [3, 4]]))


def analyzeCandidate(c):
    result = True  # assume it is a magic square, prove otherwise
    if not isItSquare(c):
        result = False
        print("This is not square. No magic square here.")
    if not isCandidateIntegers(c):
        result = False
        print("not all integers, silly!")
        return False  # quit - no point causing more errors if we're not all integers.
    magicSum = get_magicNumber(c)
    if not isMagicByRows(c, magicSum):
        result = False
        print("Not all rows sum to the same thing.")
    if not isMagicByCols(c, magicSum):
        result = False
        print("Column mismatch")
    if not isMagicByForwardSlashDiag(c, magicSum):
        result = False
        print("forward diagonal bad")
    if not isMagicByBackwardSlashDiag(c, magicSum):
        result = False
        print("back diagonal bad")
    if not allNumbersInSequence(c, magicSum):
        print("Note:  not using a sequence")
    return result


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



TESTING = True

if __name__ == '__main__':
    if not TESTING:
        main()
    else:
        # test_getCandidate()
        test_isItSquare()
        test_getMagicNumber()
        test_isCandidateIntegers()
        test_isMagicByRows()
        test_allNumbersUnique()



