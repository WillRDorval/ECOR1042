"""
Team Submission

Team T099
Members: Mohammad Saud, William Dorval, Chaelan Murray, Raunaq Hoque

Red channel: William Dorval
Green channel: Chaelan Murray
Blue channel: Raunaq Hoque
Combine: Mohammad Saud

"""
from Cimpl import choose_file, load_image, copy, create_color, set_color, show, Image, get_color, create_image, \
    get_height, get_width, Color, save_as
from unit_testing import check_equal


# RED CHANNEL
def red_channel(input_image: Image) -> Image:
    """
    Creates an image containing only the red channel of the given image.
    >>> test_image = load_image(choose_file())
    >>> test_result = red_channel(test_image)
    >>> show(test_result)
    
    Created by William Dorval(101187466)
    """
    new_image = copy(input_image)
    for pixel in new_image:
        x, y, (r, g, b) = pixel
        red_colour = create_color(r, 0, 0)
        set_color(new_image, x, y, red_colour)
    return new_image


# RED CHANNEL TESTS
def red_channel_image_test(filepath: str):
    """
    A tests that loads an image and an a version of that image that has been manually
    changed to only have the red channel
    Created by William Dorval(101187466)
    """
    # Gimp was used to manually create the effects of the filters for comparison

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
    """
    Individually tests the red filter for a set of pixels containing all cases
    Created by William Dorval(101187466)
    """
    print("Running independent individual pixel checks")
    original = create_image(4, 1)
    set_color(original, 0, 0, create_color(107, 0, 0))  # only red channel active
    set_color(original, 1, 0, create_color(125, 126, 127))  # all channels active
    set_color(original, 2, 0, create_color(0, 127, 127))  # inactive red channel
    set_color(original, 3, 0, create_color(0, 0, 0))  # no channels active

    expected = create_image(4, 1)
    set_color(expected, 0, 0, create_color(107, 0, 0))
    set_color(expected, 1, 0, create_color(125, 0, 0))
    set_color(expected, 2, 0, create_color(0, 0, 0))
    set_color(expected, 3, 0, create_color(0, 0, 0))

    red = red_channel(original)
    for x, y, col in red:
        check_equal(f"checking pixel {x},{y}", col, get_color(expected, x, y))


# BLUE CHANNEL
def blue_channel(image: Image) -> Image:
    """Return the blue channel copy of image.
    >>> image = load_image(choose_file()) 
    >>> blue_image = blue_channel(image)
    >>> show(blue_image)
    
    Created by Raunaq Hoque (101180524)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        blue = create_color(0, 0, b)
        set_color(new_image, x, y, blue)
    return new_image


# BLUE CHANNEL TESTING
def test_blue_channel() -> None:
    """A test function for blue_channel.
    >>> test_blue_channel()

    Created by Raunaq Hoque (101180524)
    """
    original = create_image(3, 1)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(0, 0, 128))
    set_color(original, 2, 0, create_color(0, 0, 255))

    # Create an image that's identical to the one a correct implementation of
    # invert should produce when it is passed original.

    expected = create_image(3, 1)
    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 1, 0, create_color(0, 0, 128))
    set_color(expected, 2, 0, create_color(0, 0, 255))

    # Now compare the transformed image returned by the filter with the
    # expected image, one pixel at a time.

    bluechannel = blue_channel(original)
    for x, y, col in bluechannel:  # col is the Color object for the pixel @ (x,y).
        # There's no need to unpack that object into RGB components.
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))


# GREEN CHANNEL
def green_channel(image: Image) -> Image:
    """Return a new image that is the same as the original image but in the green filter.
    >>> image = load_image(choose_file())
    >>> green_image = green_channel(image)
    >>> show(green_image)
    
    Created by Chaelan Murray (101180990)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        green = create_color(0, g, 0)
        set_color(new_image, x, y, green)
    return new_image


# GREEN CHANNEL TESTING
def test_green_channel() -> None:
    """ Test the green_channel function.
    >>> test_green_channel()
    
    Created by Chaelan Murray (101180990)
    """
    original = create_image(5, 1)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(0, 1, 0))
    set_color(original, 2, 0, create_color(127, 0, 127))
    set_color(original, 3, 0, create_color(125, 73, 224))
    set_color(original, 4, 0, create_color(7, 255, 7))

    expected = create_image(5, 1)
    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 1, 0, create_color(0, 1, 0))
    set_color(expected, 2, 0, create_color(0, 0, 0))
    set_color(expected, 3, 0, create_color(0, 73, 0))
    set_color(expected, 4, 0, create_color(0, 255, 0))

    green_image = green_channel(original)

    for x, y, col in green_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')', col, get_color(expected, x, y))


# COMBINE FUNCTION
def combine(red_img: Image, green_img: Image, blue_img: Image) -> Image:
    """ 
    This function will return the combination of 3 images which are in color
    channels of red,green and blue. This will return a combined image which is
    fully colored.
    
    >>> red = load_image(choose_file())
    >>> blue = load_image(choose_file())
    >>> green = load_image(choose_file())
    >>> combination = combine(red, green, blue)
    >>> show(combination)
    
    Created by Mohammad Saud
    """

    final_height = get_height(red_img)
    final_width = get_width(red_img)

    combine_image = create_image(final_width, final_height)

    for x, y, (r, g, b) in combine_image:
        red_channel = get_color(red_img, x, y)
        (r1, g1, b1) = red_channel

        blue_channel = get_color(blue_img, x, y)
        (r2, g2, b2) = blue_channel

        green_channel = get_color(green_img, x, y)
        (r3, g3, b3) = green_channel

        pix_color = create_color(r1, g3, b2)
        set_color(combine_image, x, y, pix_color)

    return combine_image


# COMBINE TESTING FUNCTION
def test_combine() -> None:
    """
    The function will test whether the combine function works, no images will be 
    loaded, all tests are done internally. A message will be printed, whether 
    test was passed or failed at the location.
    
    >>>test_combine()
    
    Created by Mohammad Saud
    """
    red_test = create_image(3, 3, color=Color(red=255, green=0, blue=0))
    green_test = create_image(3, 3, color=Color(red=0, green=255, blue=0))
    blue_test = create_image(3, 3, color=Color(red=0, green=0, blue=255))
    # Creating 3 images that red,green and blue

    expected = create_image(3, 3, color=Color(red=255, green=255, blue=255))
    # A white image that is expected when combining all 3 colors

    test_original = combine(red_test, green_test, blue_test)

    for x, y, col in test_original:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))


if __name__ == '__main__':
    image = load_image(choose_file())
    red = red_channel(image)
    green = green_channel(image)
    blue = blue_channel(image)
    combination = combine(red, green, blue)
    save_as(combination, 'combined-image.png')
    show(combination)
