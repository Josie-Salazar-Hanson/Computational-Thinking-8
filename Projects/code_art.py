import turtle

t=turtle.Turtle()

t.goto(0, 0)
t.color("purple")

colors=["pink", "blue", "purple"]
for i in range (72):
    t.forward(100+4*i)
    t.color(colors[i%3])
    t.left (120)
    t.speed (9)
#The speed is really fast
#the triangle is pink blue and purple
#and it makes 72 triangles
turtle.exitonclick()


