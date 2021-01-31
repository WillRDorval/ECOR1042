"""
Name: William Dorval
Student Number: 101187466
Class: ECOR1042
Section: D
"""

from Cimpl import choose_file, load_image, copy, create_color, set_color, show, Image, get_color, create_image
from unit_testing import check_equal
from simple_Cimpl_filters import grayscale


def accurate_grayscale(input_image: Image) -> Image:
    result = copy(input_image)
    for x, y, (r, g, b) in result:
        gray = 0.299*r + 0.587*g + 0.114*b
        set_color(result, x, y, create_color(gray, gray, gray))
    return result


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


if __name__ == '__main__':
    
    show(accurate_grayscale(load_image(choose_file())))
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