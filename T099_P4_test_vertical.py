#By Raunaq Hoque, Student ID: 101180524

from Cimpl import create_color, create_image, get_color, set_color,\
                  Image

from T099_P4_filter_vertical import flip_vertical

from unit_testing import check_equal

def test_flip_vertical() -> None:
    '''A test function for flip_vertical.
    >>> test_flip_vertical()
    By Raunaq Hoque 101180524
    '''
    original = create_image(3, 2)
    set_color(original, 0, 0,  create_color(50, 50, 50))
    set_color(original, 1, 0,  create_color(100, 100, 100)) 
    set_color(original, 2, 0,  create_color(200, 200, 200))
    set_color(original, 0, 1,  create_color(75, 75, 75))
    set_color(original, 1, 1,  create_color(125, 125, 125)) 
    set_color(original, 2, 1,  create_color(175, 175, 175))    
 
    # Create an image that's identical to the one a correct implementation of
    # flip_vertical should produce when it is passed original.

    expected = create_image(3, 2)
    set_color(expected, 0, 0,  create_color(75, 75, 75))
    set_color(expected, 1, 0,  create_color(125, 125, 125)) 
    set_color(expected, 2, 0,  create_color(175, 175, 175))
    set_color(expected, 0, 1,  create_color(50, 50, 50))
    set_color(expected, 1, 1,  create_color(100, 100, 100)) 
    set_color(expected, 2, 1,  create_color(200, 200, 200)) 

    # Now compare the transformed image returned by the filter with the
    # expected image, one pixel at a time.

    flipvertical = flip_vertical(original)
    for x, y, col in flipvertical:  # col is the Color object for the pixel @ (x,y).
                                   # There's no need to unpack that object into
                                   # RGB components.
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))

# Main script 
if __name__ == '__main__':
    test_flip_vertical()