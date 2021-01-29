"""
Name: William Dorval
Student Number: 101187466
Class: ECOR1042
Section: D
"""

from Cimpl import choose_file, load_image, copy, create_color, set_color, show, Image, get_color, create_image
from unit_testing import check_equal
from simple_Cimpl_filters import grayscale


def sepia(input_image: Image) -> Image:
    new_image = copy(grayscale(input_image))
    for x, y, (r, g, b) in new_image:
        if r < 63:
            set_color(new_image, x, y, create_color(1.1*r, g, 0.9*b))
        elif r <= 191:
            set_color(new_image, x, y, create_color(1.15*r, g, 0.85*b))
        else:
            set_color(new_image, x, y, create_color(1.08*r, g, 0.93*b))
    return new_image


def test_contrast():
    original = create_image(28, 1)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(60, 0, 0))
    set_color(original, 2, 0, create_color(0, 60, 0))
    set_color(original, 3, 0, create_color(0, 0, 60))
    set_color(original, 4, 0, create_color(60, 60, 0))
    set_color(original, 5, 0, create_color(60, 0, 60))
    set_color(original, 6, 0, create_color(0, 60, 60))
    set_color(original, 7, 0, create_color(60, 255, 255))
    set_color(original, 8, 0, create_color(255, 60, 255))
    set_color(original, 9, 0, create_color(255, 255, 60))
    set_color(original, 10, 0, create_color(60, 60, 255))
    set_color(original, 11, 0, create_color(60, 255, 60))
    set_color(original, 12, 0, create_color(255, 60, 60))
    set_color(original, 13, 0, create_color(60, 60, 60))
    set_color(original, 14, 0, create_color(160, 0, 0))
    set_color(original, 15, 0, create_color(0, 160, 0))
    set_color(original, 16, 0, create_color(0, 0, 160))
    set_color(original, 17, 0, create_color(160, 160, 0))
    set_color(original, 18, 0, create_color(160, 0, 160))
    set_color(original, 19, 0, create_color(0, 160, 160))
    set_color(original, 20, 0, create_color(160, 255, 255))
    set_color(original, 21, 0, create_color(255, 160, 255))
    set_color(original, 22, 0, create_color(255, 255, 160))
    set_color(original, 23, 0, create_color(160, 160, 255))
    set_color(original, 24, 0, create_color(160, 255, 160))
    set_color(original, 25, 0, create_color(255, 160, 160))
    set_color(original, 26, 0, create_color(160, 160, 160))
    set_color(original, 27, 0, create_color(255, 255, 255))

    contrasted = None  # to be replaced with contrast filter call

    expected = create_image(28, 1)
    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 1, 0, create_color(0, 0, 0))
    set_color(expected, 2, 0, create_color(0, 0, 0))
    set_color(expected, 3, 0, create_color(0, 0, 0))
    set_color(expected, 4, 0, create_color(0, 0, 0))
    set_color(expected, 5, 0, create_color(0, 0, 0))
    set_color(expected, 6, 0, create_color(0, 0, 0))
    set_color(expected, 7, 0, create_color(0, 255, 255))
    set_color(expected, 8, 0, create_color(255, 0, 255))
    set_color(expected, 9, 0, create_color(255, 255, 0))
    set_color(expected, 10, 0, create_color(0, 0, 255))
    set_color(expected, 11, 0, create_color(0, 255, 0))
    set_color(expected, 12, 0, create_color(255, 0, 0))
    set_color(expected, 13, 0, create_color(0, 0, 0))
    set_color(expected, 14, 0, create_color(255, 0, 0))
    set_color(expected, 15, 0, create_color(0, 255, 0))
    set_color(expected, 16, 0, create_color(0, 0, 255))
    set_color(expected, 17, 0, create_color(255, 255, 0))
    set_color(expected, 18, 0, create_color(255, 0, 255))
    set_color(expected, 19, 0, create_color(0, 255, 255))
    set_color(expected, 20, 0, create_color(255, 255, 255))
    set_color(expected, 21, 0, create_color(255, 255, 255))
    set_color(expected, 22, 0, create_color(255, 255, 255))
    set_color(expected, 23, 0, create_color(255, 255, 255))
    set_color(expected, 24, 0, create_color(255, 255, 255))
    set_color(expected, 25, 0, create_color(255, 255, 255))
    set_color(expected, 26, 0, create_color(255, 255, 255))
    set_color(expected, 27, 0, create_color(255, 255, 255))


if __name__ == '__main__':

    show(sepia(load_image(choose_file())))



"""
my idea of test for sepia
    original = create_image(5, 1)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(40, 40, 40))
    set_color(original, 2, 0, create_color(100, 100, 100))
    set_color(original, 3, 0, create_color(200, 200, 200))
    set_color(original, 4, 0, create_color(255, 255, 255))
    # proceeding under the assumption that the imported grayscale function works as intended
    # the test will only pass grayscale values to the filter in order to reduce potential sources of error when
    # determining expected results

    sepia_image = sepia(original)

    expected = create_image(5, 1)
    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 1, 0, create_color(44, 40, 36))
    set_color(expected, 2, 0, create_color(115, 100, 185))
    set_color(expected, 3, 0, create_color(216, 200, 186))
    set_color(expected, 4, 0, create_color(255, 255, 237))

    for x, y, col in sepia_image:
        check_equal(f"checking pixel {x}, {y} ", col, get_color(expected, x, y))
"""