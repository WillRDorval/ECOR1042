"""
T099 

Code made by Mohammad Saud
"""

from Cimpl import get_height, get_width, Image, create_image, get_color, Color,\
                  set_color, create_color, save_as, load_image, choose_file, show, copy
from unit_testing import check_equal



def color_names(color: str) -> tuple:
    """
    This function will take the name of a color and returns a tuple containing 
    the RGB values of that color.
    
    >>> a = color_names("grey")
    >>> print(a)
    ... (128,128,128)
    
    Made by Mohammad Saud 101195172
    """
    color_str = ("black","white","blood","green","blue","lemon","cyan","magenta","gray")
    color_values = ((0,0,0),(255,255,255),(255,0,0),(0,255,0),(0,0,255),(255,255,0),(0,255,255),(255,0,255),(128,128,128))
    
    for name in range(len(color_str)):
        if color == color_str[name]:
            return color_values[name]
            
    
def three_tone(org_img: Image, tone_1: str, tone_2: str, tone_3: str) -> Image:
    """
    This function will convert an image to a three tone image. The 3 tones will 
    be specified as their correct color names in lowercase.
    
    >>> image = load_image(choose_file())
    >>> new = three_tone(image, "black", "blood", "white")
    >>> show(new)
    
    Made by Mohammad Saud 101195172
    """
    
    r1,g1,b1 = color_names(tone_1)
    r2,g2,b2 = color_names(tone_2)
    r3,g3,b3 = color_names(tone_3)
    
    three_tone_image = copy(org_img)
    
    for x, y, (r,g,b) in three_tone_image:
        
        brightness = ((r+g+b)/3)
        
        if brightness <= 84:
            pix_color = create_color(r1,g1,b1)
            set_color(three_tone_image, x, y, pix_color)
        elif (brightness >= 85) and (brightness <= 170):
            pix_color = create_color(r2,g2,b2)
            set_color(three_tone_image, x, y, pix_color)
        elif (brightness >= 171) and (brightness <= 255):
            pix_color = create_color(r3,g3,b3)
            set_color(three_tone_image, x, y, pix_color)            

    return three_tone_image


image = load_image(choose_file())
new = three_tone(image, "black", "blood", "white")
show(new)
save_as(new)


