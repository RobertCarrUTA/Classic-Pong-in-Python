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

# Main game loop
while True:
    window.update()
