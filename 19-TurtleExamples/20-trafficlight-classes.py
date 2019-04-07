import turtle
turtle.setup(400,400)
screen = turtle.Screen()


class Light(turtle.Turtle):  #Light is based on Turtle.  Inheritance.

    def __init__(self, color, x, y):
        super().__init__()
        self.speed(0)  # make turtle move instantly
        self.shape("circle")   # https://docs.python.org/3.3/library/turtle.html?highlight=turtle#appearance
        self.shapesize(3,3,3)   # https://docs.python.org/3.3/library/turtle.html?highlight=turtle#turtle.shapesize
        self.fillcolor("white")
        self.penup()
        self.setpos(x,y)

        self.colorON = color  # set some custom value not normally part of a turtle method


    def light_on(self):
        self.fillcolor(self.colorON)

    def light_off(self):
        self.fillcolor("black")


# put the lights on the screen where they go.
red    = Light("red",    0, 80)
yellow = Light("yellow", 0, 0)
green  = Light("green",  0, -80)


class GameFSM:

    def __init__(self, r, y, g):
        self.lightState = "GREEN"
        self.red = r
        self.yellow = y
        self.green = g

    def setLights(self):
        if self.lightState == 'GREEN':
            self.red.light_off()
            self.yellow.light_off()
            self.green.light_on()
        elif self.lightState == 'RED':
            self.red.light_on()
            self.yellow.light_off()
            self.green.light_off()
        elif self.lightState == 'YELLOW': # state is green.  Handle the timer event.
            self.red.light_off()
            self.yellow.light_on()
            self.green.light_off()
        else:
            print("Bad light!")


    def changeState(self):
        if self.lightState == 'RED':
            self.lightState = "GREEN"
            screen.ontimer(self.changeState, 2000)
        elif self.lightState == 'YELLOW':
            self.lightState = "RED"
            screen.ontimer(self.changeState, 2000)
            print("Light is now RED.")
        elif self.lightState == 'GREEN': # state is green.  Handle the timer event.
            self.lightState = "YELLOW"
            screen.ontimer(self.changeState, 1000)
        else:
            print("Bad light!")
        print("Light is now ", self.lightState)
        self.setLights()



def look_at_light(g):
    print("The light is....", game.lightState)
    screen.ontimer(lambda : look_at_light(g), 500)




# the listen function on a screen makes the screen start responding to events.
screen.listen()

# create the game out of the three lights.
game = GameFSM(red, yellow, green)
game.setLights()
screen.ontimer(game.changeState, 2000)
look_at_light(game)



# instead of exit on click, the screen mainloop function stops
#  and waits for events.  It's up to you to quit!
screen.mainloop()
