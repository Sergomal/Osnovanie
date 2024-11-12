import turtle as t

t.ht()
t.speed(0)
t.pensize(5)

t.colormode(255)

for r in range(40, 0, -10):
    side = r * 3

    for i in range(6):
        t.color(255, 165, r * 6)
        t.fillcolor(162, r * 6, 255)
        t.begin_fill()

        for j in range(3):
            t.backward(side)
            t.right(120)

        t.end_fill()
        t.rt(60)

t.done()
