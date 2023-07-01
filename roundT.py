import turtle
color=["red","blue","Green","yellow","pink","orange","skyblue","purple"]
t=turtle.pen()
turtle.speed(0)
turtle.bgcolor("black")
for x in range(360):
    turtle.pencolor(color[x%8])
    turtle.width(x/100+1)
    turtle.forward(x)
    turtle.left(55)