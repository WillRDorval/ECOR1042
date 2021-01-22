"""
Team T099
Members: Mohammad Saud, William Dorval, Chaelan Murray, Raunaq Hoque

"""
from Cimpl import choose_file, load_image, copy, create_color, set_color, show, Image, get_color, create_image
from unit_testing import check_equal

#RED CHANNEL
def red_channel(image: Image) -> Image:
    """
    Creates an image containing only the red channel of the given image.
    >>> test_image = load_image(choose_file())
    >>> test_result = red_channel(test_image)
    >>> show(test_result)
    """
    new_image = copy(image)
    for pixel in new_image:
        x, y, (r, g, b) = pixel
        red = create_color(r, 0, 0)
        set_color(new_image, x, y, red)
    return new_image

#RED CHANNEL TESTS
def red_channel_image_test(filepath: str):
    big_c = load_image(f"{filepath}.png")
    big_c_test = red_channel(big_c)
    big_c_red = load_image(f"{filepath}_red.png")
    success = True
    for i in range(big_c_test.get_width()):
        for j in range(big_c_test.get_height()):
            test_colour = get_color(big_c_test, i, j)
            red_colour = get_color(big_c_red, i, j)
            if test_colour != red_colour:
                success = False
                print(f"Non matching pixel at {i},{j} with test {test_colour} and expected {red_colour}")
    if success:
        print(f"{filepath} converted with no issues")
    else:
        print(f"{filepath} not converted successfully")


def red_channel_test():
    print("Running independent individual pixel checks")
    original = create_image(4, 1)
    set_color(original, 0, 0, create_color(107, 0, 0))
    set_color(original, 1, 0, create_color(127, 127, 127))
    set_color(original, 2, 0, create_color(0, 127, 127))
    set_color(original, 3, 0, create_color(0, 0, 0))
    
    expected = create_image(4, 1)
    set_color(expected, 0, 0, create_color(107, 0, 0))
    set_color(expected, 1, 0, create_color(127, 0, 0))
    set_color(expected, 2, 0, create_color(0, 0, 0))
    set_color(expected, 3, 0, create_color(0, 0, 0))

    red = red_channel(original)
    for x, y, col in red:
        check_equal(f"checking pixel {x},{y}", col, get_color(expected, x, y))

#BLUE CHANNEL
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

#BLUE CHANNEL TESTING
def test_blue_channel() -> None:
    '''A test function for blue_channel.
    >>> test_blue_channel()
    '''
    original = create_image(3, 1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(0, 0, 128))
    set_color(original, 2, 0,  create_color(0, 0, 255))

    # Create an image that's identical to the one a correct implementation of
    # invert should produce when it is passed original.

    expected = create_image(3, 1)
    set_color(expected, 0, 0,  create_color(0, 0, 0))
    set_color(expected, 1, 0,  create_color(0, 0, 128))
    set_color(expected, 2, 0,  create_color(0, 0, 255))

    # Now compare the transformed image returned by the filter with the
    # expected image, one pixel at a time.

    bluechannel = blue_channel(original)
    for x, y, col in bluechannel:  # col is the Color object for the pixel @ (x,y).
                                   # There's no need to unpack that object into
                                   # RGB components.
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))



#COMBINE FUNCTION
def combine(red_img: Image, green_img: Image, blue_img: Image) -> Image:
    """ 
    This function will return the combinattion of 3 images which are in color
    channels of red,green and blue. This will return a combined image which is
    fully colored.
    
    >>> red = load_image(choose_file())
    >>> blue = load_image(choose_file())
    >>> green = load_image(choose_file())
    >>> combination = combine(red, green, blue)
    >>> show(combination)
    
    Created by Mohammad Saud(101195172)
    """
    
    final_height = get_height(red_img)
    final_width = get_width(red_img)
    
    combine_image = create_image(final_width, final_height)

    for x, y , (r,g,b) in combine_image:
        red_channel = get_color(red_img, x, y)
        (r1,g1,b1) = red_channel
        
        blue_channel = get_color(blue_img, x, y)
        (r2,g2,b2) = blue_channel
        
        green_channel = get_color(green_img, x, y)
        (r3,g3,b3) = green_channel
        
        pix_color = create_color(r1,g3,b2)
        set_color(combine_image, x, y, pix_color)

    return combine_image

#COMBINE TESTING FUNCTION
def test_combine() -> None:
    """
    The function will create 3 images that are red, green and blue. Then use the 
    combine filter to check whether the image is the same as the expected
    
    >>>test_combine()
    
    Created by Mohammad Saud(101195172)
    """
    red_test = create_image(3,3, color=Color(red=255, green= 0, blue= 0))
    green_test = create_image(3,3, color=Color(red=0, green= 255, blue= 0))
    blue_test = create_image(3,3, color=Color(red=0, green= 0, blue= 255))
    
    expected = create_image(3,3, color=Color(red=255, green= 255, blue= 255))
    
    test_original = combine(red_test, green_test, blue_test)
    
    for x, y, col in test_original:                        
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))    


#MAIN SCRIPTS
#RED SCRIPT

if __name__ == "__main__":
    red_channel_image_test("great_big_c")
    red_channel_image_test("miss_sullivan")
    red_channel_image_test("riveter")
    red_channel_test()

#BLUE SCRIPT

#BLUE TEST CALL
test_blue_channel()

#COMBINE SCRIPT

red = load_image(choose_file())
green = load_image(choose_file())
blue = load_image(choose_file())
combination = combine(red, green, blue)
save_as(combination, 'combined-image.png')
show(combination)

#COMBINE TEST
test_combine()