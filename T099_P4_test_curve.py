"""
Name: William Dorval
Student Number: 101187466
Class: ECOR1042
Section: D
"""
from Cimpl import choose_file, load_image, copy, create_color, set_color, show, Image, save_as
from unit_testing import check_equal
import T099_P4_filter_curve as curve

def test_curve():
    original = Image(width=20, height=20)
    result = curve.draw_curve(original, "magenta", points=[(1, 1), (2, 2)])

    magenta = create_color(255, 0, 255)
    expected = Image(width=20, height=20)
    for x, y, (_, _, _) in expected:
        if abs(x-y) <= 2:
            expected.set_color(x, y, magenta)
    for x, y, color in result:
        pass
        check_equal(f"Testing pixel {x}, {y}", color, expected.get_color(x, y))

    # parabolic interpolation
    original = Image(width=50, height=50)
    result = curve.draw_curve(original, "lemon", points=[(0, 1), (10, 3), (20, 7)])

    lemon = create_color(255, 255, 0)
    expected = Image(width=50, height=50)
    for x, y, (_, _, _) in expected:
        if abs(int((0.01*(x**2) + (0.1*x) + 1)) - y) <= 2:
            expected.set_color(x, y, lemon)
    for x, y, color in result:
        pass
        check_equal(f"Testing pixel {x}, {y}", color, expected.get_color(x, y))

    original = Image(width=50, height=50)
    result = curve.draw_curve(original, "cyan", points=[(0, 1), (10, 3), (20, 7), (30, 13)])

    cyan = create_color(0, 255, 255)
    expected = Image(width=50, height=50)
    for x, y, (_, _, _) in expected:
        if abs(int((0.009999999999999992 * (x ** 2) + (0.10000000000000024 * x) + 1.0000000000000007)) - y) <= 2:
            expected.set_color(x, y, cyan)
    for x, y, color in result:
        check_equal(f"Testing pixel {x}, {y}", color, expected.get_color(x, y))


if __name__ == '__main__':
    test_curve()
