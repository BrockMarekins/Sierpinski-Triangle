from colors import Color
from config import Config


class Point:
    def __init__(self, x: int, y: int, radius: int = Config.RADIUS, color: Color = Color.blue):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
