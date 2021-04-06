import pygame

from config import Config

# Init pygame
from window_manager import WindowManager

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode(Config.WINDOW_SIZE, Config.WINDOW_TYPE)

# Set the window title
pygame.display.set_caption(Config.CAPTION)

# set clock FPS
clock = pygame.time.Clock()

# get window manager
window_manager = WindowManager()

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            done = True

    # Draw the image
    window_manager.draw(screen)

    # Flip the display
    pygame.display.flip()

    # set FPS
    clock.tick(Config.FPS)

# Done! Time to quit.
pygame.quit()
