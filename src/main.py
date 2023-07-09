import pyglet
from pyglet import shapes
from complex import get_coordinates_from_complex_value
from constants import ORIGIN, WIDTH, HEIGHT, YELLOW, RED, ROTATION_SPEED, MAX_TRACE_LENGTH, SHAPES
from math import cos, log, sin, radians, pi
from create_shape import image_to_complex_array
from line import LinkedLine
import numpy as np


def create_trace(last_line):
    r = last_line.rectangle
    x = r.x + r.width * cos(radians(r.rotation))
    y = r.y - r.width * sin(radians(r.rotation))
    return shapes.Circle(x, y, 2, color=YELLOW)


def draw_original_shape(original_shape):
    color = list(RED)
    for value in original_shape:
        ox, oy = ORIGIN
        x, y = get_coordinates_from_complex_value(value)
        shapes.Circle(x + ox, HEIGHT - (y + oy), 2, color=tuple(color)).draw()
        color[2] = min(5 + color[2], 255)


def create_linked_lines(initial_vector):
    N = len(initial_vector)
    lines = []
    prev_line = None
    values_and_rates = []
    for fourier_coefficient in range(-N//2, N//2):
        rate = ROTATION_SPEED * 2 * pi * fourier_coefficient / N
        complex_value = initial_vector[fourier_coefficient + N//2]
        values_and_rates.append((complex_value, rate))

    values_and_rates.sort(key=lambda x: abs(x[1]), reverse=False)

    for (value, rate) in values_and_rates:
        line = LinkedLine(value, rate, prev_line)
        lines.append(line)
        prev_line = line

    return lines


def make_draw(window, lines, traces, original_shape):
    @window.event
    def on_draw():
        window.clear()
        for line in lines:
            line.draw()
        for trace in traces:
            trace.draw()
        draw_original_shape(original_shape)
    return on_draw


def make_update(lines, traces):
    def update(dt):
        for line in lines:
            line.update(dt)
        traces.append(create_trace(lines[-1]))
        if len(traces) > MAX_TRACE_LENGTH:
            traces.pop(0)
        for i, trace in enumerate(traces):
            rate = MAX_TRACE_LENGTH
            fade_factor = log(rate - min(rate - 1, len(traces) - i))
            fade_factor = max(0, fade_factor) / log(rate)
            trace.color = (int(255 * fade_factor), int(255 * fade_factor), 0)
    return update


def initialize():
    shape = SHAPES[2] # heart
    original_shape = image_to_complex_array(shape, num_points=100, scale=300)
    initial_vector = np.fft.fftshift(
        np.fft.fft(original_shape) / len(original_shape))
    lines = create_linked_lines(initial_vector)
    traces = []

    window = pyglet.window.Window(WIDTH, HEIGHT)
    return window, lines, traces, original_shape


def main():
    window, lines, traces, original_shape = initialize()
    make_draw(window, lines, traces, original_shape)
    pyglet.clock.schedule(make_update(lines, traces))
    pyglet.app.run()


if __name__ == '__main__':
    main()
