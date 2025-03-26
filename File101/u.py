import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Window settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Minecraft")

# Colors
GRASS_COLOR = (0, 255, 0)
STONE_COLOR = (128, 128, 128)
WATER_COLOR = (0, 0, 255)
TREE_COLOR = (0, 128, 0)
SAND_COLOR = (240, 240, 64)  # Added sand color
SKY_COLOR = (135, 206, 235)
PLAYER_COLOR = (255, 0, 0)
SNOW_COLOR = (255, 250, 250)

# Block size and player size
BLOCK_SIZE = 30
PLAYER_SIZE = 20
PLAYER_SPEED = 5

# World generation
def generate_world(width, height):
    """
    Generates a simple Minecraft-like world.  Adds trees, lakes, and variation.
    """
    world = [[GRASS_COLOR for _ in range(width)] for _ in range(height)]

    # Add a layer of stone underground
    for y in range(height // 2, height):
        for x in range(width):
            world[y][x] = STONE_COLOR

    # Create water areas (lakes)
    for _ in range(3):  #number of lakes
        lake_x = random.randint(0, width - 6)
        lake_y = random.randint(0, height // 2 - 6)
        for x in range(lake_x, lake_x + 6):
            for y in range(lake_y, lake_y + 6):
                world[y][x] = WATER_COLOR
                #create sand edges
                if random.random() > 0.5:
                    if x > lake_x and world[y][x-1] == GRASS_COLOR:
                         world[y][x-1] = SAND_COLOR
                    if x < lake_x + 5 and world[y][x+1] == GRASS_COLOR:
                         world[y][x+1] = SAND_COLOR
                    if y > lake_y and world[y-1][x] == GRASS_COLOR:
                         world[y-1][x] = SAND_COLOR
                    if y < lake_y + 5 and world[y+1][x] == GRASS_COLOR:
                         world[y+1][x] = SAND_COLOR

    # Create trees
    for _ in range(20): #number of trees
        tree_x = random.randint(0, width - 1)
        tree_y = random.randint(0, height // 2 - 1)
        if world[tree_y][tree_x] == GRASS_COLOR:
            world[tree_y][tree_x] = TREE_COLOR
            if tree_y > 0:
                world[tree_y - 1][tree_x] = TREE_COLOR  # Add a bit of trunk

    # Add random elevation to grass
    for x in range(width):
        for y in range(height // 2):
            if world[y][x] == GRASS_COLOR:
                if random.random() < 0.2:  # Probability of elevation change
                    world[y][x] = (0, 200 + random.randint(-50, 50), 0)  # Darker/lighter grass

    # Add snow to the top of the world
    for x in range(width):
        for y in range(height // 4):
            if world[y][x] == GRASS_COLOR or world[y][x] == TREE_COLOR:
                if random.random() < 0.1:
                    world[y][x] = SNOW_COLOR
    return world

# Game variables
WORLD_WIDTH = WIDTH // BLOCK_SIZE
WORLD_HEIGHT = HEIGHT // BLOCK_SIZE
world = generate_world(WORLD_WIDTH, WORLD_HEIGHT)
player_x = WIDTH // 2 - PLAYER_SIZE // 2
player_y = HEIGHT // 2 - PLAYER_SIZE // 2

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player_x < WIDTH - PLAYER_SIZE:
        player_x += PLAYER_SPEED
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= PLAYER_SPEED
    if keys[pygame.K_DOWN] and player_y < HEIGHT - PLAYER_SIZE:
        player_y += PLAYER_SPEED

    # Draw the world
    for y in range(WORLD_HEIGHT):
        for x in range(WORLD_WIDTH):
            pygame.draw.rect(screen, world[y][x], (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    # Draw the player
    pygame.draw.rect(screen, PLAYER_COLOR, (player_x, player_y, PLAYER_SIZE, PLAYER_SIZE))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
