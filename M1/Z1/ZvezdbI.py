import turtle

turtle.ht()

turtle.penup()
turtle.goto(-150, 0)
turtle.pendown()

number_of_corners = 5
color_shape = "red"
turtle.color(color_shape)
turtle.begin_fill()

for i in range(number_of_corners):
    turtle.forward(100)
    turtle.right(360 * 2 / number_of_corners)
turtle.end_fill()

turtle.penup()
turtle.forward(100)
turtle.pendown()

number_of_corners = 8
color_shape = "red"
turtle.color(color_shape)
turtle.begin_fill()

for i in range(number_of_corners):
    turtle.forward(100)
    turtle.right(360 * 3 / number_of_corners)
turtle.end_fill()

turtle.penup()
turtle.forward(100)
turtle.pendown()
number_of_corners = 16
color_shape = "red"
turtle.color(color_shape)
turtle.begin_fill()

for i in range(number_of_corners):
    turtle.forward(100)
    turtle.right(360 * 7 / number_of_corners)
turtle.end_fill()




# turtle.mainloop()
# turtle.done()
turtle.done()
