import random
from typing import Tuple

import pygame

from config import Config
from point import Point


class WindowManager:

    def __init__(self, window_size: Tuple[int, int], screen: pygame.surface.Surface):
        self.width, self.height = window_size

        self.corners = []
        if Config.SOLID_CORNERS:
            self.corners.append(
                Point(self.width // 2, 0, color=Config.CORNER_POINT_COLOR, radius=Config.CORNER_POINT_RADIUS))
            self.corners.append(
                Point(0, self.height, color=Config.CORNER_POINT_COLOR, radius=Config.CORNER_POINT_RADIUS))
            self.corners.append(
                Point(self.width, self.height, color=Config.CORNER_POINT_COLOR, radius=Config.CORNER_POINT_RADIUS))
        else:
            for i in range(3):
                point = self._random_point()
                point.color = Config.CORNER_POINT_COLOR
                point.radius = Config.CORNER_POINT_RADIUS
                self.corners.append(point)

        self.screen = screen

        self.current_point = None
        self._init_draw()

    def _draw_current_point(self):
        pygame.draw.circle(self.screen, self.current_point.color, (self.current_point.x, self.current_point.y),
                           self.current_point.radius)

    def _init_draw(self):
        # Fill the background with black
        self.screen.fill(Config.BACKGROUND_COLOR)

        # Draw a solid blue circle in the center
        for corner in self.corners:
            pygame.draw.circle(self.screen, corner.color, (corner.x, corner.y), corner.radius)

        # Draw current point
        self.current_point = self._random_point()
        self._draw_current_point()

    def _random_point(self):
        # Generate random point
        return Point(random.randint(0, self.width), random.randint(0, self.height), color=Config.RANDOM_POINT_COLOR,
                     radius=Config.RANDOM_POINT_RADIUS)

    @staticmethod
    def _middle_point(point_1: Point, point_2: Point):
        # Return point in the middle of these two files
        return Point((point_1.x + point_2.x) // 2, (point_1.y + point_2.y) // 2, color=Config.RANDOM_POINT_COLOR,
                     radius=Config.RANDOM_POINT_RADIUS)

    def new_point(self):
        # Add new point to points
        random_corner = random.choice(self.corners)
        middle_point = self._middle_point(random_corner, self.current_point)
        self.current_point = middle_point

    def draw(self):
        # Update the display
        pygame.display.update()

        # Generate new point
        self.new_point()

        # Draw new point
        self._draw_current_point()
