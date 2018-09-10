from turtle import *

speed(0)
def draw_star(x, y, length ):
    penup()
    setpos(x,y)
    pendown()    
    for i in range(5):
        forward(length)
        right(144)
        
draw_star(10,10,100)
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)      

mainloop()