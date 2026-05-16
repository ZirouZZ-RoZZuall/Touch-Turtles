from turtle import *
from random import *
from time import *

def square():
    speed(10)
    color('grey')
    pensize(10)
    penup()
    goto(-205,-205)
    pendown()
    for i in range(4):
        forward(400)
        left(90)
    hideturtle()


t1 = Turtle()
t2 = Turtle()
t3 = Turtle()

square()

def specifications(t,col,shapes,tilt):
    t.color(col)
    t.shape(shapes)
    t.goto(0,0)
    t.left(tilt)
    t.pendown()

specifications(t1,'blue','turtle',0)
specifications(t2,'green','turtle',120)
specifications(t3,'red','turtle',240)

def move(t):
    t.pensize(5)
    t.speed(10)
    t.forward(randint(2,5))

def random_move(t):
    t.penup()
    t.goto(randint(-100,100),randint(-100,100))
    t.left(randint(0,180))
    t.pendown()

def catch1(a,b):
    random_move(t1)

def catch2(a,b):
    random_move(t2)

def catch3(a,b):
    random_move(t3)

def write_end():
    t1.clear()
    t2.clear()
    t3.clear()
    penup()
    goto(-60,0)
    color('orange')
    write('Good Bye!', font = ('Arial',20,'bold'))       

# ('A!', font = ('Arial',10,'bold'))

def gameFinished(t1,t2,t3):
    t1_outside = abs(t1.xcor()) > 200 or abs(t1.ycor()) > 200
    t2_outside = abs(t2.xcor()) > 200 or abs(t2.ycor()) > 200
    t3_outside = abs(t3.xcor()) > 200 or abs(t3.ycor()) > 200
    is0utside = t1_outside or t2_outside or t3_outside
    return is0utside


t1.onclick(catch1)
t2.onclick(catch2)
t3.onclick(catch3)

while gameFinished(t1,t2,t3) != True:
    move(t1)
    move(t2)
    move(t3)

write_end()
    
exitonclick()
