# Name: Chaelan Murray
# Student number: 101180990

from Cimpl import set_color, create_image, create_color, get_color
from unit_testing import check_equal
from T099_P4_filter_horizontal import flip_horizontal

def test_horizontal() -> None:
    """ Test the flip horizontal filter 
    >>> test_horizontal()
    """
    original = create_image(2, 3) 
    set_color(original, 0, 0,  create_color(20, 50, 60))
    set_color(original, 1, 1,  create_color(70, 80, 90))
    set_color(original, 0, 2,  create_color(255, 0, 255))
    set_color(original, 1, 0,  create_color(135, 135, 135))
    set_color(original, 0, 1,  create_color(0, 0, 0))
    set_color(original, 1, 2,  create_color(77, 77, 77))
    
    expected = create_image(2, 3) 
    set_color(expected, 0, 0,  create_color(135, 135, 135))
    set_color(expected, 1, 1,  create_color(0, 0, 0))
    set_color(expected, 0, 2,  create_color(77, 77, 77))
    set_color(expected, 1, 0,  create_color(20, 50, 60))
    set_color(expected, 0, 1,  create_color(70, 80, 90))
    set_color(expected, 1, 2,  create_color(255, 0, 255))

    horizontal_image = flip_horizontal(original)
    
    for x, y, col in expected:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')', col, get_color(horizontal_image, x, y))


# Main script 
if __name__ == '__main__':
    test_horizontal()