from turtle import Turtle
from random import randint
from turtle import title, exitonclick

"""
Remember: Comments tell you the why behind a code
"""

title("Turtle Race")

# make player objects from Turtle class
player1 = Turtle() 
player2 = Turtle()
player3 = Turtle()
player4 = Turtle()
player5 = Turtle()

# player1 customization
player1.color("red")
player1.shape("turtle")
player1.penup()
player1.goto(-250, 140)
player1.pendown()

# player2 customization
player2.color("blue")
player2.shape("turtle")
player2.penup()
player2.goto(-250, 110)
player2.pendown()

# player3 customization
player3.color("green")
player3.shape("turtle")
player3.penup()
player3.goto(-250, 80)
player3.pendown()

# player4 customization
player4.color("orange")
player4.shape("turtle")
player4.penup()
player4.goto(-250, 50)
player4.pendown()

# player5 customization
player5.color("purple")
player5.shape("turtle")
player5.penup()
player5.goto(-250, 20)
player5.pendown()

# Move players using random integers
for x in range(150):
    player1.forward(randint(1,5))
    player2.forward(randint(1,5))
    player3.forward(randint(1,5))
    player4.forward(randint(1,5))
    player5.forward(randint(1,5))

distance_covered = {
    "player1": player1.xcor(),
    "player2": player2.xcor(),
    "player3": player3.xcor(),
    "player4": player4.xcor(),
    "player5": player5.xcor(),
    }

# print(distance_covered.items())

# prevent the window from closing
# closes the window when the mouse is clicked
exitonclick()
