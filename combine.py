"""
Mohammad Saud (101195172) Combine Function
Team T099
Members: Mohammad Saud, William Dorval, Chaelan Murray, Raunaq Hoque

"""
from Cimpl import *
from unit_testing import *

def combine(red_img: Image, green_img: Image, blue_img: Image) -> Image:
    """ 
    This function will return the combinattion of 3 images which are in color
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

    for x, y , (r,g,b) in combine_image:
        red_channel = get_color(red_img, x, y)
        (r1,g1,b1) = red_channel
        
        blue_channel = get_color(blue_img, x, y)
        (r2,g2,b2) = blue_channel
        
        green_channel = get_color(green_img, x, y)
        (r3,g3,b3) = green_channel
        
        pix_color = create_color(r1,g3,b2)
        set_color(combine_image, x, y, pix_color)

    return combine_image


def test_combine() -> None:
    """
    The function will create 3 images that are red, green and blue. Then use the 
    combine filter to check whether the image is the same as the expected
    
    >>>test_combine()
    
    Created by Mohammad Saud
    """
    red_test = create_image(3,3, color=Color(red=255, green= 0, blue= 0))
    green_test = create_image(3,3, color=Color(red=0, green= 255, blue= 0))
    blue_test = create_image(3,3, color=Color(red=0, green= 0, blue= 255))
    
    expected = create_image(3,3, color=Color(red=255, green= 255, blue= 255))
    
    test_original = combine(red_test, green_test, blue_test)
    
    for x, y, col in test_original:                        
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))    
    
    
#MAIN SCRIPT    

# Using the combine function
red = load_image(choose_file())
green = load_image(choose_file())
blue = load_image(choose_file())
combination = combine(red, green, blue)
show(combination)

#Testing whether the combine function works
test_combine()








    
    