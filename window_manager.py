import pygame
from colors import Color


class WindowManager:
    def __init__(self):
        pass

    def draw(self, screen):
        # Fill the background with white
        screen.fill(Color.black)

        # Draw a solid blue circle in the center
        pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
