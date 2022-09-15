import turtle
import math


obj = turtle.Turtle()


"""
t -> turtle object
r -> radius
n -> number of sides
"""


# Q1
def square(t):
    """Draw a square

    Args:
        t (Turtle): turtle object
    """

    # since the sqaure has 4 sides, 4 lines have to be drawn
    for lines in range(4):
        t.fd(100)

        # lt takes an angle of turn, for a square, it 90 degrees
        t.lt(90)


# Q2
def square_2(t, length):
    """Draw a square of with given length

    Args:
        t (Turtle): turtle object
        length (float): length of a side
    """

    for lines in range(4):

        # since the length is the size of the side
        t.fd(length)
        t.lt(90)


# Q3
def polygon(t, length, n):
    """Draw a polygon of n sides of a specific length

    Args:
        t (Turtle): turtle object
        length (float): length of polygon
        n (int): number of sides a polygon
    """

    exterior_angle = 360 / n
    for lines in range(n):
        t.fd(length)
        t.lt(exterior_angle)


# Q4
def circle(t, r):
    """Draw a circle

    Args:
        t (Turtle): turtle object
        r (float): radius of the circle
    """

    circumference = 2 * math.pi * r

    # The greater the number segments, the smoother the circle
    n = int(circumference / 0.5)

    segment_length = circumference / n
    polygon(t, segment_length, n)


# Q5
def arc(t, r, angle):
    """Draw an arc

    Args:
        t (Turtle): turtle object
        r (float): radius of arc
        angle (float): angle of arc wich determines fraction of circle to draw
    """

    arc_length = (angle / 360) * 2 * math.pi * r

    # The greater the number of segments, the smoother the arc
    n = int(arc_length / 0.5)

    segment_length = arc_length / n
    segment_angle = angle / n
    for lines in range(n):
        t.fd(segment_length)
        t.lt(segment_angle)


# test functions


# exit turtle window mouse onclick
turtle.exitonclick()
