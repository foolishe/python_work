import turtle as t
import random,time
def drawcap():
    t.penup();t.fd(5)
def drawline(draw):
    t.pencolor(random.choice(['#ff2222','#ff00ff','#7529ff','#0088ff','#ff00ff']))
    drawcap()
    t.pendown() if draw else t.penup()
    t.fd(40)
    drawcap()
    t.left(90)
def drawchar(draw):
   
    drawline(True)if draw in (2,3,4,5,6,8,9) else  drawline(False)
    drawline(True)if draw in (0,1,2,3,4,7,8,9)  else drawline(False)
    drawline(True)if draw in (0,2,3,5,6,7,8,9)else drawline(False)
    drawline(True)if draw in (0,4,5,6,8,9) else drawline(False)
    t.right(90)
    drawline(True)if draw in (0,2,4,6,8,)else drawline(False)
    drawline(True)if draw in (0,2,3,5,6,8,9) else drawline(False)
    drawline(True)if draw in (0,1,3,4,5,6,7,8,9)else  drawline(False)
    t.seth(0)
    t.penup()
    t.fd(20)
def drawsevenlight(a):
    t.penup()
    t.goto(-350,0)
    t.setup(800,350,300,300)
    for i in range(len(a)):
        if a[i]=='=':
            t.write('年',font=('Arial',17,'normal'))
            t.fd(30)
        elif a[i]=='-':
            t.write('月',font=('Arial',15,'normal'))
            t.fd(20)
        elif a[i]=='+':
            t.write('日',font=('Arial',15,'normal'))
        else:
            drawchar(eval(a[i]))
    t.penhideturtle()        
a=time.strftime('%Y=%m-%d+',time.gmtime())
drawsevenlight(a)
        
   
   
