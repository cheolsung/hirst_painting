# import colorgram
#
# n_colors=10
# e_colors=colorgram.extract('R.png',n_colors)
#
# colors=[]
#
# for x in e_colors:
#     colors.append((x.rgb.r,x.rgb.g,x.rgb.b))

from turtle import Turtle, Screen
import random

colors = [(252, 251, 244), (184, 227, 235), (237, 29, 85), (196, 216, 59), (252, 254, 253), (242, 117, 125), (251, 225, 230), (246, 156, 168), (236, 16, 74), (190, 212, 38)]

sc=Screen()
sc.colormode(255)

tt=Turtle()
tt.hideturtle()

for i in range(15):
    tt.penup()
    tt.goto(-200,-300+i*50)
    for _ in range(10):
        tt.pendown()
        tt.dot(20,random.choice(colors))
        tt.penup()
        tt.setx(tt.xcor()+50)

sc.exitonclick()