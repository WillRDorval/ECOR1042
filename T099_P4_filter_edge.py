"""
Name: William Dorval
Student Number: 101187466
Class: ECOR1042
Section: D
"""

from Cimpl import choose_file, load_image, copy, create_color, set_color, show, Image, save_as
import math


def grayscale(input_image: Image) -> Image:
    result = copy(input_image)
    for x, y, (r, g, b) in input_image:
        gray = (r+g+b)/3
        result.set_color(x, y, create_color(gray, gray, gray))

    return result


def detect_edges(input_image: Image, threshold: int) -> Image:
    brightness = grayscale(input_image)
    result = Image(width=input_image.get_width(), height=input_image.get_height())
    for x, y, (r, _, _) in brightness:
        if abs(r - brightness.get_color(x, y-1)[0]) > threshold:
            result.set_color(x, y, create_color(0, 0, 0))

    return result


def real_detect_edges(input_image: Image, tolerance: int) -> Image:
    if 100 < tolerance < 0:
        raise ValueError("tolerance must be a percentage form 0 to 100")

    result = Image(width=input_image.get_width(), height=input_image.get_height())
    gap = tolerance / 100
    for x in range(input_image.get_width()):
        for y in range(input_image.get_height()):
            try:
                r_diff = abs((orig := input_image.get_color(x, y)[0]**2) - (new := input_image.get_color(x, y - 1)[0]**2))
                if new == 0 == orig:
                    pass
                elif new > orig:
                    r_diff = r_diff/new
                else:
                    r_diff = r_diff/orig
                g_diff = abs((orig := input_image.get_color(x, y)[1]**2) - (new := input_image.get_color(x, y - 1)[1]**2))
                if new == 0 == orig:
                    pass
                elif new > orig:
                    g_diff = g_diff/new
                else:
                    g_diff = g_diff/orig
                b_diff = abs((orig := input_image.get_color(x, y)[2]**2) - (new := input_image.get_color(x, y - 1)[2]**2))
                if new == 0 == orig:
                    pass
                elif new > orig:
                    b_diff = b_diff/new
                else:
                    b_diff = b_diff/orig

                r_side = abs((orig := input_image.get_color(x, y)[0]**2) - (new := input_image.get_color(x-1, y)[0]**2))
                if new == 0 == orig:
                    pass
                elif new > orig:
                    r_side = r_side/new
                else:
                    r_side = r_side/orig

                g_side = abs((orig := input_image.get_color(x, y)[1]**2) - (new := input_image.get_color(x-1, y)[1]**2))
                if new == 0 == orig:
                    pass
                elif new > orig:
                    g_side = g_side/new
                else:
                    g_side = g_side/orig

                b_side = abs((orig := input_image.get_color(x, y)[2]**2) - (new := input_image.get_color(x-1, y)[2]**2))
                if new == 0 == orig:
                    pass
                elif new > orig:
                    b_side = b_side/new
                else:
                    b_side = b_side/orig

                if r_side > r_diff:
                    r_diff = r_side
                if g_side > g_diff:
                    g_diff = g_side
                if b_side > b_diff:
                    b_diff = b_side

            except IndexError:
                pass

            else:
                diff = (0.299 * r_diff + 0.587 * g_diff + 0.114 * b_diff)
                val = 255 - round(255 * (math.sqrt(diff)/(1 + pow(math.e, -8*(diff-gap)))))
                result.set_color(x, y, create_color(val, val, val))
    return result


if __name__ == "__main__":
    image = detect_edges(load_image(choose_file()), 10)
    show(image)
    save_as(image)
