"""
Name: William Dorval
Student Number: 101187466
Class: ECOR1042
Section: D
"""

from Cimpl import choose_file, load_image, copy, create_color, set_color, show, Image
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

    show(sepia(load_image(choose_file())))
    """
    I have created a grayscale filter that more accurately determines lightness based on human perception
    if you could tell me in the feedback for this if I can use that in the sepia filter for the next milestone that
    would be much appreciated
    show(accurate_grayscale(load_image(choose_file())))
    """
