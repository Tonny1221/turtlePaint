from turtle import *
from interface_paint import *


t = Turtle()
t.color('red')
t.width(5)
t.shape('circle')
t.pendown()
t.speed(0)
scr = t.getscreen()

def setWidth_1():
    t.width(5)

def setWidth_2():
    t.width(10)

def setWidth_3():
    t.width(15)

def setWidth_4():
    t.width(20)

def setWidth_5():
    t.width(25)

def black_color():
    scr.bgcolor('black')
def white_color():
    scr.bgcolor('white')


def c_clear():
    t.clear()
def draw(x,y):
    t.goto(x, y)
def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def stepright():
    t.goto(t.xcor() + 5, t.ycor())
def stepleft():
    t.goto(t.xcor() - 5, t.ycor())
def stepup():
    t.goto(t.xcor(), t.ycor() +5)
def stepdown():
    t.goto(t.xcor(), t.ycor() -5)


def beginFill():
    t.begin_fill()
def endFill():
    t.end_fill()



def setGreen():
    t.color('green')
def setRed():
    t.color('red')
def setpurple():
    t.color('purple')
def setblue():
    t.color('blue')
def setyellow():
    t.color('yellow')
def setlb():
    t.color('light blue')
def setwhite():
    t.color('white')


scr.listen()
scr.onkey(setGreen, 'g')
scr.onkey(setRed,'r')
scr.onkey(setpurple ,'p')
scr.onkey( setlb,'l')
scr.onkey( setyellow,'y')
scr.onkey( setwhite,'w')
scr.onkey( setblue,'b')
scr.onkey(stepright,'right')
scr.onkey(stepleft,'left')
scr.onkey(stepup,'up')
scr.onkey(stepdown,'down')
scr.onkey(beginFill, 'q')
scr.onkey(endFill, 'e')
scr.onkey(c_clear, 'c')

scr.onkey(setWidth_1, '1')
scr.onkey(setWidth_2, '2')
scr.onkey(setWidth_3, '3')
scr.onkey(setWidth_4, '4')
scr.onkey(setWidth_5, '5')

scr.onkey(black_color, 'n')
scr.onkey(white_color, 'd')


scr.onscreenclick(move)
t.ondrag(draw)
