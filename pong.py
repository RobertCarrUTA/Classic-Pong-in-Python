# The turtle module lets us do some basic graphics, and
# unlike pygame, turtle comes built in

import turtle

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width = 800, height = 600)
# .tracer stops the window from auto updating, this makes us manually update it.
# By manually updating it, it allows us to speed up the game
window.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # sets the speed of the animation to the maximum possible speed, if not done, it would be really slow
paddle_a.shape("square")
paddle_a.color("white")

# By definition, Turtle objects draw a line as they are moving. We do not want this and .penup() is how we remove the lines made when moving
paddle_a.penup()

paddle_a.goto(-350, 0) # Positions paddle to right side of window

# Paddle B

# Ball

# Main game loop
while True:
    window.update()
