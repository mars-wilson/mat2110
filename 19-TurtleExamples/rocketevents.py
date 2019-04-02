import turtle

screen = turtle.Screen()

# modified from trinket https://blog.trinket.io/using-images-in-turtle-programs/
# somehow trinket supports png graphics with turtles and the png images can rotate.
# I have no clue how that was implemented but it's likely a rewrite of parts of the turtle module.


# click the image icon in the top right of the code window to see
# which images are available in this trinket
image = "rocketship.gif"

# add the shape first then set the turtle shape
screen.addshape(image)
turtle.shape(image)

screen.bgcolor("lightblue")

move_speed = 10
turn_speed = 10

# these defs control the movement of our "turtle"
def forward():
  turtle.forward(move_speed)

def backward():
  turtle.backward(move_speed)

def left():
  turtle.left(turn_speed)

def right():
  turtle.right(turn_speed)

def quit():
    """ quit the game """
    screen.bye()  # this is how you close a turtle screen and quit the program gracefully.

turtle.penup()
turtle.speed(0)
turtle.home()

# now associate the defs from above with certain keyboard events
screen.onkey(forward, "Up")
screen.onkey(backward, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(quit, 'q')

# the listen function on a screen makes the screen start responding to events.
screen.listen()

# instead of exit on click, the screen mainloop function stops and waits for events.  It's up to you to quit!
screen.mainloop()
