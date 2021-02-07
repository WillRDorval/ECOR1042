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
    for y in range(height): #goes through all the y pixels
        for x in range(width//2): #goes through the x pixels until the halfway point
            col_left = get_color(image, x, y) #gets pixel colors on left handside of the image
            col_right = get_color(image, (width-1-x), y) #gets pixel colors on right handside of the image
            set_color(new_image, (width-1-x), y, col_left) #replace the pixels from the left onto the right
            set_color(new_image, x, y, col_right) #replace the pixels from the right onto the left
    return new_image #return the horizontally flipped image

#Main Script
if __name__ == '__main__':
    show(flip_horizontal(load_image(choose_file())))

print("End of file reached successfully.")
