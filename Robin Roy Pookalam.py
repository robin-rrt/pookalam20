import turtle

turtle.bgcolor("black")


turtle.pensize(3)
turtle.speed(0)

#first circle
turtle.color("pink", "yellow")
turtle.penup()
turtle.right(90)
turtle.forward(200)
turtle.left(90)
turtle.pendown()
turtle.begin_fill()
turtle.circle(200)
turtle.end_fill()
turtle.penup()
turtle.left(90)
turtle.forward(20)
turtle.right(90)

#second circle
turtle.color("purple", "purple")
turtle.begin_fill()
turtle.pendown()
turtle.circle(180)
turtle.end_fill()


turtle.penup()
turtle.left(90)
turtle.forward(180)
turtle.right(90)

#zigzag pattern on second circle
turtle.pendown()
turtle.color("pink")
turtle.begin_fill()
for i in range(36):
    turtle.left(10)
    turtle.forward(127.27)
    turtle.left(90)
    turtle.forward(127.27)
    turtle.left(90)
    turtle.forward(127.27)
    turtle.left(90)
    turtle.forward(127.27)
    turtle.left(90)
turtle.end_fill()

#third circle
turtle.penup()
turtle.right(90)
turtle.forward(165)
turtle.left(90)
turtle.pendown()
turtle.color("dark red", "dark red")
turtle.begin_fill()
turtle.circle(165)
turtle.end_fill()
turtle.penup()

turtle.left(90)
turtle.forward(165)
turtle.right(90)

#circle spirograph
turtle.pendown()
turtle.color("orange", "orange")
turtle.begin_fill()
for i in range(6):
    turtle.left(60)
    turtle.circle(80)
turtle.end_fill()
    
    

#star shape part1
turtle.begin_fill()
turtle.color("purple", "purple")
turtle.left(45)
for i in range(6):
    turtle.left(60)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()

#star shape part 2
turtle.begin_fill()
turtle.right(10)
for i in range(6):
    turtle.circle(65)
    turtle.left(60)
turtle.end_fill()

turtle.color("yellow")
turtle.right(45)


#ztar pattern 
turtle.pendown()
turtle.color("green", "green")

for i in range(6):
    turtle.begin_fill()
    turtle.left(60)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.end_fill()

#ztar pattern 2
turtle.pendown()
turtle.color("pink", "pink")

for i in range(6):
    turtle.begin_fill()
    turtle.left(60)
    turtle.forward(58)
    turtle.left(90)
    turtle.forward(58)
    turtle.left(90)
    turtle.forward(58)
    turtle.left(90)
    turtle.forward(58)
    turtle.left(90)
    turtle.end_fill()

#ztar pattern 3
turtle.pendown()
turtle.color("magenta", "magenta")

for i in range(6):
    turtle.begin_fill()
    turtle.left(60)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.end_fill()
#fourth circle
turtle.penup()
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.pendown()
turtle.color("green", "green")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()
turtle.penup()

turtle.left(90)
turtle.forward(50)
turtle.right(90)

#fourth circle
turtle.penup()
turtle.right(90)
turtle.forward(47)
turtle.left(90)
turtle.pendown()
turtle.color("yellow", "yellow")
turtle.begin_fill()
turtle.circle(47)
turtle.end_fill()
turtle.penup()

turtle.left(90)
turtle.forward(47)
turtle.right(90)

#fifth circle
turtle.penup()
turtle.right(90)
turtle.forward(20)
turtle.left(90)
turtle.pendown()
turtle.color("dark red", "dark red")
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()
turtle.penup()

turtle.left(90)
turtle.forward(20)
turtle.right(90)

#sixth circle
turtle.penup()
turtle.right(90)
turtle.forward(15)
turtle.left(90)
turtle.pendown()
turtle.color("white", "white")
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()
turtle.penup()

turtle.left(90)
turtle.forward(15)
turtle.right(90)

#centre circle
turtle.penup()
turtle.right(90)
turtle.forward(5)
turtle.left(90)
turtle.pendown()
turtle.color("red", "red")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()
turtle.penup()

turtle.left(90)
turtle.forward(5)
turtle.right(90)

#dot
turtle.penup()
turtle.right(90)
turtle.forward(1)
turtle.left(90)
turtle.pendown()
turtle.color("white", "white")
turtle.begin_fill()
turtle.circle(1)
turtle.end_fill()
turtle.penup()

turtle.left(90)
turtle.forward(1)
turtle.right(90)

turtle.hideturtle()

turtle.done()
