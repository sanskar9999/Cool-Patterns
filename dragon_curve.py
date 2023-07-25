import turtle

# Define the L-system rules
rules = {"X": "X+YF+", "Y": "-FX-Y"}

# Define the initial string
axiom = "FX"

# Define the number of iterations
n = 10

# Define the angle of rotation
angle = 90

# Define the drawing length
length = 5

# Apply the rules n times to generate the final string
string = axiom
for i in range(n):
  new_string = ""
  for char in string:
    new_string += rules.get(char, char) # Replace char by rules if possible, otherwise keep char
  string = new_string

# Create a turtle object
t = turtle.Turtle()
t.speed(0) # Set the speed to the fastest
t.hideturtle() # Hide the turtle

# Draw the string using turtle commands
for char in string:
  if char == "F": # Move forward by length units
    t.forward(length)
  elif char == "+": # Turn right by angle degrees
    t.right(angle)
  elif char == "-": # Turn left by angle degrees
    t.left(angle)

# Keep the window open until the user clicks on it
turtle.done()
