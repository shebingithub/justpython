# sketching

# from sketchpy import canvas
# import turtle
# obj = canvas.sketch_from_svg("PathToImage.svg")
# t = turtle.Turtle()
# t.penup()

# t.pendown()
# obj.draw()


# CALENDER

# DRAWINGTURTLE


import turtle

# shebi1 = [  [(50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50)],
#   [(50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50)]
# ]
# shebi2 = [  [(50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50)],
#   [(50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50)]
# ]
# shebi3 =  [  [(50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50)],
#   [(50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50)]
# ]
# shebi4 =  [  [(50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50)],
#   [(50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50), (50, 50)]
# ]
shebi1 = [[(-40, 120), (-70, 260), (-130, 230), (-170, 200), (-170, 100), (-160, 40), (-170, 10), (-150, -10), (-140, 10),
           (-40, -20), (0, -20)],
          [(0, -20), (40, -20), (140, 10), (150, -10), (170, 10), (160, 40), (170, 100), (170, 200), (130, 230), (70, 260),
           (40, 120), (0, 120)]]
shebi2 = [[(-40, -30), (-50, -40), (-100, -46), (-130, -40), (-176, 0), (-186, -30), (-186, -40), (-120, -170), (-110, -210),
           (-80, -230), (-64, -210), (0, -210)],
          [(0, -210), (64, -210), (80, -230), (110, -210), (120, -170), (186, -40), (186, -30), (176, 0), (130, -40),
           (100, -46), (50, -40), (40, -30), (0, -30)]]
shebi3 = [[(-60, -220), (-80, -240), (-110, -220), (-120, -250), (-90, -280), (-60, -260), (-30, -260), (-20, -250),
           (0, -250)],
          [(0, -250), (20, -250), (30, -260), (60, -260), (90, -280), (120, -250), (110, -220), (80, -240), (60, -220),
           (0, -220)]]

turtle.hideturtle()
turtle.bgcolor('#ba161e')  # Dark Red
turtle.setup(500, 600)
turtle.title("SHEBI'S  AI IRONMAN")
shebi1Goto = (0, 120)
shebi2Goto = (0, -30)
shebi3Goto =  (120,0)
# shebi4Goto = (0, -360)
turtle.speed(2)


def logo(a, b):
    turtle.penup()
    turtle.goto(b)
    turtle.pendown()
    turtle.color("#FFD700")  # Light Yellow
    turtle.begin_fill()

    for i in range(len(a[0])):
        x, y = a[0][i]
        turtle.goto(x,y)
    for i in range(len(a[1])):
        x, y = a[1][i]
        turtle.goto(x, y)
    turtle.end_fill()


logo(shebi1, shebi1Goto)
logo(shebi2, shebi2Goto)
logo(shebi3, shebi3Goto)
# logo(shebi4, shebi4Goto)
turtle.hideturtle()
turtle.done()


# MENTROW DRAWING

# import turtle

# # Function to draw a letter 'M'
# def draw_m():
#     turtle.left(90)
#     turtle.forward(100)
#     turtle.right(135)
#     turtle.forward(70)
#     turtle.left(90)
#     turtle.forward(70)
#     turtle.right(135)
#     turtle.forward(100)
#     turtle.left(90)

# # # Function to draw a letter 'E'
# def draw_e():
#     turtle.forward(70)
#     turtle.backward(70)
#     turtle.left(90)
#     turtle.forward(50)
#     turtle.right(90)
#     turtle.forward(70)
#     turtle.backward(70)
#     turtle.left(90)
#     turtle.forward(50)
#     turtle.right(90)
#     turtle.forward(70)
#     turtle.backward(70)
#     # turtle.right(-90)  (EDIT FROM HERE )

# # # Function to draw a letter 'N'
# def draw_n():
#     turtle.left(90)
#     turtle.forward(100)
#     turtle.right(150)
#     turtle.forward(110)
#     turtle.left(150)
#     turtle.forward(100)
#     turtle.backward(100)
#     turtle.right(90)

# # # Function to draw a letter 'T'
# def draw_t():
#     turtle.forward(100)
#     turtle.backward(50)
#     turtle.right(90)
#     turtle.forward(100)
#     turtle.left(90)

# # Function to draw a letter 'O'
# def draw_o():
#     turtle.circle(50)

# # Function to draw a letter 'R'
# def draw_r():
#     turtle.left(90)
#     turtle.forward(100)
#     turtle.right(90)
#     turtle.forward(50)
#     turtle.right(90)
#     turtle.forward(50)
#     turtle.right(90)
#     turtle.forward(50)
#     turtle.right(180)
#     turtle.left(-45)
#     turtle.forward(70)
#     turtle.backward(70)

# # Function to draw a letter 'W'
# import turtle

# def draw_w():
#     turtle.left(-60)
#     turtle.forward(100)
#     turtle.right(-120)
#     turtle.forward(100)
#     turtle.left(-120)
#     turtle.forward(100)
#     turtle.right(-120)
#     turtle.forward(100)
#     turtle.left(-60)

# # Set up the turtle
# turtle.speed(2)

# # Starting position for drawing the word "MENTORW"
# x_start = -250
# y_start = 0

# # Move turtle to the starting position
# turtle.penup()
# turtle.goto(x_start, y_start)
# turtle.pendown()

# # Draw each letter in "MENTORW"
# draw_m()
# turtle.penup()
# turtle.forward(50)
# turtle.pendown()
# draw_e()
# turtle.penup()
# turtle.forward(50)
# turtle.pendown()
# draw_n()
# turtle.penup()
# turtle.forward(50)
# turtle.pendown()
# draw_t()
# turtle.penup()
# turtle.forward(50)
# turtle.pendown()
# draw_o()
# turtle.penup()
# turtle.forward(50)
# turtle.pendown()
# draw_r()
# turtle.penup()
# turtle.forward(50)
# turtle.pendown()
# draw_w()

# # Hide the turtle
# turtle.hideturtle()

# # Keep the window open
# turtle.done()
