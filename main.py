from turtle import Turtle, Screen
import random
from tkinter import messagebox


screen = Screen()

race_start = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour:")
turtle_colours = ["red", "green", "blue", "pink", "purple", "orange", "yellow"]
turtles = []

y_value = -120
for turtle_index in range(0, 7):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(f"{turtle_colours[turtle_index]}")
    turtle.goto(x=-230, y=y_value)
    y_value += 40
    turtles.append(turtle)

if user_bet:
    race_start = True

while race_start:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race_start = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You won! The {winning_colour} turtle was the winner!")
                messagebox.showinfo("Congratulations!", f"The {winning_colour} turtle won!")
            else:
                print(f"Sorry, you lost. The {winning_colour} turtle was the winner.")
                messagebox.showinfo("Sorry, you lost!", f"The {winning_colour} turtle won.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
# def move_forwards():
#     turtle.forward(10)
# def move_backwards():
#     turtle.backward(10)
# def turn_left():
#     turtle.left(10)
# def turn_right():
#     turtle.right(10)
# def clear():
#     turtle.clear()
#     turtle.penup()
#     turtle.home()
#     turtle.pendown()

screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="d", fun=turn_right)
# screen.onkey(key="c", fun=clear)







screen.exitonclick()