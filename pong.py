# Controls:
#   Paddle A:
#       Up: W
#       Down: S
#   Paddle B: 
#       Up: ;
#       Down: .

# Change paddle controls on the following lines:

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

# By default the square shape is 20x20 pixels, using shapesize we can change this.
# By using stretch_wid=5 we multiply the height of the square by 5. This makes it 100 pixels tall by 20 pixels wide.
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

# By definition, Turtle objects draw a line as they are moving. We do not want this and .penup() is how we remove the lines made when moving
paddle_a.penup()

paddle_a.goto(-350, 0) # Positions paddle to right side of window

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Paddle Movement Functions
def paddle_a_up():
    y = paddle_a.ycor() # .ycor() returns the y-coordinate
    y += 20 # Makes the paddle move up 20 pixels
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard Binding
window.listen() # Listen for keyboard presses
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, ";")
window.onkeypress(paddle_b_down, ".")

# Main game loop
while True:
    window.update()
