import random
import time
from typing import Tuple

import pygame

from colors import Color
from point import Point


class WindowManager:

    def __init__(self, window_size: Tuple[int, int]):
        self.width, self.height = window_size

        self.corners = []
        self.corners.append(Point(self.width // 2, 0, color=Color.red, radius=3))
        self.corners.append(Point(0, self.height, color=Color.red, radius=3))
        self.corners.append(Point(self.width, self.height, color=Color.red, radius=3))

        self.points = [self._random_point()]

        self.last = time.time()

    def _random_point(self):
        # Generate random point
        return Point(random.randint(0, self.width), random.randint(0, self.height))

    @staticmethod
    def _middle_point(corner: Point, point: Point):
        # Return point in the middle of these two files
        return Point((corner.x + point.x) // 2, (corner.y + point.y) // 2)

    def add_new_point(self):
        # Add new point to points
        last_point = self.points[-1]
        random_corner = random.choice(self.corners)
        middle_point = self._middle_point(random_corner, last_point)
        self.points.append(middle_point)

    def draw(self, screen: pygame.surface.Surface):
        old_screen = screen
        # Fill the background with white
        screen.fill(Color.black)

        # Draw a solid blue circle in the center
        for corner in self.corners:
            pygame.draw.circle(screen, corner.color, (corner.x, corner.y), corner.radius)

        # Draw points
        for point in self.points:
            pygame.draw.circle(screen, point.color, (point.x, point.y), point.radius)

        # Update the display
        pygame.display.update()

        # Generate new point
        self.add_new_point()
