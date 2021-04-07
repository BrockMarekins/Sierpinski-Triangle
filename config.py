import pygame

from colors import Color


class Config:
    WINDOW_TYPE = pygame.SCALED | pygame.RESIZABLE
    CAPTION = "Sierpinski Triangle"
    FPS = 1000
    CORNER_POINT_RADIUS = 3
    CORNER_POINT_COLOR = Color.blue
    RANDOM_POINT_RADIUS = 1
    RANDOM_POINT_COLOR = Color.red
    BACKGROUND_COLOR = Color.black
    SCALE_OF_MAX = 0.7
    SOLID_CORNERS = True
