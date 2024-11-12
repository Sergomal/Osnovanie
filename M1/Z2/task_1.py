import turtle as t

"""
Нарисуйте три разных круга, используя разные цвета и радиусы, 
используя модуль turtle. 
Для каждого круга используйте begin_fill(), color(), circle() и end_fill().

Сохраните файл с проектом на компьютер.
"""

t.ht()

t.penup()
t.goto(-250, 0)
t.pendown()

offset = 0

for i in range(3):
    radius = int(input("Введите радиус: "))
    offset = radius
    t.penup()
    t.forward(offset)
    t.pendown()
    color_shape = input("Введите цвет (red, green, blue, pink, yellow, purple, indigo, gray):")
    t.color(color_shape)
    t.begin_fill()

    t.circle(radius)
    t.end_fill()

    t.penup()
    t.forward(offset)
    t.pendown()

t.exitonclick()
