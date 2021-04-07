import pygame

from config import Config
from window_manager import WindowManager

# Init pygame
pygame.init()

# Get window size
display_info = pygame.display.Info()
window_size = int(Config.SCALE_OF_MAX * display_info.current_w), int(Config.SCALE_OF_MAX * display_info.current_h)

# Set up the drawing window
screen = pygame.display.set_mode(window_size, Config.WINDOW_TYPE)

# Set the window title
pygame.display.set_caption(Config.CAPTION)

# Set clock FPS
fps_clock = pygame.time.Clock()

# Get window manager
window_manager = WindowManager(window_size, screen)

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            running = False

    # Draw the image
    window_manager.draw()

    # Set FPS
    fps_clock.tick(Config.FPS)

# Done! Time to quit.
pygame.quit()
