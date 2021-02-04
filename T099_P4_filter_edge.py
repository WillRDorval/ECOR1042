"""
Name: William Dorval
Student Number: 101187466
Class: ECOR1042
Section: D
"""

from Cimpl import choose_file, load_image, copy, create_color, set_color, show, Image, save_as
import math


def accurate_grayscale(input_image: Image) -> Image:
    result = copy(input_image)
    for x, y, (r, g, b) in result:
        gray = round(0.299 * r + 0.587 * g + 0.114 * b)
        set_color(result, x, y, create_color(gray, gray, gray))
    return result


def detect_edges(input_image: Image, tolerance: int) -> Image:
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
                """if r_diff > g_diff and r_diff > b_diff:
                    val = 255 * ((r_diff - gap) / (1 - gap))
                elif g_diff > b_diff:
                    val = 255 * ((g_diff - gap) / (1 - gap))
                else:
                    val = 255 * ((b_diff - gap) / (1 - gap))
                """
                diff = (0.299 * r_diff + 0.587 * g_diff + 0.114 * b_diff)
                val = 255 - round(255 * (math.sqrt(diff)/(1 + pow(math.e, -8*(diff-gap)))))
                result.set_color(x, y, create_color(val, val, val))
    return result


"""
def cleanup_edges(input_image: Image) -> Image:
    result = copy(input_image)
    thickness = [0]*input_image.get_width()
    for x in range(input_image.get_width()):
        for y in range(input_image.get_height()):
            if input_image.get_color(x, y) == create_color(0, 0, 0):
                thickness[x] = thickness[x] + 1
            else:
                if thickness[x] > 4:
                    if thickness[x] & 1 == 1:
                        center = y - math.ceil(thickness[x]/2)
                        for i in range(y-thickness[x], y):
                            if abs(center-i) > 1:
                                result.set_color(x, i, create_color(255, 255, 255))
                    else:
                        center = y - (thickness[x]/2 + 0.5)
                        for i in range(y-thickness[x], y):
                            if abs(center-i) >= 2:
                                result.set_color(x, i, create_color(255, 255, 255))
                thickness[x] = 0
    return result
"""

if __name__ == "__main__":
    image = detect_edges(load_image(choose_file()), 30)
    show(image)
    save_as(image)
