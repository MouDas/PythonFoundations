import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.left(90)

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("yellow")

    brad = turtle.Turtle()
    brad.shape("classic")
    brad.color("purple")
    brad.speed(10)
    #draw a square
    count = 0
    while count<36:
        draw_square(brad)
        brad.left(10)
        count = count+1
        
 #   angie = turtle.Turtle()
 #  angie.shape("classic")
 #   angie.color("red")
 #   angie.circle(100)

 #   maxine = turtle.Turtle()
 #   maxine.shape()
 #   maxine.right(50)
 #   maxine.forward(100)
 #   maxine.right(140)
 #   maxine.forward(125)
 #   maxine.right(130)
 #   maxine.forward(90)
    
    
    
    
    window.exitonclick()
draw_shapes()
