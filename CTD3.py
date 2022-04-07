import turtle

turtle.title("My Turtle Program")
t = turtle.Turtle()
turtle.bgcolor("black")
t.color("cyan")
t.speed(0)

for n in range(1000):
    t.forward(n)
    t.right(50)
