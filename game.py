import pygame

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode((600, 600), pygame.SCALED | pygame.RESIZABLE)
pygame.display.set_caption("Test")

# define colors
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
FPS = 60

# set clock FPS
clock = pygame.time.Clock()

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            done = True

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip the display
    pygame.display.flip()

    # set FPS
    clock.tick(FPS)

# Done! Time to quit.
pygame.quit()
