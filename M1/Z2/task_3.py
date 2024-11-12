import turtle as t

"""
Нарисуйте зеленую елку из трех закрашенных треугольников.
"""

t.ht()

t.penup()
t.goto(0, 150)
t.pendown()

color_tree = "green"
t.color(color_tree)

t.begin_fill()
t.right(60)
t.forward(40)
t.left(240)
t.forward(40)
t.right(120)
t.forward(40)
t.end_fill()

t.left(210)
t.forward(25)

t.begin_fill()
t.left(30)
t.forward(60)
t.left(240)
t.forward(60)
t.right(120)
t.forward(60)
t.end_fill()

t.left(210)
t.forward(25)

t.begin_fill()
t.left(30)
t.forward(80)
t.left(240)
t.forward(80)
t.right(120)
t.forward(80)
t.end_fill()

t.exitonclick()
