import turtle
import random
t = turtle.Turtle()

wn = turtle.Screen()
wn.setup(height = 600, width = 600)
t.speed(5)

t.penup()
t.goto(-80, 80)

t.pendown()
w = 0
while w < 4:
    t.forward(160)
    t.right(90)
    w = w + 1
    
t.penup()


#------------------------------------------------------------------


t.goto(0, 0)
t.pendown()

a = 0
b = 0
c = 0
d = 0

x = 0
y = 0

while True:
    rand = random.randrange(1, 5)

    if rand == 1 and a < 2:   #r
        t.forward(40)
        a = a + 1
        c = c - 1
        x = x + 40

    elif a == 2:
        t.right(180)
        t.forward(40)
        t.right(180)
        a = a - 1
        c = c + 1
        x = x - 40

    if rand == 2 and b < 2:   #d
        t.right(90)
        t.forward(40)
        t.left(90)
        b = b + 1 
        d = d - 1
        y = y - 40

    elif b == 2:
        t.left(90)
        t.forward(40)
        t.right(90)
        b = b - 1  
        d = d + 1
        y = y + 40

    if rand == 3 and c < 2:   #l
        t.right(180)
        t.forward(40)
        t.right(180)
        c = c + 1
        a = a - 1
        x = x - 40

        point.append(1)
    elif c == 2:
        t.forward(40)
        c = c - 1
        a = a + 1
        x = x + 40
    
    if rand == 4 and d < 2:   #u
        t.left(90)
        t.forward(40)
        t.right(90)
        d = d + 1
        b = b - 1
        y = y + 40

    elif d == 2:
        t.right(90)
        t.forward(40)
        t.left(90)
        d = d - 1
        b = b + 1
        y = y - 40
    
    print ("turtle is at:", x, y)
