from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.setup(width=800, height=600)
user_bet = screen.textinput(
    title="MAKE YOUR BET", prompt="Which turtle will win the race ? We have blue, red, green, yellow, pink, black, orange, gray, purple.")
colors = ["blue", "red", "green", "yellow",
          "pink", "black", "orange", "gray", "purple"]
y_position = [-200, -150, -100, -50, 0, 50, 100, 150, 200]
is_race = False
all_turtles = []

for turtle_num in range(0, 8):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_num])
    new_turtle.penup()
    new_turtle.goto(x=-380, y=y_position[turtle_num])
    all_turtles.append(new_turtle)

if user_bet:
    is_race = True

while is_race:
    for turtle in all_turtles:
        if turtle.xcor() > 380:
            is_race = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                tim.write(f"The {winning_color} is the winner !!",
                          align="center", font=("Arial", 24, "bold"))
            else:
                tim.write(f"The {winning_color} is the winner !!",
                          align="center", font=("Arial", 24, "bold"))
        random_distance = random.randint(0, 20)
        turtle.forward(random_distance)


screen.exitonclick()
