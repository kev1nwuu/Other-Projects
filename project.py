import turtle as t
import random

def changePenColor(): # set pen color change
    t.colormode(255) # color format
    a = random.randint(100,255) # set a color and color in range 
    b = random.randint(100,255)
    c = random.randint(100,255)
    t.pencolor(a,b,c)  # pen colors

def shape(): # shape going to Draw
    t.pensize(10) # set pensize
    while True: # set a loop
        changePenColor() # Bring in changepencolor to here(the equation for changing the pen color set before)
        t.fd(200)
        t.speed(10)
        t.right(111)

#shape()




# Question 2 
import turtle as t
import random

def changePenColor(): #set color change
    t.colormode(255)
    a = random.randint(100,255)
    b = random.randint(100,255)
    c = random.randint(100,255)
    t.pencolor(a,b,c)

def fd():   # set moving forward
    t.fd(100)

def fdr():   # set turn right 90 degree and moving forward
    t.right(90)
    t.fd(100)

def fdl():  # set turn left 90 degree and movinng forward
    t.left(90)
    t.fd(100)

def bk():  # set moving backward
    t.bk(100)
    

def onkey(): #  Set keyboard operation
    t.pensize(10) 
    while True:  # using loop 
        changePenColor() 
        t.onkey(fd,"Up") # press up going forward 
        t.onkey(fdr,"Right")
        t.onkey(fdl,"Left")
        t.onkey(bk,"Down")
        t.listen()

onkey()