#Turtle Graphics

# from turtle import Turtle,Screen
# tim = Turtle()

# tim.shape("turtle")
# tim.color("red")
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# screen = Screen()
# screen.exitonclick()


#Basic import
# import turtle
# tim = turtle.Turtle()

# #Using from
# from turtle import Turtle
# tim=Turtle()

#Aliasing the name of the module
# import turtle as t
# tim=t.Turtle()

#Drawing a dashed line
# import turtle as t 
# tim=t.Turtle()
# for _ in range(0,10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# t.exitonclick()

#Drawing the sides from 3 sided triangle to 10 sided decathon by using different colours
# import turtle as t
# import random
# tim=t.Turtle()
# colors=["red","green","yellow","orange","blue","purple"]
# def draw_shape(num_sides):
#     angle=360/num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
        
# for shape_side_n in range(3,11):       #From triangle to Decathon so 3 to 10 sides
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)


#Drawing a random walk
# import turtle as t
# import random
# tim=t.Turtle()
# colors=["red","green","yellow","orange","blue","purple"]
# directions=[0,90,180,270]
# tim.pensize(15)             #size of that turtle pointer
# tim.speed("fastest")        #speed of the movement 

# for _ in range(200):
#     tim.color(random.choice(colors))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


#Generating a random RGB colours
# import turtle as t
# import random
# tim=t.Turtle()
# t.colormode(255)
# def random_color():
#     r=random.randint(0,255)
#     g=random.randint(0,255)
#     b=random.randint(0,255)
#     random_color=(r,g,b)
#     return(random_color)
    
# directions=[0,90,180,270]
# tim.pensize(15)            

# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
    
    
#Making a spirograph
import turtle as t
import random
tim=t.Turtle()
t.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return(random_color)
tim.speed("fastest")
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
draw_spirograph(5)
    
screen=t.Screen()
screen.exitonclick()