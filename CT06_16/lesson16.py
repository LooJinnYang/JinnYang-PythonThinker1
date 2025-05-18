# print("Hello from lesson 16")

import turtle

def drawShape(imes):
    ang = 360 / imes

window = turtle.Screen()
window.setup(width = 600, height = 400)
t = turtle.Turtle()
t.shape("turtle")
t.fillcolor("green")
t.pendown()
for i in range(8):
    t.forward(100)
    t.right(45)
t.penup()
window.mainloop()