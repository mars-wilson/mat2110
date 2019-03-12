"""
    To execute this file in Python Console in PyCharm:
        the "exec" function in Python 3 executes a string like a program.
        the below line opens the file, reads the entire file as one string.
        Then executes it!
        This brings all the functions into the console.
        exec( open("16_CanoeOverFalls.py").read() )

"""

import random

def getWordsList(minLength=4):
    try:
        filehandle = open("words.txt", "r")
        wordsFromFile = filehandle.readlines()
        filehandle.close()
    except IOError as e:
        print("OOPS! \n", str(e))
        return []

    # here, step through the list backwards
    # remove every word that is less than minLength
    for i in reversed(range(len(wordsFromFile))):
        if len(wordsFromFile[i]) < minLength:
            del wordsFromFile[i]
        else:
            wordsFromFile[i] = wordsFromFile[i].strip()
    return wordsFromFile


def fillBlanksWhereGuessMatchesWord(gChar, wrd, b):
  """ where the word wrd has a character that matches guess char gChar,
      replace the corresponding place in list b with the char g """
  # b is a list.  Make a copy of it so as to not clobber the argument passed in.
  b = b[:]
  for index in range(len(wrd)):
    if wrd[index] == gChar:
      b[index] = gChar
  return b



def test_fillBlanksWhereGuessMatchesWord():
  b = fillBlanksWhereGuessMatchesWord( 'o', 'moo',  list('___') )
  print(' '.join(b),  'should be _ o o')
  b = fillBlanksWhereGuessMatchesWord( 'm', 'moo',  list('___') )
  print(' '.join(b),  'should be m _ _' )


def makeBlanksList( wordLen ):
    return list("_" * wordLen)

def test_makeBlanksList():
    print("Here's a blank list len 5", makeBlanksList(5))
    print("Here's a blank list len 0", makeBlanksList(0))



def pickRandomWord(listOfWords):
    """ select one random word from a list of words"""
    #i = random.randrange(0, len(listOfWords))
    #return listOfWords[i]
    return random.choice(listOfWords)

def test_pickRandomWord():
    for i in range(10):
        print("Random word from a,b,c: ", pickRandomWord(['a','b','c']))


def displayCurrentGame(bList, m):
    print("You have ", m, "guesses remaining.")
    result = ""
    for element in bList:
        result = result + " " + element
    #result =  " ".join(bList) # bList must be a list OF STRINGS
    print(result)

def test_displayCurrentGame():
    displayCurrentGame(['_',"_"], 5)


def getGuess(missesleft):
    """ get a guess from the user """
    print("You have ", missesleft, "misses to go")
    return input("What's your guess? ")

def insultPlayer():
    result = random.choice(["You dolt.", "Farthead.","You're a Dweeb", "DOH!"])
    return result;

def complimentPlayer():
    result = random.choice(["You ace.", "Brainhead.","You're a cutie", "YARH!"])
    return result;

def playGame():
    wordsList = getWordsList(5)

    word = pickRandomWord(wordsList)
    blanks = makeBlanksList( len(word) )

    missesRemaining = 5
    guessedTheWord = False

    while (missesRemaining > 0) and not guessedTheWord:
        displayCurrentGame(blanks, missesRemaining)
        guess = getGuess(missesRemaining)
        if len(guess) == 1:
            if guess in word:
                blanks = fillBlanksWhereGuessMatchesWord(guess, word, blanks)
                print(complimentPlayer(), "You guessed right!")
            else:
                print("WRONG.", insultPlayer())
                missesRemaining = missesRemaining - 1
        else:
            if word == guess:
                guessedTheWord = True
            else:
                print("Wrong word!", insultPlayer())
                missesRemaining = missesRemaining - 1

    # now the game is over.
    if guessedTheWord:
        for i in range(3):
            print(complimentPlayer())
        print("YOU ARE SAVED!")
    else:
        for i in range(3):
            print(insultPlayer())
        print("The word was",word)
        print("AAaaaaahhhhh….. byebye.  Off the falls you go.  So tragic.")

playGame()
