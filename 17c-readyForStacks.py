import turtle
import math

FORWARDSIZE = 10
ANGLESIZE = 60


def buildRules(ruleString):
    """
    Write function buildRules that builds a set of rules from a rule string
    it takes one parameter, a rule string
    it returns an axiom
    it also returns a list of transformations.  Let's name it a "rule set!"
    Example ruleString:
        '''
        A
        A --> BAB
        B --> +F--FF++F-
        '''
    Another example ruleString:  'A \n  A-->FBF \n  B-->+CFC- \n  C--> --A++ '
    """
    ruleString = ruleString.strip()
    myList = ruleString.split("\n")
    axiom = myList[0]


    rulesDict = {}  # empty dictionary
    for i in range(1, len(myList)):
        # step through the rules, parse them into lhs and rhs, trim whitespace, and store in dict.
        line = myList[i]
        rules = line.split('-->')
        lhs = rules[0].strip()
        rhs = rules[1].strip()
        rulesDict[lhs] = rhs

    return axiom, rulesDict


def applyRuleSet(ruleSet, leftChar):
    """Write function applyRuleSet that takes a list of transformations( a rule set)
     , and a left character, and returns a right character.
    """

    # Look up the leftchar in the  ruleSet dict.  If it's not there, return the leftchar.
    return ruleSet.get(leftChar, leftChar)



def processString(rulz, oldStr):
    """ given a string oldStr transform it into newStr with rules """
    newStr = ""
    for ch in oldStr:
        newStr = newStr + applyRuleSet(rulz, ch)

    return newStr


def executeLSystem(numIters,rules, axiom):
    currentString = axiom
    for i in range(numIters):
        newString = processString(rules, currentString)
        currentString = newString

    return currentString




def goTurtleStep(t, c, distance=FORWARDSIZE, angle=ANGLESIZE):
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
        t.forward(distance)
    elif c == '+':
        t.right(angle)
    elif c == '-':
        t.left(angle)
    else:
        pass

    return


def test_goTurtleStep(t):
    t.pendown()
    goTurtleStep(t, 'F')
    goTurtleStep(t, '+')
    goTurtleStep(t, 'F')
    goTurtleStep(t, '-')
    goTurtleStep(t, 'F')


def goTurtleGo(someT, cmdString, startPos=(0,0), stepSize=FORWARDSIZE, angle=ANGLESIZE):

    # introducing format strings!  New with Python 3.5
    # see how the string has a f before opening quote?
    # see how it has a { } in it that contains a variable name!
    print(f"We are going to run the turtle with this command string: \n  {cmdString} ")

    someT.penup()
    someT.setpos(startPos)  # put someT on the screen left.
    someT.setheading(0)
    someT.pendown()
    for command in cmdString:
        goTurtleStep(someT, command, stepSize, angle)


def colorAngleToRGB(degrees, intensity=1.0):
    """ Take an angle in degrees and convert it to a color combo of red, green, and blue
     This gives us a convenient way to cycle through colors with just one parameter.
     intensity of 1 is on the edge of the circle.  intensity of 0 is in the middle and is black.
     The returned RGB are using red green blue values between 0 and 1.
     """
    redAngle   = math.radians(degrees)
    greenAngle = math.radians(degrees + 120.0)
    blueAngle  = math.radians(degrees + 240.0)
    red   = intensity * (math.sin(redAngle)   + 1) / 2   # convert range -1 .. 1 to range 0..1.
    green = intensity * (math.sin(greenAngle) + 1) / 2   # add one makes it 1 .. 2
    blue  = intensity * (math.sin(blueAngle)  + 1) / 2   # divide by 2 makes 1 ... 2 range into 0..1
    return red,green,blue  #  RGB color model in range 0,1



# Set up the window and its attributes
turtle.setup(400,400)
wn = turtle.Screen()
wn.bgcolor("antique white")
wn.colormode(1.0)  # use red,green,blue in range 0-1 because sin returns range -1 to 1


# Make an L-System.

# Execute the string from the L System to move the turtle around!
# named colors are here:  http://wiki.tcl.tk/37701

#mars = turtle.Turtle()  # create mars

#test_goTurtleStep(mars)


def main():
    mars = turtle.Turtle()  # create mars
    maxIters = 5

    stepSize = 400      # initial stepsize, how much to move F
    scaler = 3          # how much to scale stepsize for different nums of iterations
    start = (-200, 0)   # starting location of turtle
    angle = 30
    triangleFractal = "F   \n     F --> +F--FF++F-  "

    axiom, rules = buildRules(triangleFractal)
    for i in range(maxIters):
        commandString = executeLSystem(i, rules, axiom)
        mars.color(colorAngleToRGB(i / maxIters * 360))
        goTurtleGo(mars, commandString, start, stepSize, angle)
        stepSize = stepSize / scaler

main()

wn.exitonclick()