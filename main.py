import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle's gonna win?: ")
color = ["red", "orange", "yellow", "green", "blue", "violet"]
y_positions = [-150, -100, -50, 0 , 50, 100]
all_turtles = []



for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    new_turtle.color(color[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The winning turtle in {winning_color}")
            else:
                print(f"You have lost! The winning turtle in {winning_color}")


        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)







screen.exitonclick()

