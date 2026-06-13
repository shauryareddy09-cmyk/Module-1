import turtle

turtle.Screen().bgcolor("Red")

sc = turtle.Screen()
sc.setup(300,400)

board = turtle.Turtle()

for i in range(3):
    board.forward(200)
    board.left(120)