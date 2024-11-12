import turtle

print(range(4))

number_of_corners = int(input("How many corners do you want? "))
color_shape=input("What color do you want? ")
turtle.color(color_shape)
turtle.begin_fill()

for i in range(number_of_corners):
    turtle.forward(100)
    turtle.left(360/number_of_corners)
turtle.end_fill()

# number_of_corners = 4
#
# for i in range(number_of_corners):
#     turtle.forward(100)
#     turtle.left(360/number_of_corners)

# turtle.mainloop()
# turtle.done()
turtle.done()
