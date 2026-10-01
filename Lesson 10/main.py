import turtle

t = turtle.Turtle()

t.speed(100)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

t.begin_fill()
for i in range(12):
    t.color(colors[i % 6], colors[3])
    t.forward(50)
    t.right(30)
t.end_fill()

turtle.done()
