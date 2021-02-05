# Name: Chaelan Murray
# Student number: 101180990

from Cimpl import *

def flip_vertical(image: Image) -> Image:
    """  Returns a copy of the image, flipped along the middle horizontal line.
    >>> orignial_image = load_image(choose_file())
    >>> extreme_image = flip_vertical(orignial_image)
    >>> show(flip_vertical)
    """
    width = get_width(image)
    height = get_height(image)
    new_image = copy(image)
    for x in range(width):
        for y in range(height // 2):
            top = get_color(image, x, y)
            bottom = get_color(image, x, (height - 1 - y))
            set_color(new_image, x, (height - 1 - y), top)
            set_color(new_image, x, y, bottom)   
    return new_image
   
# Main Script
if __name__ == '__main__':
    show(flip_vertical(load_image(choose_file())))

print("End of file reached successfully.")