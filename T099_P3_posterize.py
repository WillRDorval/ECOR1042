from Cimpl import choose_file, load_image, copy, create_color, set_color,\
                  show, Image, get_color, create_image, Color

def _adjust_component (a, b, c):
    for i in range(3):
        if ((r,g,b)[i] <= 63):
            (r,g,b)[i] = 31
        elif ((r,g,b)[i] >= 64) and ((r,g,b)[i] <= 127):
            (r,g,b)[i] = 95
        elif ((r,g,b)[i] >= 128) and ((r,g,b)[i] <= 191):
            (r,g,b)[i] = 159
        elif ((r,g,b)[i] >= 192) and ((r,g,b)[i] <= 255):
            (r,g,b)[i] = 223 
        pixel = create_color(r, g, b)
    return pixel    

def posterize(image: Image) -> Image:
    """Return the blue channel copy of image.
    >>> image = load_image(choose_file()) 
    >>> blue_image = posterize(image)
    >>> show(blue_image)     
    """
    new_image = copy(image)
    for x, y, (r,g,b) in image:
    
        color = _adjust_component (r,g,b)
        set_color(new_image, x, y, color)
    return new_image

image=load_image(choose_file())
yes=posterize(image)
show(yes)