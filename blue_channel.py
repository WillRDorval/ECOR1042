from Cimpl import choose_file, load_image, copy, create_color, set_color,\
                  show, Image, get_color

def blue_channel(image: Image) -> Image:
    """Return the blue channel copy of image.
    >>> image = load_image(choose_file()) 
    >>> blue_image = blue_channel(image)
    >>> show(blue_image)     
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        blue = create_color(0, 0, b)
        set_color(new_image, x, y, blue)       
    return new_image
