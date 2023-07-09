from pyglet import shapes
from complex import get_coordinates_from_complex_value
from constants import HEIGHT, ORIGIN
from math import atan2, cos, sin, radians, degrees

WHITE = (255, 255, 255)


class LinkedLine:
    def __init__(self, complex_value, rate, prev_linked_line=None):
        self.complex_value = complex_value
        self.rate = rate
        self.next = None

        self.prev_rectangle = prev_linked_line

        if self.prev_rectangle:
            self.prev_rectangle.next = self

        x, y = get_coordinates_from_complex_value(self.complex_value)
        if self.prev_rectangle:
            prev_x, prev_y = get_coordinates_from_complex_value(
                self.prev_rectangle.complex_value)
        else:
            prev_x, prev_y = ORIGIN

        length = abs(self.complex_value)
        angle_radians = atan2(y, x)
        angle = degrees(angle_radians)

        self.rectangle = shapes.Rectangle(
            prev_x, HEIGHT - prev_y, int(length), 1, color=WHITE)
        self.rectangle.rotation = angle

    def draw(self):
        self.rectangle.draw()

    def update(self, dt):
        self.rectangle.rotation += self.rate * dt
        r = self.prev_rectangle.rectangle if self.prev_rectangle else None
        if r:
            self.rectangle.x = r.x + r.width * cos(radians(r.rotation))
            self.rectangle.y = r.y - r.width * sin(radians(r.rotation))
