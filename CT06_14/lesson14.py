# print("Hello from lesson 14")

# import turtle
# window = turtle.Screen()
# window.setup(width = 600, height = 400)
# window.mainloop()

# import turtle
# window = turtle.Screen()
# window.setup(width = 600, height = 400)
# t = turtle.Turtle()
# t.shape("turtle")
# t.fillcolor("green")
# window.mainloop()

import turtle
window = turtle.Screen()
window.setup(width = 600, height = 400)
t = turtle.Turtle()
t.shape("turtle")
t.fillcolor("green")
t.forward(100)
window.mainloop()

import turtle
window = turtle.Screen()
window.setup(width = 600, height = 400)
t = turtle.Turtle()
t.shape("turtle")
t.fillcolor("green")
for i in range(4):
    t.forward(100)
    t.seth(90)
window.mainloop()