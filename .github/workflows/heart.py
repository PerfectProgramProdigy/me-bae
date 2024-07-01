#turtle is a module which allows you to make gui graphics using python
import turtle
"""
left turns the pen or cursor to the left by given degrees
right turns the pen or cursor to the right by given degrees
forward moves the pen forward or draws for the given units

so pen.forward(100): draws for 100 units
"""
#sets up screen or window
screen = turtle.Screen()
#sets background color
screen.bgcolor('black')
#sets window title 
screen.title('Heart <3')
#sets a pen or stylus
pen = turtle.Pen()
#sets the speed the pen will move at
pen.speed(500)
#sends the pen to 100 units left of the center
pen.goto(-100, 0)
pen.left(90)
#sets pen color
pen.color('pink')
#sets fill color
pen.fillcolor('pink')
#sets pen width
pen.width(7)
pen.speed(500)
#flags start of shape
pen.begin_fill()
#allows programmer to create circles and semi-circles
for angle in range(160):
    pen.forward(1)
    pen.right(1)
pen.left(140)
pen.speed(500)
for angle in range(160):
    pen.forward(1)
    pen.right(1)
pen.speed(500)
for angle in range(25):
    pen.forward(1)
    pen.right(1.5)
pen.speed(1)
pen.forward(180)
pen.right(109)
pen.forward(180)
pen.speed(500)
for angle in range(25):
    pen.forward(1)
    pen.right(1.5)
#flags end of shape
pen.end_fill()
#keeps the window open until user closes it
turtle.done()
