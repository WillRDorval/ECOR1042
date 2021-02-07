#By Raunaq Hoque, Student ID: 101180524

from Cimpl import choose_file, load_image, copy, create_color, set_color,\
                  show, Image, get_color, create_image, Color, get_width,\
                  get_height

def flip_horizontal(image: Image) -> Image:
    """Return the flipped horizontal copy of the image.
    >>> image = load_image(choose_file()) 
    >>> horizontal_image=flip_horizontal(image)
    >>> show(horizontal_image)
    By Raunaq Hoque 101180524
    """
    new_image = copy(image)
    width = get_width(image)
    height = get_height(image)
    for y in range(height):
        for x in range(width//2):
            col_left = get_color(image, x, y)
            col_right = get_color(image, -x, y)
            set_color(new_image, -x, y, col_left)
            set_color(new_image, x, y, col_right) 
    return new_image

#Main Script
image=load_image(choose_file())
horizontal_image=flip_horizontal(image)
show(horizontal_image)