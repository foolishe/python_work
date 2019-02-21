import turtle,random
def koch(size,n):
    
    if n==0:
        turtle.pencolor(random.choice(["#ff0022","#33ffff","#778822","pink",'yellow']))
        turtle.fd(size)
    else:
        for angle in[0,60,-120,60]:
##            turtle.pencolor(random.choice(["#ff0022","#33ffff","#778822"]))
            turtle.left(angle)
            koch(size/4,n-1)
def main():
    turtle.setup(600,600)
    turtle.penup()
    turtle.goto(-200,100)
    turtle.pendown()
    turtle.pensize(2)
    level=3
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    turtle.hideturtle()
    

main()
