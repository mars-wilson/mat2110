import turtle
turtle.setup(300,300)
screen = turtle.Screen()

move_speed = 10  # a constant

fred = turtle.Turtle()

# here is our event handler.
# it uses a global var because event handlers can't have params.
# BAD BAD BAD
def goUP():
    fred.forward(move_speed)

# screen method onkey binds the event handler to a keyboard event
screen.onkey(goUP, "Up")

# now set up the main program
fred.penup()
fred.left(90)
fred.speed(0)   # makes the turtle move as fast as possible.

# the listen function on a screen makes the screen start responding to events.
screen.listen()

# instead of exit on click, the screen mainloop function stops
#  and waits for events.  It's up to you to quit!
screen.mainloop()
