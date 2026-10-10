from turtle import *


def colors():
    t_i.penup()
    t_i.goto(-250, 150)
    t_i.pendown()
    t_i.color('green')
    t_i.begin_fill()
    for i in range(4):
        t_i.forward(35)
        t_i.right(90)
    t_i.end_fill()
    t_i.penup()
    t_i.goto(-210, 125)
    t_i.pendown()
    t_i.write('G', font = ('Arial', 16, 'normal'))

    t_i.penup()
    t_i.goto(-250, 100)
    t_i.pendown()
    t_i.color('red')
    t_i.begin_fill()
    for i in range(4):
        t_i.forward(35)
        t_i.right(90)
    t_i.end_fill()
    t_i.penup()
    t_i.goto(-210, 75)
    t_i.pendown()
    t_i.write('R', font = ('Arial', 16, 'normal'))

    t_i.penup()
    t_i.goto(-250, 50)
    t_i.pendown()
    t_i.color('purple')
    t_i.begin_fill()
    for i in range(4):
        t_i.forward(35)
        t_i.right(90)
    t_i.end_fill()
    t_i.penup()
    t_i.goto(-210, 25)
    t_i.pendown()
    t_i.write('P', font = ('Arial', 16, 'normal'))

    t_i.penup()
    t_i.goto(-250, 0)
    t_i.pendown()
    t_i.color('blue')
    t_i.begin_fill()
    for i in range(4):
        t_i.forward(35)
        t_i.right(90)
    t_i.end_fill()
    t_i.penup()
    t_i.goto(-210, -25)
    t_i.pendown()
    t_i.write('B', font = ('Arial', 16, 'normal'))

    t_i.penup()
    t_i.goto(-250, -50)
    t_i.pendown()
    t_i.color('yellow')
    t_i.begin_fill()
    for i in range(4):
        t_i.forward(35)
        t_i.right(90)
    t_i.end_fill()
    t_i.penup()
    t_i.goto(-210, -75)
    t_i.pendown()
    t_i.write('Y', font = ('Arial', 16, 'normal'))

    t_i.penup()
    t_i.goto(-250, -100)
    t_i.pendown()
    t_i.color('light blue')
    t_i.begin_fill()
    for i in range(4):
        t_i.forward(35)
        t_i.right(90)
    t_i.end_fill()
    t_i.penup()
    t_i.goto(-210, -125)
    t_i.pendown()
    t_i.write('L', font = ('Arial', 16, 'normal'))

    t_i.penup()
    t_i.goto(-250, -150)
    t_i.pendown()
    t_i.color('white')
    t_i.begin_fill()
    for i in range(4):
        t_i.forward(35)
        t_i.right(90)
    t_i.end_fill()
    t_i.penup()
    t_i.goto(-210, -175)
    t_i.pendown()
    t_i.write('W', font = ('Arial', 16, 'normal'))
    t_i.penup()

    

def draw_line():
    y1 = 150
    widths = 5

    t_i.goto(190, y1)
    t_i.pendown()
    t_i.width(widths)
    t_i.color('gray')
    t_i.setheading(90)
    t_i.forward(10)
    t_i.penup()
    y1 -= 20
    widths +=  5

    t_i.goto(190, y1)
    t_i.pendown()
    t_i.width(widths)
    t_i.color('gray')
    t_i.setheading(90)
    t_i.forward(10)
    t_i.penup()
    y1 -= 20
    widths +=  5

    y1 -= 5
    t_i.goto(190, y1)
    t_i.pendown()
    t_i.width(widths)
    t_i.color('gray')
    t_i.setheading(90)
    t_i.forward(10)
    t_i.penup()
    widths += 5

    y1 -= 30
    t_i.goto(190, y1)
    t_i.pendown()
    t_i.width(widths)
    t_i.color('gray')
    t_i.setheading(90)
    t_i.forward(10)
    t_i.penup()

    y1 -= 35
    t_i.goto(190, y1)
    t_i.pendown()
    t_i.width(widths)
    t_i.color('gray')
    t_i.setheading(90)
    t_i.forward(10)
    t_i.penup()

    y1 = 150

    t_i.goto(200, y1)
    t_i.write('1', font = ('Ariel', 10, 'normal'))
    y1 -= 20

    t_i.goto(200, y1)
    t_i.write('2', font = ('Ariel', 10, 'normal'))
    y1 -= 20

    t_i.goto(200, y1)
    t_i.write('3', font = ('Ariel', 10, 'normal'))
    y1 -= 30

    t_i.goto(200,y1)
    t_i.write('4', font = ('Ariel', 10, 'normal'))
    y1 -= 39

    t_i.goto(200,y1)
    t_i.write('5', font = ('Ariel', 10, 'normal'))

    t_i.width(5)
    t_i.setheading(90)


def screen_color():

    t_i.penup()
    t_i.goto(200, -180)
    t_i.pendown()
    t_i.color('white', 'black')
    t_i.begin_fill()
    for i in range(4):
        t_i.forward(35)
        t_i.right(90)
    t_i.end_fill()
    t_i.penup()
    t_i.goto(-210, 75)
    t_i.pendown()
    

    t_i.penup()
    t_i.goto(150, -180)
    t_i.pendown()
    t_i.color('black', 'white')
    t_i.begin_fill()
    for i in range(4):
        t_i.forward(35)
        t_i.right(90)
    t_i.end_fill()
    t_i.penup()
    t_i.goto(165, -130)
    

    t_i.color('black')
    t_i.write('D', font = ('Arial', 16, 'normal'))
    t_i.goto(213, -130)
    t_i.write('N', font = ('Arial', 16, 'normal'))
    

t_i = Turtle()
t_i.speed(0)

colors()
draw_line()
screen_color()

t_i.hideturtle()
