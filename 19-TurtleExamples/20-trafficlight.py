import turtle
turtle.setup(400,400)
screen = turtle.Screen()

def set_light_properties(somet, color, x, y):
    somet.speed(0)  # make turtle move instantly
    somet.shape("circle")   # https://docs.python.org/3.3/library/turtle.html?highlight=turtle#appearance
    somet.shapesize(3,3,3)   # https://docs.python.org/3.3/library/turtle.html?highlight=turtle#turtle.shapesize
    somet.custom_oncolor = color    # set some custom value not normally part of a turtle method
    somet.fillcolor("white")
    somet.penup()
    somet.setpos(x,y)

def set_light_on(somet):
    somet.fillcolor(somet.custom_oncolor)

def set_light_off(somet):
    somet.fillcolor("black")


# put the lights on the screen where they go.
red = turtle.Turtle()
set_light_properties(red, "red", 0, 80)
yellow = turtle.Turtle()
set_light_properties(yellow, "yellow", 0, 0)
green = turtle.Turtle()
set_light_properties(green, "green", 0, -80)



global_light_state = "GREEN"
def set_lights_for_state():
    global global_light_state
    if global_light_state == 'GREEN':
        set_light_off(red)
        set_light_off(yellow)
        set_light_on(green)
    elif global_light_state == 'RED':
        set_light_on(red)
        set_light_off(yellow)
        set_light_off(green)
    elif global_light_state == 'YELLOW': # state is green.  Handle the timer event.
        set_light_off(red)
        set_light_on(yellow)
        set_light_off(green)
    else:
        print("Bad light!")


def change_light_state():
    global global_light_state
    if global_light_state == 'RED':
        global_light_state = "GREEN"
        screen.ontimer(change_light_state, 2000)
    elif global_light_state == 'YELLOW':
        global_light_state = "RED"
        screen.ontimer(change_light_state, 2000)
        print("Light is now RED.")
    elif global_light_state == 'GREEN': # state is green.  Handle the timer event.
        global_light_state = "YELLOW"
        screen.ontimer(change_light_state, 1000)
    else:
        print("Bad light!")
    print("Light is now ", global_light_state)
    set_lights_for_state()


def look_at_light():
    print("The light is....", global_light_state)
    screen.ontimer(look_at_light, 500)




# the listen function on a screen makes the screen start responding to events.
screen.listen()

global_light_state = "GREEN"
set_lights_for_state()
screen.ontimer(change_light_state, 2000)
look_at_light()



# instead of exit on click, the screen mainloop function stops
#  and waits for events.  It's up to you to quit!
screen.mainloop()
