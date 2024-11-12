import turtle as t


def triangular_maze():
    t.colormode(255)
    t.color('red')
    t.rt(60)
    for i in range(6, 100, 6):
        t.forward(i)
        t.rt(120)


def triangular_maze2():
    t.color('red')
    t.rt(60)
    for i in range(6, 100, 12):
        t.forward(i)
        t.rt(120)


def hexagonal_maze(size=3):
    t.pensize(size)
    t.color('red')
    t.rt(60)
    for i in range(4, 80, 4):
        t.forward(i)
        t.rt(60)


def quadrangular_maze(size=4, pattern=[4, 56, 4]):  # 52, 0, -4
    t.pensize(size)
    t.color('blue')
    t.ht()
    for i in range(pattern[0], pattern[1], pattern[2]):
        t.forward(i)
        t.rt(90)


def six_round_petals(radius=40):
    radius = radius
    t.pensize(5)
    t.color("#FFA500")
    t.fillcolor("#A200FF")
    for i in range(6):
        t.begin_fill()
        t.circle(radius)
        t.end_fill()
        t.rt(60)


def six_round_petals2(radius=40):
    radius = radius
    t.pensize(5)
    t.color("#FFA500")
    t.fillcolor("#A200FF")
    for i in range(4):
        for j in range(6):
            t.begin_fill()
            t.circle(radius)
            t.end_fill()
            t.rt(60)
        radius = radius - 10


if __name__ == '__main__':
    # triangular_maze()
    # triangular_maze2()
    # hexagonal_maze()
    # hexagonal_maze(6)

    # quadrangular_maze()
    # t.rt(270)
    # quadrangular_maze(4, [52, 0, -4])

    # six_round_petals()
    # six_round_petals(30)
    # six_round_petals(20)
    # six_round_petals(10)

    six_round_petals2()

    # pen = t.Turtle()
    # pen.shape("circle")
    # pen.shapesize(10, 4, 1)
    # pen.fillcolor("white")


t.done()
