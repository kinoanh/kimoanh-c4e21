from turtle import *

speed(0)
def  draw_square(length ,square_color):
    color(square_color)
    for i in range(4):
        forward(length)
        left(90)

for j in range(30):
    draw_square(j * 5, 'red')
    left(17)
    penup()
    forward(j * 2)
    pendown()

    mainloop()

