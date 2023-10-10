import turtle
import random
colors = ('red','blue','green','purple','gray','black')
kaks = turtle.Turtle()
def formas():
    for eb in range(6):
        kaks.forward(25)
        kaks.right(60)

for at in range(6):
    for me in range(2):
        kaks.color(random.choice(colors))
        for u in range(4):
            formas
            kaks.penup()
            kaks.forward(50)
            kaks.pendown()
        kaks.penup()
        kaks.back(25)
        kaks.left(60)
        kaks.penup()
        kaks.forward(50)
        kaks.pendown()
        kaks.right(60)
