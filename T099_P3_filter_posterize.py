#By Raunaq Hoque, Student ID: 101180524

from Cimpl import choose_file, load_image, copy, create_color, set_color,\
                  show, Image, get_color, create_image, Color

def _adjust_component (r, g, b):
    """Return the midpoint of the rgb component from the 4 quadrants 
    (0..63, 64..127, 128..191, and 192..255).
    >>> _adjust_component (60, 120, 190) 
    >>> (31, 95, 159)
    By Raunaq Hoque 101180524
    """    
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
    By Raunaq Hoque 101180524
    """
    new_image = copy(image)
    for x, y, (r,g,b) in image:
    
        color = _adjust_component (r,g,b)
        set_color(new_image, x, y, color)
    return new_image

image=load_image(choose_file())
posterize_image=posterize(image)
show(posterize_image)