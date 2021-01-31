from Cimpl import *

def extreme_contrast((image: Image) -> Image :
    """ Returns a copy of an image with the contrast between the pixels being maximized. 
    >>> image = load_image(choose_file())
    >>> extreme_image = extreme_contrast(image)
    >>> show(extreme_image)
    """
    new_image = copy(image)
    red, green, blue = (r, g, b)
    for x, y, (r, g, b) in image:
        extreme = create_color(r, g, b)
        if red >= 127:
            red = 0
        elif red <= 128:
            red = 255
        if green >= 127:
            green = 0
        elif green <= 128:
            green = 255   
        if blue >= 127:
                blue = 0
        elif blue <= 128:
                blue = 255                 
        set_color(new_image, x, y, extreme)       
    return new_image    