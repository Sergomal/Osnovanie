import turtle as t

"""
Нарисуйте три квадрата размером 30 на 30 на расстоянии 
30 пикселей друг от друга. 
Квадраты не должны соединятся зеленой линией.
"""

t.ht()

t.penup()
t.goto(-+75, 0)
t.pendown()

t.color("green")

side = 30

for i in range(3):
    t.begin_fill()
    for j in range(4):
        t.forward(side)
        t.left(90)
    t.end_fill()

    t.penup()
    t.forward(side * 2)
    t.pendown()

t.exitonclick()
