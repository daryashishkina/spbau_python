import turtle as tl

def draw_fractal(size):
    if size >= 4:
        tl.pensize(max(size / 60, 1))
        tl.left(30)
        tl.forward(size)
        tl.left(60)
        tl.forward(size)
        tl.left(120)
        tl.forward(size)
        tl.left(120)
        draw_fractal(size / 1.4)
        tl.right(60)
        tl.penup()
        tl.backward(size)
        tl.pendown()
    else:
        tl.pensize(3)
        
size = 120

tl.delay(1)  # уменьшение задержки для скорости
tl.speed(0)
tl.penup()
tl.color('orange')
tl.bgcolor('black')
tl.pendown()

for i in range(1,6):
    draw_fractal(size)
    tl.penup()
    tl.goto(0,0)
    tl.pendown()
    tl.setheading(60*i)
draw_fractal(size)
tl.done()