# print("Hello from lesson 16")

?
#        print("LOL")
#        break

# import turtle

# window = turtle.Screen()
# window.setup(width = 600, height = 400)
# t = turtle.Turtle()
# t.shape("turtle")
# t.fillcolor("green")

# def drawShape(times, length):
#     ang = 360 / times
#     t.pendown()
#     for i in range(times):
#         t.forward(length)
#         t.right(ang)
#     t.penup()

# times = int(input("How many sides does your polygon have: "))
# length = int(input("How long does your turtle move: "))

# drawShape(times, length)
# window.mainloop()

import turtle

def setp(length, hight):
    screen = turtle.Screen()
    screen.setup(width = length, height = hight)
    return screen

def create():
    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color("blue")
    ball.penup()
    return ball

length = 300
hight = 500
screen = setp(length, hight)
ball = create()

screen.mainloop()