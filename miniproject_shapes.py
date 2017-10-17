import turtle

def draw_triangle(some_turtle):
        some_turtle.left(35)
        some_turtle.forward(50)
        some_turtle.right(35)
        some_turtle.forward(50)
        some_turtle.right(145)
        some_turtle.forward(50)
        some_turtle.right(35)
        some_turtle.forward(50)
        some_turtle.right(10)

    
def draw_figures():
    window = turtle.Screen()
    window.bgcolor("yellow")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("purple")
    brad.speed(20)

#write Initials
    brad.pu()
    brad.setpos(0,0)
    brad.pd()
    brad.seth(90)

    draw_initials(brad)


#draw a triangle

    brad.pu()
    brad.setpos(-200,0)
    brad.pd()
    
    for i in range(1,37):
            draw_triangle(brad)
    brad.right(270)
    brad.forward(200)

    #draw the initials

 
    
    window.exitonclick()

def draw_initials(some_turtle):
    some_turtle.pencolor("blue")
    some_turtle.forward(200)
    some_turtle.right(135)
    some_turtle.forward(100)
    some_turtle.left(90)
    some_turtle.forward(100)
    some_turtle.right(135)
    some_turtle.forward(200)

    some_turtle.pu()
    some_turtle.setpos(200,0)
    some_turtle.pd()
    some_turtle.seth(90)

    some_turtle.forward(200)
    some_turtle.right(90)
    some_turtle.forward(50)

    for i in range(1,180):
        some_turtle.right(1)
        some_turtle.forward(1.75)

    some_turtle.seth(180)
    some_turtle.forward(50)

draw_figures()
