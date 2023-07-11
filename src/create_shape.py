import ruspy as rp
from math import pi
import cmath


def complex_numbers_on_unit_circle(num_points):
    angle_step = 2 * cmath.pi / num_points
    complex_numbers = []

    for i in range(num_points):
        angle = i * angle_step
        complex_number = cmath.rect(1, angle)
        complex_numbers.append(complex_number)

    return rp.array(complex_numbers)


def complex_numbers_on_ellipse(num_points, a, b):
    angle_step = 2 * cmath.pi / num_points
    complex_numbers = []

    for i in range(num_points):
        angle = i * angle_step
        x = a * cmath.cos(angle)
        y = b * cmath.sin(angle)
        complex_number = x + y * 1j
        complex_numbers.append(complex_number)

    return rp.array(complex_numbers)


def complex_numbers_heart(num_points, size):
    t = rp.linspace(0, 2 * pi, num_points)
    x = size * (16 * rp.sin(t) ** 3) / 16
    y = size * (13 * rp.cos(t) - 5 * rp.cos(2 * t) -
                2 * rp.cos(3 * t) - rp.cos(4 * t)) / 16

    complex_numbers = [complex(x[i], y[i]) for i in range(num_points)]
    return rp.array(complex_numbers)


def complex_numbers_star(num_points, num_arms):
    t = rp.linspace(0, 2 * pi, num_points)
    # Varying radius creates the star effect
    r = (0.9 + 0.1 * rp.cos(num_arms * t))
    x = r * rp.cos(t)
    y = r * rp.sin(t)

    complex_numbers = [complex(x[i], y[i]) for i in range(num_points)]
    return rp.array(complex_numbers)


def complex_numbers_eighth_note():
    points = [
        (0, 6),  # Start of the stem
        (0, -1),  # Bottom of the stem
        (1, -2),  # Start of the oval
        (2, -2.5),  # Rightmost part of the oval
        (1, -3),  # End of the oval
        (0, -2),  # Bottom of the stem again
        (0, 1),  # A bit up the stem
        (1, 2),  # Start of the flag
        (0.5, 3),  # Tip of the flag
        (0, 2),  # Back to the stem
        (0, 6),  # Top of the stem
    ]
    complex_numbers = [complex(x, y) for x, y in points]
    return rp.array(complex_numbers) * 0.1


def image_to_complex_array(shape, num_points=10, scale=2.0):
    complex_array = complex_numbers_on_unit_circle
    if shape == 'heart':
        complex_array = complex_numbers_heart(num_points, 1)
    if shape == 'star':
        complex_array = complex_numbers_star(num_points, 5)
    if shape == 'ellipse':
        complex_array = complex_numbers_on_ellipse(num_points, 1, 0.5)
    if shape == 'eighth_note':
        complex_array = complex_numbers_eighth_note()
    return (complex_array + (0.5 - 0.5j)) * scale
