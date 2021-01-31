from Cimpl import set_color, create_image, create_color, get_color
from unit_testing import check_equal
from T099_P3_sepia import sepia


def test_sepia() -> None:
    """ Test the sepia filter 
    >>> test_sepia()
    """
    original = create_image(5, 1) 
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(62, 62, 62))
    set_color(original, 2, 0,  create_color(63 , 63, 63))
    set_color(original, 3, 0,  create_color(191, 191, 191))
    set_color(original, 4, 0,  create_color(255, 255, 255)) 
  
    expected = create_image(5, 1) 
    set_color(expected, 0, 0,  create_color(0, 0, 0))
    set_color(expected, 1, 0,  create_color(68.2, 62, 55.8))
    set_color(expected, 2, 0,  create_color(72.45, 63, 53.55))
    set_color(expected, 3, 0,  create_color(219.65, 191, 162.35))
    set_color(expected, 4, 0,  create_color(255, 255, 237.15)) 
  
    sepia_image = sepia(original)
    
    for x, y, col in expected:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')', col, get_color(expected, x, y))    


# Main script 
if __name__ == '__main__':
    test_sepia()
