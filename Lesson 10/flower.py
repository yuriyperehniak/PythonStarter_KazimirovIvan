import turtle

t = turtle.Turtle()
t.speed(0)

# Червоний контур та жовта заливка
t.color("red", "yellow")

t.begin_fill()
for _ in range(36):
  t.forward(200)
  t.left(170)
t.end_fill()

turtle.done()