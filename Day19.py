#Higher order functions and Event Listeners

#Moving the turtle when we press spacebar.
# from turtle import Turtle,Screen
# tim=Turtle()
# screen=Screen()
# def move_forward():
#     tim.forward(10)
# screen.listen()
# screen.onkey(key="space",fun=move_forward)
# screen.exitonclick()


#Sketching a diagram using a,w,f,d,...
# from turtle import Turtle,Screen
# tim=Turtle()
# screen=Screen()
# def move_forward():
#     tim.forward(10)
# def move_backward():
#     tim.backward(10)
# def turn_left():
#     tim.left(10)
# def turn_right():
#     tim.right(10)
# def clear_screen():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()   
# screen.listen()
# screen.onkey(move_forward,"w")
# screen.onkey(move_backward,"s")
# screen.onkey(turn_right,"d")
# screen.onkey(turn_right,"a")
# screen.onkey(clear_screen,"c")
# screen.exitonclick()


#Turtle Racing Game[using objects and instances]
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        #230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)   #Make each turtle move a random amount.
        turtle.forward(rand_distance)

screen.exitonclick()