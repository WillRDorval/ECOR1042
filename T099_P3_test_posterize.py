"""
T099 

Code made by Mohammad Saud
"""
from Cimpl import get_height, get_width, Image, create_image, get_color, Color,\
                  set_color, create_color, save_as, load_image, choose_file,\
                  show, copy

from unit_testing import check_equal
from T099_P3_posterize import _adjust_component, posterize



def test_posterize() -> None:
    """
    Test the green_channel function.
    
    >>> test_posterize()
    """
    
    original = create_image(5, 1) 
    # Lowest RGB values possible
    set_color(original, 0, 0,  create_color(0, 0, 0)) 
    # Only one non zero value
    set_color(original, 1, 0,  create_color(0, 128, 0))
    # Two non zero values
    set_color(original, 2, 0,  create_color(127, 0, 127))
    # Three non zero values
    set_color(original, 3, 0,  create_color(125, 22, 224))
    # Highest RGB values possible
    set_color(original, 4, 0,  create_color(255, 255, 255)) 
  
    expected = create_image(5, 1) 
    set_color(expected, 0, 0,  create_color(31, 31, 31))
    set_color(expected, 1, 0,  create_color(31, 159, 31))
    set_color(expected, 2, 0,  create_color(95, 31, 95))
    set_color(expected, 3, 0,  create_color(95, 31, 223))
    set_color(expected, 4, 0,  create_color(223, 223, 223)) 
  
    post_test_image = posterize(original)
    
    for x, y, col in post_test_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')', col,\
                    get_color(expected, x, y))
        
          
test_posterize()