# print("Hello from lesson 16")

import turtle
window = turtle.Screen()
window.setup(width = 600, height = 400)
t = turtle.Turtle()
t.shape("turtle")
t.fillcolor("green")
t.pendown()
for i in range(4):
    t.forward(100)
    t.right(90)
t.penup()
window.mainloop()