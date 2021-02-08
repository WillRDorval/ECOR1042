"""
Name: William Dorval
Student Number: 101187466
Class: ECOR1042
Section: D
"""

import math

from Cimpl import choose_file, load_image, copy, create_color, show, Image


def grayscale(input_image: Image) -> Image:
    """
    copied from simple cimpl filters
    """
    result = copy(input_image)
    for x, y, (r, g, b) in input_image:
        gray = (r+g+b)/3
        result.set_color(x, y, create_color(gray, gray, gray))

    return result


def detect_edges(input_image: Image, threshold: int) -> Image:
    """
    Returns an image with only edges of the original image in black with the rest of the image
    in white. Edges are detected by change in brightness which must be greater than the given threshold.
    >>> loaded_image = load_image(choose_file())
    >>> edge_image = detect_edges(loaded_image)
    >>> show(edge_image)
    """
    # uses grayscale filter to get  brightness of each pixel
    brightness = grayscale(input_image)
    # creates empty white canvas the same size as the original image
    result = Image(width=input_image.get_width(), height=input_image.get_height())
    # checks each pixel, if the change in brightness is enough, it sets that position in the result to black
    for x, y, (r, _, _) in brightness:
        if abs(r - brightness.get_color(x, y-1)[0]) > threshold:
            result.set_color(x, y, create_color(0, 0, 0))

    return result

# this is a function I devised to make a much more accurate pencil like sketch of the given image
def real_detect_edges(input_image: Image, tolerance: int) -> Image:
    # ensures the tolerance is within acceptable ranges
    if 100 < tolerance < 0:
        raise ValueError("tolerance must be a percentage form 0 to 100")

    # creates a properly sized blank canvas
    result = Image(width=input_image.get_width(), height=input_image.get_height())
    # turns the tolerance into a decimal
    gap = tolerance / 100
    for x in range(input_image.get_width()):
        for y in range(input_image.get_height()):
            # for each position in the image
            try:
                # compares the squares of the changes in each colour between given position and pixel below
                r_diff = abs((orig := input_image.get_color(x, y)[0]**2) - (new := input_image.get_color(x, y - 1)[0]**2))
                # turns it into a relative difference (0-1) then repeat for each colour
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

                # makes the same comparison as before but now checking to the side
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

                # selects the larger of the two differences for use in calculation
                if r_side > r_diff:
                    r_diff = r_side
                if g_side > g_diff:
                    g_diff = g_side
                if b_side > b_diff:
                    b_diff = b_side

            except IndexError:  # if the comparisons go out of bounds, the pixel will be left white
                pass

            else:  # so long as no exception was thrown
                # calculates the total difference in lightness based on the human perception of different colours
                diff = (0.299 * r_diff + 0.587 * g_diff + 0.114 * b_diff)
                # passes the difference in lightness through a function to determine the darkness that should be drawn
                # at that point. The threshold is used here as a modifier to change how much change must occur for the
                # value to be as light or dark
                val = 255 - round(255 * (math.sqrt(diff)/(1 + pow(math.e, -8*(diff-gap)))))
                # updates the canvas to the correct darkness at the position
                result.set_color(x, y, create_color(val, val, val))
    return result


if __name__ == "__main__":
    image = detect_edges(load_image(choose_file()), 10)
    show(image)

    # uncomment code below to try out the more accurate detect edges the first should be a very clean pencil like
    # drawing and the second should only show very significant edges in the image
    image = real_detect_edges(load_image(choose_file()), 0)
    show(image)

    image = real_detect_edges(load_image(choose_file()), 50)
    show(image)
    # the threshold can be adjusted based on the image and what result you want, higher than 50 isn't recommended in
    # most cases as the filter will become too selective to be useful in most cases

