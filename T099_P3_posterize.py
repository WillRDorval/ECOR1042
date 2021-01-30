from Cimpl import choose_file, load_image, copy, create_color, set_color,\
                  show, Image, get_color, create_image, Color

def _adjust_component (r, g, b):
    p_col = [r,g,b]
    for i in range(3):
        if p_col[i] <= 63:
            p_col[i] = 31
        elif p_col[i] <= 127:
            p_col[i] = 95
        elif  p_col[i] <= 191:
            p_col[i] = 159
        elif p_col[i] <= 255:
            p_col[i] = 223 
        pixel = create_color(*p_col)
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