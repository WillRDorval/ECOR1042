from Cimpl import *
from unit_testing import check_equal

def green_channel(image: Image) -> Image:
    """Return a new image that is the same as the original image but in the green filter.
    >>> image = load_image(choose_file())
    >>> green_image = green_channel(image)
    >>> show(green_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        green = create_color(0, g, 0)    
        set_color(new_image, x, y, green)       
    return new_image

def test_green_channel() -> None:
    """ Test the green_channel function.
    >>> test_green_channel()
    """
    original = create_image(5, 1) 
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(0, 1, 0))
    set_color(original, 2, 0,  create_color(127, 0, 127))
    set_color(original, 3, 0,  create_color(125, 73, 224))
    set_color(original, 4, 0,  create_color(7, 255, 7)) 
  
    expected = create_image(5, 1) 
    set_color(expected, 0, 0,  create_color(0, 0, 0))
    set_color(expected, 1, 0,  create_color(0, 1, 0))
    set_color(expected, 2, 0,  create_color(0, 0, 0))
    set_color(expected, 3, 0,  create_color(0, 73, 0))
    set_color(expected, 4, 0,  create_color(0, 255, 0)) 
  
    green_image = green_channel (original)
    
    for x, y, col in green_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')', col, get_color(expected, x, y))
    

# Main Script 
show (green_channel(load_image(choose_file())))
test_green_channel()

print("End of file reached successfully.")