"""
T099

Made by Mohammad Saud 101195172
"""

from Cimpl import choose_file, load_image, copy, create_color, set_color, show, Image, save_as, get_color
import math
from T099_P4_filter_edge import *
from unit_testing import check_equal

def test_edge () -> None:
    """
    Tests the detect_edges fiter. 
    
    >>> test_edge()
    
    Made by Mohammad Saud
    """
    
    original = create_image(3, 2) 
    set_color(original, 0, 0,  create_color(25,23, 24)) 
    set_color(original, 1, 0,  create_color(255, 255, 255))
    set_color(original, 2, 0,  create_color(127, 0, 127))
    set_color(original, 0, 1,  create_color(41, 3,11))
    set_color(original, 1, 1,  create_color(255, 255, 255)) 
    set_color(original, 2, 1,  create_color(173, 255, 123))
  
    expected = create_image(3, 2) 
    set_color(expected, 0, 0,  create_color(255,255,255))
    set_color(expected, 1, 0,  create_color(255,255,255))
    set_color(expected, 2, 0,  create_color(0,0,0))
    set_color(expected, 0, 1,  create_color(255,255,255))
    set_color(expected, 1, 1,  create_color(255,255,255)) 
    set_color(expected, 2, 1,  create_color(0,0,0)) 
  
    edge_test_image = detect_edges(original,10)
    
    for x, y, col in edge_test_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')', col,\
                    get_color(expected, x, y))    
        
test_edge()