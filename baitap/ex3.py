from turtle import *

speed(0)
def  draw_square(length ,square_color):
    color(square_color)
    for i in range(4):
        forward(length)
        left(90)
    
    mainloop()
draw_square(50,'red')