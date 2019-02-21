#draw a sanke
from turtle import*
setup(1000,500,100,100)
penup()
fd(-400)
pendown()
pensize(45)
pencolor("yellow")
seth(-45)
for i in range(5):
    circle(50,90)
    circle(-50,90)
seth(0)
fd(50)
pensize(40)
circle(90,150)
pensize(35)
seth(-190)
fd(20)
pensize(25)
fd(20)
pensize(10)
fd(60)
done
