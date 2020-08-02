"""
------------------------------------------------------------------------
Author's name: Ibrahim Sel

The purpose of this game is to shoot down all 4 squares on the screen before they reach the shooter.
Use the arrow keys to move left and right and use the space key to shoot.
This is the first game I have ever made and hopefully, more will be coming soon.
------------------------------------------------------------------------
"""

import pygame

pygame.init()

# Define the x positions of objects
shooter_x = 360
square1_x = 50
square2_x = 250
square3_x = 450
square4_x = 650
projectile_x = 365

# Define the y positions of objects
shooter_y = 450
squares_y = 50
projectile_y = 745

# Define some colors
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Define the trackers for stats
shots_missed = 0
squares_shot = 0
projectiles_fired = 0

# Define velocities of objects
projectile_x_vel = 5
projectile_y_vel = 20
shooter_x_vel = 8
squares_y_vel = 1

# Define the size of objects
cursor_width = 5
cursor_height = 5
shooter_width = 10
square_width = 20
shooterHeight = 50
square_height = 20
projectile_radius = 5

# Define the window's size
window_x = 720
window_y = 500

# Main loop condition
go = True

# Create the game window
window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption("Blast Me")

# Set the timer up
clock = pygame.time.Clock()

while go:  # Main loop
    clock.tick(30)
    squares_y += squares_y_vel
    keys = pygame.key.get_pressed()
    window.fill(BLACK)

    for event in pygame.event.get():  # Shuts the program down if desired
        if event.type == pygame.QUIT:
            go = False

    if keys[pygame.K_q]:  # Allow user to quit the program by pressing q
        pygame.quit()
        quit(0)

    if keys[pygame.K_LEFT]:
        if shooter_x > 0:  # Keeps the shooter from getting out of screen
            shooter_x -= shooter_x_vel
            projectile_x -= projectile_x_vel

    if keys[pygame.K_RIGHT]:
        if window_x > shooter_x + shooter_width:  # Keeps the shooter from getting out of screen
            shooter_x += shooter_x_vel
            projectile_x += projectile_x_vel

    if keys[pygame.K_SPACE]:
        # Projectile
        shots_missed += 1  # Assume the shot has been missed
        projectiles_fired += 1
        projectile_x = shooter_x
        projectile_y = shooter_y
        pygame.draw.circle(window, RED, (projectile_x, projectile_y), projectile_radius, 2)
        
        while projectile_y + projectile_radius > 0:  #  Allow the movement of objects while shooting
            clock.tick(27)
            keys = pygame.key.get_pressed()
            window.fill(BLACK)

            for event in pygame.event.get():  # Makes it possible to quit the program
                if event.type == pygame.QUIT:
                    go = False
                    
            if keys[pygame.K_LEFT]:
                if shooter_x > 0:  # Keeps the shooter from getting out of screen
                    shooter_x -= shooter_x_vel

            if keys[pygame.K_RIGHT]:
                if window_x > shooter_x + shooter_width:  # Keeps the shooter from getting out of screen
                    shooter_x += shooter_x_vel

            # Check if squares have been shot
            if squares_y <= projectile_y <= squares_y + square_width and \
                    square1_x - projectile_radius < projectile_x < square1_x + square_width + projectile_radius:
                # Make the square that has been shot disappear
                squares_y_vel = 1000
                square1_x += squares_y_vel
                squares_y_vel = 1
                squares_shot += 1
                shots_missed -= 1
                break

            elif squares_y <= projectile_y <= squares_y + square_width and \
                    square2_x - projectile_radius < projectile_x < square2_x + square_width + projectile_radius:
                # Make the square that has been shot disappear
                squares_y_vel = 1000
                square2_x += squares_y_vel
                squares_y_vel = 1
                squares_shot += 1
                shots_missed -= 1
                break

            elif squares_y <= projectile_y <= squares_y + square_width and \
                    square3_x - projectile_radius < projectile_x < square3_x + square_width + projectile_radius:
                # Make the square that has been shot disappear
                squares_y_vel = 1000
                square3_x += squares_y_vel
                squares_y_vel = 1
                squares_shot += 1
                shots_missed -= 1
                break

            elif squares_y <= projectile_y <= squares_y + square_width and \
                    square4_x - projectile_radius < projectile_x < square4_x + square_width + projectile_radius:
                # Make the square that has been shot disappear
                squares_y_vel = 1000
                square4_x += squares_y_vel
                squares_y_vel = 1
                squares_shot += 1
                shots_missed -= 1
                break

            # Cursor
            pygame.draw.rect(window, YELLOW,
                             (shooter_x, squares_y + square_height, cursor_width, cursor_height))

            # Squares
            pygame.draw.rect(window, GREEN, (square1_x, squares_y, square_width, square_height))
            pygame.draw.rect(window, GREEN, (square2_x, squares_y, square_width, square_height))
            pygame.draw.rect(window, GREEN, (square3_x, squares_y, square_width, square_height))
            pygame.draw.rect(window, GREEN, (square4_x, squares_y, square_width, square_height))
            pygame.draw.rect(window, (0, 0, 255), (shooter_x, shooter_y, shooter_width, shooterHeight))

            # Projectile
            pygame.draw.circle(window, RED, (projectile_x, projectile_y), projectile_radius, 2)
            projectile_y -= projectile_y_vel
            pygame.display.update()

    if squares_y + square_width + projectile_radius == shooter_y:  # Controls the ending mechanism
        print("------------------------------\n           YOU LOSE         \n------------------------------")
        print("STATS:\n", "Shots: ", projectiles_fired, "\nHit: ", squares_shot, "\nMissed: ",
              shots_missed, sep="")
        pygame.time.delay(2000)
        pygame.quit()
        quit(0)

    if squares_shot == 4:  # Controls the ending mechanism
        print("------------------------------\n           YOU WIN         \n------------------------------")
        print("STATS:\n", "Shots: ", projectiles_fired, "\nHit: ", squares_shot, "\nMissed: ", shots_missed,
              sep="")
        pygame.quit()
        quit(0)

    # Cursor
    pygame.draw.rect(window, YELLOW, (shooter_x, squares_y + square_height, cursor_width, cursor_height))

    # Squares
    pygame.draw.rect(window, GREEN, (square1_x, squares_y, square_width, square_height))
    pygame.draw.rect(window, GREEN, (square2_x, squares_y, square_width, square_height))
    pygame.draw.rect(window, GREEN, (square3_x, squares_y, square_width, square_height))
    pygame.draw.rect(window, GREEN, (square4_x, squares_y, square_width, square_height))

    # Shooter
    pygame.draw.rect(window, BLUE, (shooter_x, shooter_y, shooter_width, shooterHeight))

    pygame.display.update()
