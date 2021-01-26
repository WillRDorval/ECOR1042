from Cimpl import choose_file, load_image, copy, create_color, set_color, show, Image, get_color, create_image
from unit_testing import check_equal


def red_channel(image: Image) -> Image:
    """
    Creates an image containing only the red channel of the given image.
    >>> test_image = load_image(choose_file())
    >>> test_result = red_channel(test_image)
    >>> show(test_result)
    """
    new_image = copy(image)
    for pixel in new_image:
        x, y, (r, g, b) = pixel
        red = create_color(r, 0, 0)
        set_color(new_image, x, y, red)
    return new_image


def red_channel_image_test(filepath: str):
    big_c = load_image(f"{filepath}.png")
    big_c_test = red_channel(big_c)
    big_c_red = load_image(f"{filepath}_red.png")
    success = True
    for i in range(big_c_test.get_width()):
        for j in range(big_c_test.get_height()):
            test_colour = get_color(big_c_test, i, j)
            red_colour = get_color(big_c_red, i, j)
            if test_colour != red_colour:
                success = False
                print(f"Non matching pixel at {i},{j} with test {test_colour} and expected {red_colour}")
    if success:
        print(f"{filepath} converted with no issues")
    else:
        print(f"{filepath} not converted successfully")


def red_channel_test():
    print("Running independent individual pixel checks")
    original = create_image(4, 1)
    set_color(original, 0, 0, create_color(107, 0, 0))
    set_color(original, 1, 0, create_color(127, 127, 127))
    set_color(original, 2, 0, create_color(0, 127, 127))
    set_color(original, 3, 0, create_color(0, 0, 0))

    expected = create_image(4, 1)
    set_color(expected, 0, 0, create_color(107, 0, 0))
    set_color(expected, 1, 0, create_color(127, 0, 0))
    set_color(expected, 2, 0, create_color(0, 0, 0))
    set_color(expected, 3, 0, create_color(0, 0, 0))

    red = red_channel(original)
    for x, y, col in red:
        check_equal(f"checking pixel {x},{y}", col, get_color(expected, x, y))


if __name__ == "__main__":
    """
    These tests compare the result of the function to a copy of the image that has had
    its red RGB channel isolated in external software. It will not work without the proper image files
    which I can email to you or add to CUlearn if you want me to.
    red_channel_image_test("great_big_c")
    red_channel_image_test("miss_sullivan")
    red_channel_image_test("riveter")
    """
    red_channel_test()
    show(red_channel(load_image(choose_file())))
