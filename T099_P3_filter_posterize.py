from Cimpl import choose_file, load_image, copy, create_color, set_color,\
                  show, Image, get_color, create_image, Color

def _adjust_component (r, g, b):
    pixel_color = [r,g,b]
    for i in range(3):
        if pixel_color[i] <= 63:
            pixel_color[i] = 31
        elif pixel_color[i] <= 127:
            pixel_color[i] = 95
        elif  pixel_color[i] <= 191:
            pixel_color[i] = 159
        elif pixel_color[i] <= 255:
            pixel_color[i] = 223 
        pixel = create_color(*pixel_color)
    return pixel    

def posterize(image: Image) -> Image:
    """Return the posterized copy of image.
    >>> image = load_image(choose_file()) 
    >>> posterize_image=posterize(image)
    >>> show(posterize_image)    
    """
    new_image = copy(image)
    for x, y, (r,g,b) in image:
    
        color = _adjust_component (r,g,b)
        set_color(new_image, x, y, color)
    return new_image

image=load_image(choose_file())
posterize_image=posterize(image)
show(posterize_image)