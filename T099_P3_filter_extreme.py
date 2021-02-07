# Chaelan Murray 
# 101180990

from Cimpl import *


def extreme_contrast(image: Image) -> Image:
    """ Returns a copy of an image with the contrast between the pixels being maximized. 
    >>> original_image = load_image(choose_file())
    >>> extreme_image = extreme_contrast(original_image)
    >>> show(extreme_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        col = [r, g, b]
        for t in range(3):
            if col[t] >= 128:
                col[t] = 255
            else:
                col[t] = 0
        extreme = create_color(*col)
        set_color(new_image, x, y, extreme)
    return new_image


# Main Script 
if __name__ == '__main__':
    show(extreme_contrast(load_image(choose_file())))

print("End of file reached successfully.")
