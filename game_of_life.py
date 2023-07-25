import pygame
import random

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define the size of each cell
CELL_SIZE = 10

# Define the number of rows and columns
ROWS = 60
COLS = 80

# Define the probability of a cell being alive at the start
PROB_ALIVE = 0.2

# Define the window size and title
WINDOW_SIZE = (CELL_SIZE * COLS, CELL_SIZE * ROWS)
WINDOW_TITLE = "Conway's Game of Life"

# Initialize pygame and create a window
pygame.init()
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(WINDOW_TITLE)

# Create a 2D array to store the current state of each cell (0 = dead, 1 = alive)
grid = []
for i in range(ROWS):
  row = []
  for j in range(COLS):
    if random.random() < PROB_ALIVE: # Randomly assign a state to each cell with a given probability
      row.append(1)
    else:
      row.append(0)
  grid.append(row)

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Create a boolean variable to control the main loop
running = True

# Main loop
while running:
  # Handle events
  for event in pygame.event.get():
    if event.type == pygame.QUIT: # User clicks the close button
      running = False # Stop the loop
  
  # Update the state of each cell according to the rules of the Game of Life
  # Rules:
  # - Any live cell with fewer than two live neighbors dies, as if by underpopulation.
  # - Any live cell with two or three live neighbors lives on to the next generation.
  # - Any live cell with more than three live neighbors dies, as if by overpopulation.
  # - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
  
  # Create a copy of the grid to store the new state of each cell
  new_grid = []
  for i in range(ROWS):
    new_row = []
    for j in range(COLS):
      new_row.append(grid[i][j])
    new_grid.append(new_row)
  
  # Loop through each cell and count its live neighbors
  for i in range(ROWS):
    for j in range(COLS):
      live_neighbors = 0
      # Check the eight neighboring cells using a nested loop and modulo arithmetic
      for x in range(-1, 2):
        for y in range(-1, 2):
          if x == 0 and y == 0: # Skip the cell itself
            continue
          # Use modulo to create a toroidal grid (wrap around the edges)
          row = (i + x + ROWS) % ROWS
          col = (j + y + COLS) % COLS
          # Increment the live neighbor count if the cell is alive
          if grid[row][col] == 1:
            live_neighbors += 1
      
      # Apply the rules to update the state of the cell
      if grid[i][j] == 1: # The cell is alive
        if live_neighbors < 2 or live_neighbors > 3: # The cell dies
          new_grid[i][j] = 0
      else: # The cell is dead
        if live_neighbors == 3: # The cell becomes alive
          new_grid[i][j] = 1
  
  # Replace the grid with the new grid
  grid = new_grid

  # Draw the grid on the window
  window.fill(BLACK) # Fill the window with black
  for i in range(ROWS):
    for j in range(COLS):
      if grid[i][j] == 1: # The cell is alive
        # Calculate the coordinates of the top left corner of the cell
        x = j * CELL_SIZE
        y = i * CELL_SIZE
        # Draw a white rectangle to represent the cell
        pygame.draw.rect(window, WHITE, (x, y, CELL_SIZE, CELL_SIZE))
  
  # Update the display
  pygame.display.flip()

  # Set the frame rate to 10 frames per second
  clock.tick(10)

# Quit pygame and exit the program
pygame.quit()
