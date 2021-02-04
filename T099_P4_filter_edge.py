"""
Name: William Dorval
Student Number: 101187466
Class: ECOR1042
Section: D
"""

from Cimpl import choose_file, load_image, copy, create_color, set_color, show, Image, get_color


def accurate_grayscale(input_image: Image) -> Image:
    result = copy(input_image)
    for x, y, (r, g, b) in result:
        gray = round(0.299*r + 0.587*g + 0.114*b)
        set_color(result, x, y, create_color(gray, gray, gray))
    return result

def detect_edges(input_image: Image, tolerance: int) -> Image:
    if 100 < tolerance < 0:
        raise ValueError("tolerance must be a percentage form 0 to 100")

    result = Image(width=input_image.get_width(), height=input_image.get_height())
    gap = 255-255*(tolerance/100)
    for x in range(input_image.get_width()):
        for y in range(input_image.get_height()):
            try:
                if abs(input_image.get_color(x, y)[0] - input_image.get_color(x, y-1)[0]) >= gap:
                    result.set_color(x, y, create_color(0, 0, 0))
                elif abs(input_image.get_color(x, y)[1] - input_image.get_color(x, y-1)[1]) >= gap:
                    result.set_color(x, y, create_color(0, 0, 0))
                elif abs(input_image.get_color(x, y)[2] - input_image.get_color(x, y-1)[2]) >= gap:
                    result.set_color(x, y, create_color(0, 0, 0))
            except IndexError:
                pass

    return result


if __name__ == "__main__":
    show(detect_edges(load_image(choose_file()), 96))
