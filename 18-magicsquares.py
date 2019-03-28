

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

def isItSquare(cand):
    # the number of lists is the same as the number of numbers in each list
    numLists = len(cand)
    for lst in cand:
        if len(lst) != numLists:
            return False
    # [ [1,2], [4,5] ]
    return True


def test_isItSquare():


def analyzeCandidate(c):
    result = True  # assume it is a magic square, prove otherwise
    if not isItSquare(c):
        result = False
    #magicSum = computeMagicSum(c)
    #if not allRowsSumToMagicSum(c, magicSum):
    #    result = False

    return result



def main():
    print("Welcome to ... MANGIC SUWARD!")
    print("Enter your candidate square.")
    print("I, your oracle, will analyze it and determine if yoiiu are stupid or not.")
    print("Type your square with ints seprated by spaces")
    print("And a bblank liine when yoiu are done")
    candidate = getCandidate()
    result = analyzeCandidate(candidate)
    if result:
        print("You are wise.  This is GOOD SQUARE.")
    else:
        print("You are stupid.  Go away.")


if __name__ == '__main__':
    main()
