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

red = load_image(choose_file())
green = load_image(choose_file())
blue = load_image(choose_file())
combination = combine(red, green, blue)
#save_as(combination, 'combined_image.png')
show(combination)

original = load_image(choose_file())
combination_sv = load_image(choose_file())
#check_equal("provided original image with combined image", combination_sv, original)

if original == combination_sv:
    print("pass")
else:
    print("failed")



    
    