# print("Hello from lesson 14")

# import turtle
# window = turtle.Screen()
# window.setup(width = 600, height = 400)
# window.mainloop()

import turtle

# Step 2: Create screen and set up 400x400 size
screen = turtle.Screen()
screen.setup(width=400, height=400)

# Step 3: Define x and y limits (half of 400 because (0,0) is center)
x_limit = 200
y_limit = 200

# Step 4: Create turtle and move to bottom-left corner
t = turtle.Turtle()
t.penup()
t.goto(-x_limit, -y_limit)
t.pendown()
t.speed(1)

# Step 5: Move around the edges
while True:
    while t.xcor() < x_limit:
        t.forward(1)
    t.left(90)

    while t.ycor() < y_limit:
        t.forward(1)
    t.left(90)

    while t.xcor() > -x_limit:
        t.forward(1)
    t.left(90)

    while t.ycor() > -y_limit:
        t.forward(1)
    t.left(90)