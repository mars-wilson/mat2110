

import turtle

FORWARDSIZE = 10
ANGLESIZE = 60


def applyRules(leftChar):
    """ apply rule transforming leftChar to rightStr
    Axiom: F
    F    ->    F - F + +F - F"""
    rightStr = ""
    if leftChar == 'F':
        rightStr = "F-F++F-F"
    return rightStr


def processString(oldStr):
    """ given a string oldStr transform it into newStr with rules """
    newStr = ""
    for ch in oldStr:
        newStr = newStr + applyRules(ch)

    return newStr


def executeLSystem(numIters,axiom):
    resultString = axiom
    for i in range(numIters):
        newString = processString(resultString)
        resultString = newString

    return resultString



def goTurtleStep(t, c):
    """
    Parameters:
        a turtle - some turtle - any turtle!
        a command character - any command character.
    And
        makes the turtle execute the command character
        if the command character isn't implemented, then don't do anything.
    The function need not return anything.
    """
    if c == 'F':
        t.forward(FORWARDSIZE)
    elif c == '+':
        t.right(ANGLESIZE)
    elif c == '-':
        t.left(ANGLESIZE)
    else:
        pass

    return




# Set up the window and its attributes
turtle.setup(400,400)
wn = turtle.Screen()
wn.bgcolor("antique white")

# named colors are here:  http://wiki.tcl.tk/37701

mars = turtle.Turtle()  # create mike
mars.pendown()
goTurtleStep(mars, 'F')
goTurtleStep(mars, '+')
goTurtleStep(mars, 'F')
goTurtleStep(mars, '-')
goTurtleStep(mars, 'F')

# Make an L-System.
commandString = executeLSystem(1, 'F')

# Execute the string from the L System to move the turtle around!
goTurgleGo(mars, commandString)

wn.exitonclick()
