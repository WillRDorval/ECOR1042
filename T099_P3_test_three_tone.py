#By Raunaq Hoque, Student ID: 101180524

from Cimpl import create_color, create_image, get_color, set_color,\
                  Image

from  three_tone import three_tone, color_names

from unit_testing import check_equal

def test_three_tone() -> None:
    '''A test function for three_tone.
    >>> test_three_tone()
    By Raunaq Hoque 101180524
    '''
    original = create_image(3, 1)
    set_color(original, 0, 0,  create_color(100, 100, 50)) #testing color to covert to black
    set_color(original, 1, 0,  create_color(200, 200, 100)) #testing color to covert to blood
    set_color(original, 2, 0,  create_color(200, 200, 250)) #testing color to covert to white
 
    # Create an image that's identical to the one a correct implementation of
    # three_tone should produce when it is passed original.

    expected = create_image(3, 1)
    set_color(expected, 0, 0,  create_color(0, 0, 0)) #black
    set_color(expected, 1, 0,  create_color(255, 0, 0)) #blood
    set_color(expected, 2, 0,  create_color(255, 255, 255)) #white

    # Now compare the transformed image returned by the filter with the
    # expected image, one pixel at a time.

    threetone = three_tone(original, "black", "blood", "white")
    for x, y, col in threetone:  # col is the Color object for the pixel @ (x,y).
                                   # There's no need to unpack that object into
                                   # RGB components.
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))

test_three_tone()