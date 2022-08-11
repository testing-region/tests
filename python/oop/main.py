# Notice how python classes are Capitalised: Pascal case

from shapes import Paper, Rectangle, Oval, Triangle

paper = Paper()

rect1 = Rectangle()
rect1.set_color("blue")
rect1.set_height(100)
rect1.set_width(200)

rect1.draw()

rect2 = Rectangle()
rect2.set_color("yellow")
rect2.set_height(100)
rect2.set_width(200)
rect2.set_x(10)
rect2.set_y(50)


paper.display()
