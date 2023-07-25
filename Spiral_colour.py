from PIL import Image, ImageDraw
import math

# Define the image size and mode
IMAGE_SIZE = (800, 800)
IMAGE_MODE = "RGB"

# Define the number of iterations and angle increment
ITERATIONS = 1000
ANGLE_INCREMENT = 0.01

# Define the initial radius and radius increment
RADIUS = 10
RADIUS_INCREMENT = 0.5

# Define the initial color and color increment
COLOR = (255, 0, 0)
COLOR_INCREMENT = (0, 1, -1)

# Create a new image and a draw object
image = Image.new(IMAGE_MODE, IMAGE_SIZE)
draw = ImageDraw.Draw(image)

# Loop through each iteration
for i in range(ITERATIONS):
  # Calculate the coordinates of the end point of the line using polar coordinates
  angle = i * ANGLE_INCREMENT # The angle is proportional to the iteration number
  x = IMAGE_SIZE[0] / 2 + RADIUS * math.cos(angle) # The x coordinate is the center plus the radius times the cosine of the angle
  y = IMAGE_SIZE[1] / 2 + RADIUS * math.sin(angle) # The y coordinate is the center plus the radius times the sine of the angle
  
  # Draw a line from the center to the end point with the current color
  draw.line([(IMAGE_SIZE[0] / 2, IMAGE_SIZE[1] / 2), (x, y)], fill=COLOR)
  
  # Increment the radius and color by their respective increments
  RADIUS += RADIUS_INCREMENT
  COLOR = tuple((c + COLOR_INCREMENT[i % len(COLOR_INCREMENT)]) % 256 for i, c in enumerate(COLOR)) # Use modulo arithmetic to cycle through the RGB values

# Save and show the image
image.save("spiral.png")
image.show()
