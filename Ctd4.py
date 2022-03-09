import turtle

t = turtle.Turtle()
t.color("cyan")
t.speed(0)
for n in range(1000):
    t.forward(n)
    t.right(50)
