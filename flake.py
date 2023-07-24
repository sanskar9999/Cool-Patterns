import turtle

# Define a function to draw a Koch curve of a given length and order
def koch_curve(t, length, order):
  if order == 0: # Base case: draw a straight line
    t.forward(length)
  else: # Recursive case: draw four smaller Koch curves
    koch_curve(t, length/3, order-1) # Draw the first segment
    t.left(60) # Turn left by 60 degrees
    koch_curve(t, length/3, order-1) # Draw the second segment
    t.right(120) # Turn right by 120 degrees
    koch_curve(t, length/3, order-1) # Draw the third segment
    t.left(60) # Turn left by 60 degrees
    koch_curve(t, length/3, order-1) # Draw the fourth segment

# Define a function to draw a Koch snowflake of a given side length and order
def koch_snowflake(t, side, order):
  for i in range(3): # Repeat three times
    koch_curve(t, side, order) # Draw a Koch curve
    t.right(120) # Turn right by 120 degrees

# Create a turtle object
t = turtle.Turtle()
t.speed(0) # Set the speed to the fastest
t.penup() # Lift the pen up
t.goto(-100, 100) # Move the turtle to the upper left corner
t.pendown() # Put the pen down

# Draw a Koch snowflake of side length 200 and order 4
koch_snowflake(t, 200, 4)

# Hide the turtle
t.hideturtle()

# Keep the window open until the user clicks on it
turtle.done()
