import numpy as np
import cmath


def complex_numbers_on_unit_circle(num_points):
    angle_step = 2 * cmath.pi / num_points
    complex_numbers = []

    for i in range(num_points):
        angle = i * angle_step
        complex_number = cmath.rect(1, angle)
        complex_numbers.append(complex_number)

    return np.array(complex_numbers)


def complex_numbers_on_ellipse(num_points, a, b):
    angle_step = 2 * cmath.pi / num_points
    complex_numbers = []

    for i in range(num_points):
        angle = i * angle_step
        x = a * cmath.cos(angle)
        y = b * cmath.sin(angle)
        complex_number = x + y * 1j
        complex_numbers.append(complex_number)

    return np.array(complex_numbers)


def complex_numbers_heart(num_points, size):
    t = np.linspace(0, 2 * np.pi, num_points)
    x = size * (16 * np.sin(t) ** 3) / 16
    y = size * (13 * np.cos(t) - 5 * np.cos(2 * t) -
                2 * np.cos(3 * t) - np.cos(4 * t)) / 16

    complex_numbers = [complex(x[i], y[i]) for i in range(num_points)]
    return np.array(complex_numbers)


def complex_numbers_star(num_points, num_arms):
    t = np.linspace(0, 2 * np.pi, num_points)
    # Varying radius creates the star effect
    r = (0.9 + 0.1 * np.cos(num_arms * t))
    x = r * np.cos(t)
    y = r * np.sin(t)

    complex_numbers = [complex(x[i], y[i]) for i in range(num_points)]
    return np.array(complex_numbers)


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
    return np.array(complex_numbers) * 0.1


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
