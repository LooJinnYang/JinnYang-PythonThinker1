# print("Hello from lesson 16")

import turtle

def drawShape(times, length):
    ang = 360 / times
    t.pendown()
    for i in range(times):
        t.forward(length)
        t.right(ang)
    t.penup()
window = turtle.Screen()
window.setup(width = 600, height = 400)
t = turtle.Turtle()
t.shape("turtle")
t.fillcolor("green")
times = int(input("How many sides does your polygon have: "))
drawShape(times)
window.mainloop()