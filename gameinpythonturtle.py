import turtle
import math
import random
import os

#set up screen

window=turtle.Screen()
window.tracer(3)
window.setup(570,570)
window.title("Turtle's Hunt")
window.bgcolor("white")
window.bgpic("exam.png")





#draw border
mypen= turtle.Turtle()
mypen.penup()
mypen.color("white")
mypen.setposition(-270,-270)
mypen.pendown()
mypen.pensize(3)
for i in range(4):
    mypen.forward(540)
    mypen.left(90)
mypen.hideturtle()


player=turtle.Turtle()
player.color("lightblue")
player.shape("turtle")
player.penup()
player.speed(0)
player.turtlesize(1.5,1.5)


score=0


maxgoons=6
goon=[]

for c in range(maxgoons):
    goon.append(turtle.Turtle())
    goon[c].color("yellow")
    goon[c].shape("circle")
    goon[c].penup()
    goon[c].setposition(random.randint(-250,250),random.randint(-250,250))
    goon[c].speed(0)
    goon[c].turtlesize(.5,.5)


def tl():
    player.left(30)

def tr():
    player.right(30)

def increasespeed():
    global speed
    speed+=1;


def iscollision(t1,t2):
    d=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if(d<25):
        return True
    else:
        return False

turtle.listen()
turtle.onkey(tl,"Left")
turtle.onkey(tr,"Right")
turtle.onkey(increasespeed,"Up")

speed=1
speedg=1


while(True):
    player.forward(speed)
    
    if(player.xcor()>270 or player.xcor()<-270):
        player.right(180)
        
    if(player.ycor()>270 or player.ycor()<-270):
        player.left(180)

    #collision
    


    for c in range(maxgoons):
        goon[c].forward(speedg)
        
        if(goon[c].xcor()>270 or goon[c].xcor()<-270):
            goon[c].right(180)
            
        if(goon[c].ycor()>270 or goon[c].ycor()<-270):
            goon[c].left(180)

        if(iscollision(player,goon[c])):
            goon[c].setposition(random.randint(-250,250),random.randint(-250,250))
            goon[c].right(random.randint(0,360))
            #os.system("afplay collision.mp36")
            score+=1
            mypen.undo()
            mypen.penup()
            mypen.setposition(160,230)
            scorestring="Score : %s" %score
            mypen.write(scorestring,False,align="Left",font=("Arial",14,"normal"))




delay=input("Press Enter ")
