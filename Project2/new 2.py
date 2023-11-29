import turtle  # Corrected import statement
from time import sleep

# Create a screen
scorpio = turtle.Screen()
scorpio.setup(width=400, height=300)
scorpio.bgcolor("beige")
scorpio.tracer(0)  # Disable automatic screen updates

# Define a custom color
turtle.colormode(255)
champagne_color = (230, 206, 172)  # RGB values for champagne color

# Create a Turtle object
splash_turtle = turtle.Turtle()
splash_turtle.penup()
splash_turtle.speed(1)

# Create a champagne-colored rectangle
splash_turtle.color(champagne_color)  # Use the defined RGB color
splash_turtle.goto(-180, 100)
splash_turtle.begin_fill()  # Corrected method name
for _ in range(2):  # Added missing iteration variable _
    splash_turtle.forward(360)
    splash_turtle.right(90)
    splash_turtle.forward(120)
    splash_turtle.right(90)
splash_turtle.end_fill()

# Register and create a profile photo turtle
scorpio.addshape("profile", "profile.JPG")  # Corrected method name and added before turtle creation
profile_turtle = turtle.Turtle("profile")
profile_turtle.penup()
profile_turtle.goto(0, 45)

# Your name
splash_turtle.goto(0, 20)
splash_turtle.color("black")
splash_turtle.write("Jennifer Romain", align="center", font=("Times New Roman", 12, "bold"))

# Loading bar outline
splash_turtle.goto(-150, -10)
splash_turtle.color(champagne_color)
splash_turtle.pendown()
splash_turtle.begin_fill()
for _ in range(2):  # Added missing iteration variable _
    splash_turtle.forward(300)
    splash_turtle.right(90)
    splash_turtle.forward(20)
    splash_turtle.right(90)
splash_turtle.end_fill()
splash_turtle.penup()

loading_speed = 5  # Adjust the speed as needed
for i in range(0, 301, loading_speed):
    splash_turtle.goto(-150, -10)
    splash_turtle.pendown()
    splash_turtle.color("green")
    splash_turtle.begin_fill()
    for _ in range(2):  # Added missing iteration variable _
        splash_turtle.forward(min(i, 300))  # Ensure that the loading bar does not exceed its bounds
        splash_turtle.right(90)
        splash_turtle.forward(20)
        splash_turtle.right(90)
    splash_turtle.end_fill()
    splash_turtle.penup()
    splash_turtle.goto(0, -40)
    splash_turtle.color("black")
    percentage_complete = min(i, 300) // 3  # Cap the percentage at 100
    splash_turtle.write(f"Loading: {percentage_complete}% Complete", align="center", font=("Times New Roman", 10, "normal"))
    scorpio.update()  # Update the screen with the current drawing
    sleep(0.1)

# Hide the Turtle and display the splash screen
splash_turtle.hideturtle()
scorpio.update()  # Final screen update
turtle.done()
