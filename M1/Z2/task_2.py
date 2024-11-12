import turtle as t

"""
Используя методы модуля turtle, 
нарисуйте несколько геометрических фигур: 
прямоугольник, ромб и трапецию. 
Каждая фигура должна быть закрашена в свой цвет, 
который сочетается с остальными. 
Используйте цветовой круг Adobe для выбора красивого сочетания цветов.
"""

t.ht()

t.penup()
t.goto(-150, 0)
t.pendown()

t.colormode(255)
# t.colormode(cmode=None)

color_rectangle = (62, 110, 222)
t.color(color_rectangle)

t.begin_fill()
t.forward(100)
t.left(90)
t.forward(70)
t.left(90)
t.forward(100)
t.left(90)
t.forward(70)
t.end_fill()

t.left(90)
t.penup()
t.forward(150)
t.pendown()

color_rhombus = (62, 160, 223)
t.color(color_rhombus)

t.begin_fill()
t.left(60)
t.forward(60)
t.left(60)
t.forward(60)
t.left(120)
t.forward(60)
t.left(60)
t.forward(60)
t.end_fill()

t.left(60)
t.penup()
t.forward(50)
t.pendown()

color_trapezoid = (62, 222, 179)
t.color(color_trapezoid)

t.begin_fill()
t.forward(100)
t.left(120)
t.forward(60)
t.left(60)
t.forward(40)
t.left(60)
t.forward(60)
t.end_fill()

t.exitonclick()
