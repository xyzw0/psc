import turtle

sk = turtle.Turtle()

#Square
for i in range(25):
    sk.forward(100)
    sk.right(90)
    sk.forward(50)
    sk.right(90)
sk.end_fill()

#Rectangle
for i in range(25):
    sk.forward(50)
    sk.right(90)
sk.end_fill()

#Star0
sk.color("orange")
sk.fillcolor("skyblue")
sk.begin_fill()
for i in range(5):
    sk.forward(200)
    sk.right(144)
    
sk.end_fill()

