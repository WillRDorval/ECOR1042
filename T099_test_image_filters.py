"""
Submission by T099
Submission on 7th February 2021

William Dorval 
Raunaq Hoqie
Chaelan Murray
Mohammad Saud
"""

from Cimpl import choose_file, load_image, copy, create_color, set_color, show, Image, save_as, get_color, create_image

import math
from T099_image_filters import *
from unit_testing import check_equal

#Test for extreme_contrast
def test_contrast():
    """
    Test for the extreme contrast filter
    
    >>>test_contrast()
    
    Made by William Dorval 101187466
    """
    original = create_image(28, 1)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(60, 0, 0))
    set_color(original, 2, 0, create_color(0, 60, 0))
    set_color(original, 3, 0, create_color(0, 0, 60))
    set_color(original, 4, 0, create_color(60, 60, 0))
    set_color(original, 5, 0, create_color(60, 0, 60))
    set_color(original, 6, 0, create_color(0, 60, 60))
    set_color(original, 7, 0, create_color(60, 255, 255))
    set_color(original, 8, 0, create_color(255, 60, 255))
    set_color(original, 9, 0, create_color(255, 255, 60))
    set_color(original, 10, 0, create_color(60, 60, 255))
    set_color(original, 11, 0, create_color(60, 255, 60))
    set_color(original, 12, 0, create_color(255, 60, 60))
    set_color(original, 13, 0, create_color(60, 60, 60))
    set_color(original, 14, 0, create_color(160, 0, 0))
    set_color(original, 15, 0, create_color(0, 160, 0))
    set_color(original, 16, 0, create_color(0, 0, 160))
    set_color(original, 17, 0, create_color(160, 160, 0))
    set_color(original, 18, 0, create_color(160, 0, 160))
    set_color(original, 19, 0, create_color(0, 160, 160))
    set_color(original, 20, 0, create_color(160, 255, 255))
    set_color(original, 21, 0, create_color(255, 160, 255))
    set_color(original, 22, 0, create_color(255, 255, 160))
    set_color(original, 23, 0, create_color(160, 160, 255))
    set_color(original, 24, 0, create_color(160, 255, 160))
    set_color(original, 25, 0, create_color(255, 160, 160))
    set_color(original, 26, 0, create_color(160, 160, 160))
    set_color(original, 27, 0, create_color(255, 255, 255))

    contrasted = extreme_contrast(original)

    expected = create_image(28, 1)
    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 1, 0, create_color(0, 0, 0))
    set_color(expected, 2, 0, create_color(0, 0, 0))
    set_color(expected, 3, 0, create_color(0, 0, 0))
    set_color(expected, 4, 0, create_color(0, 0, 0))
    set_color(expected, 5, 0, create_color(0, 0, 0))
    set_color(expected, 6, 0, create_color(0, 0, 0))
    set_color(expected, 7, 0, create_color(0, 255, 255))
    set_color(expected, 8, 0, create_color(255, 0, 255))
    set_color(expected, 9, 0, create_color(255, 255, 0))
    set_color(expected, 10, 0, create_color(0, 0, 255))
    set_color(expected, 11, 0, create_color(0, 255, 0))
    set_color(expected, 12, 0, create_color(255, 0, 0))
    set_color(expected, 13, 0, create_color(0, 0, 0))
    set_color(expected, 14, 0, create_color(255, 0, 0))
    set_color(expected, 15, 0, create_color(0, 255, 0))
    set_color(expected, 16, 0, create_color(0, 0, 255))
    set_color(expected, 17, 0, create_color(255, 255, 0))
    set_color(expected, 18, 0, create_color(255, 0, 255))
    set_color(expected, 19, 0, create_color(0, 255, 255))
    set_color(expected, 20, 0, create_color(255, 255, 255))
    set_color(expected, 21, 0, create_color(255, 255, 255))
    set_color(expected, 22, 0, create_color(255, 255, 255))
    set_color(expected, 23, 0, create_color(255, 255, 255))
    set_color(expected, 24, 0, create_color(255, 255, 255))
    set_color(expected, 25, 0, create_color(255, 255, 255))
    set_color(expected, 26, 0, create_color(255, 255, 255))
    set_color(expected, 27, 0, create_color(255, 255, 255))
    
    for x, y, col in expected:
        actual = get_color(contrasted, x, y)
        check_equal(f"checking pixel at {x}, {y}", actual, col)

#Test function for posterize        
def test_posterize() -> None:
    """
    Test for the posterize function.
    
    >>> test_posterize()
    
    Made by Mohammad Saud 101195172
    """
    
    original = create_image(5, 1) 
    # Lowest RGB values possible
    set_color(original, 0, 0,  create_color(0, 0, 0)) 
    # Only one non zero value
    set_color(original, 1, 0,  create_color(0, 128, 0))
    # Two non zero values
    set_color(original, 2, 0,  create_color(127, 0, 127))
    # Three non zero values
    set_color(original, 3, 0,  create_color(125, 22, 224))
    # Highest RGB values possible
    set_color(original, 4, 0,  create_color(255, 255, 255)) 
  
    expected = create_image(5, 1) 
    set_color(expected, 0, 0,  create_color(31, 31, 31))
    set_color(expected, 1, 0,  create_color(31, 159, 31))
    set_color(expected, 2, 0,  create_color(95, 31, 95))
    set_color(expected, 3, 0,  create_color(95, 31, 223))
    set_color(expected, 4, 0,  create_color(223, 223, 223)) 
  
    post_test_image = posterize(original)
    
    for x, y, col in post_test_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')', col,\
                    get_color(expected, x, y))
        
#Test for sepia filter
def test_sepia() -> None:
    """ 
    Test the sepia filter 
    
    >>> test_sepia()
    
    Made by Chaelan Murray 101180990
    """
    original = create_image(5, 1) 
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(62, 62, 62))
    set_color(original, 2, 0,  create_color(63, 63, 63))
    set_color(original, 3, 0,  create_color(191, 191, 191))
    set_color(original, 4, 0,  create_color(255, 255, 255))

    expected = create_image(5, 1) 
    set_color(expected, 0, 0,  create_color(0, 0, 0))
    set_color(expected, 1, 0,  create_color(68.2, 62, 55.8))
    set_color(expected, 2, 0,  create_color(72.45, 63, 53.55))
    set_color(expected, 3, 0,  create_color(219.65, 191, 162.35))
    set_color(expected, 4, 0,  create_color(255, 255, 237.15)) 
  
    sepia_image = sepia(original)
    
    for x, y, col in expected:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')', col, get_color(sepia_image, x, y))

#Test for three tone filter
def test_three_tone() -> None:
    '''
    A test function for three_tone.
    
    >>> test_three_tone()
    
    By Raunaq Hoque 101180524
    '''
    original = create_image(3, 1)
    set_color(original, 0, 0,  create_color(100, 100, 50)) #testing color to covert to black
    set_color(original, 1, 0,  create_color(200, 200, 100)) #testing color to covert to blood
    set_color(original, 2, 0,  create_color(200, 200, 250)) #testing color to covert to white
 
    # Create an image that's identical to the one a correct implementation of
    # three_tone should produce when it is passed original.

    expected = create_image(3, 1)
    set_color(expected, 0, 0,  create_color(0, 0, 0)) #black
    set_color(expected, 1, 0,  create_color(255, 0, 0)) #blood
    set_color(expected, 2, 0,  create_color(255, 255, 255)) #white

    # Now compare the transformed image returned by the filter with the
    # expected image, one pixel at a time.

    threetone = three_tone(original, "black", "blood", "white")
    for x, y, col in threetone:  # col is the Color object for the pixel @ (x,y).
                                   # There's no need to unpack that object into
                                   # RGB components.
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))
        
#Test for draw_curve filter        
def test_curve():
    """
    Tests the draw curve filter
    
    >>>test_curve()
    
    Made by William Dorval 101187466
    """
    original = Image(width=20, height=20)
    result = draw_curve(original, "magenta", points=[(1, 1), (2, 2)])

    magenta = create_color(255, 0, 255)
    expected = Image(width=20, height=20)
    for x, y, (_, _, _) in expected:
        if abs(x-y) <= 2:
            expected.set_color(x, y, magenta)
    for x, y, color in result:
        pass
        check_equal(f"Testing pixel {x}, {y}", color, expected.get_color(x, y))

    # parabolic interpolation
    original = Image(width=50, height=50)
    result = draw_curve(original, "lemon", points=[(0, 1), (10, 3), (20, 7)])

    lemon = create_color(255, 255, 0)
    expected = Image(width=50, height=50)
    for x, y, (_, _, _) in expected:
        if abs(int((0.01*(x**2) + (0.1*x) + 1)) - y) <= 2:
            expected.set_color(x, y, lemon)
    for x, y, color in result:
        pass
        check_equal(f"Testing pixel {x}, {y}", color, expected.get_color(x, y))

    original = Image(width=50, height=50)
    result = draw_curve(original, "cyan", points=[(0, 1), (10, 3), (20, 7), (30, 13)])

    cyan = create_color(0, 255, 255)
    expected = Image(width=50, height=50)
    for x, y, (_, _, _) in expected:
        if abs(int((0.009999999999999992 * (x ** 2) + (0.10000000000000024 * x) + 1.0000000000000007)) - y) <= 2:
            expected.set_color(x, y, cyan)
    for x, y, color in result:
        check_equal(f"Testing pixel {x}, {y}", color, expected.get_color(x, y))

#Test for edge detection filter        
def test_edge () -> None:
    """
    Tests the detect_edges fiter. 
    
    >>> test_edge()
    
    Made by Mohammad Saud 101195172
    """
    
    original = create_image(3, 2) 
    set_color(original, 0, 0,  create_color(25,23, 24)) 
    set_color(original, 1, 0,  create_color(255, 255, 255))
    set_color(original, 2, 0,  create_color(127, 0, 127))
    set_color(original, 0, 1,  create_color(41, 3,11))
    set_color(original, 1, 1,  create_color(255, 255, 255)) 
    set_color(original, 2, 1,  create_color(173, 255, 123))
  
    expected = create_image(3, 2) 
    set_color(expected, 0, 0,  create_color(255,255,255))
    set_color(expected, 1, 0,  create_color(255,255,255))
    set_color(expected, 2, 0,  create_color(0,0,0))
    set_color(expected, 0, 1,  create_color(255,255,255))
    set_color(expected, 1, 1,  create_color(255,255,255)) 
    set_color(expected, 2, 1,  create_color(0,0,0)) 
  
    edge_test_image = detect_edges(original,10)
    
    for x, y, col in edge_test_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')', col,\
                    get_color(expected, x, y))

#Test for vertical flip filter
def test_flip_vertical() -> None:
    '''A test function for flip_vertical.
    >>> test_flip_vertical()
    By Raunaq Hoque 101180524
    '''
    original = create_image(3, 2)
    set_color(original, 0, 0,  create_color(50, 50, 50))
    set_color(original, 1, 0,  create_color(100, 100, 100)) 
    set_color(original, 2, 0,  create_color(200, 200, 200))
    set_color(original, 0, 1,  create_color(75, 75, 75))
    set_color(original, 1, 1,  create_color(125, 125, 125)) 
    set_color(original, 2, 1,  create_color(175, 175, 175))    
 
    # Create an image that's identical to the one a correct implementation of
    # flip_vertical should produce when it is passed original.

    expected = create_image(3, 2)
    set_color(expected, 0, 0,  create_color(75, 75, 75))
    set_color(expected, 1, 0,  create_color(125, 125, 125)) 
    set_color(expected, 2, 0,  create_color(175, 175, 175))
    set_color(expected, 0, 1,  create_color(50, 50, 50))
    set_color(expected, 1, 1,  create_color(100, 100, 100)) 
    set_color(expected, 2, 1,  create_color(200, 200, 200)) 

    # Now compare the transformed image returned by the filter with the
    # expected image, one pixel at a time.

    flipvertical = flip_vertical(original)
    for x, y, col in flipvertical:  # col is the Color object for the pixel @ (x,y).
                                   # There's no need to unpack that object into
                                   # RGB components.
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))

        
def test_horizontal() -> None:
    """ Test the flip horizontal filter 
    >>> test_horizontal()
    """
    original = create_image(2, 3) 
    set_color(original, 0, 0,  create_color(20, 50, 60))
    set_color(original, 1, 1,  create_color(70, 80, 90))
    set_color(original, 0, 2,  create_color(255, 0, 255))
    set_color(original, 1, 0,  create_color(135, 135, 135))
    set_color(original, 0, 1,  create_color(0, 0, 0))
    set_color(original, 1, 2,  create_color(77, 77, 77))
    
    expected = create_image(2, 3) 
    set_color(expected, 0, 0,  create_color(135, 135, 135))
    set_color(expected, 1, 1,  create_color(0, 0, 0))
    set_color(expected, 0, 2,  create_color(77, 77, 77))
    set_color(expected, 1, 0,  create_color(20, 50, 60))
    set_color(expected, 0, 1,  create_color(70, 80, 90))
    set_color(expected, 1, 2,  create_color(255, 0, 255))

    horizontal_image = flip_horizontal(original)
    
    for x, y, col in expected:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')', col, get_color(horizontal_image, x, y))
        
        

#Main Script
#Extreme Contrast
img = load_image(choose_file())

if __name__ == '__main__':
    
    show(extreme_contrast(img))

#Posterize
if __name__ == '__main__':

    show(posterize(img))

#Sepia    
if __name__ == '__main__':

    show(sepia(img))

#Three tone    
if __name__ == '__main__':

    show(three_tone(img,"blood","white", "lemon",))

#Draw curve            
if __name__ == '__main__':

    show(draw_curve(img,"magenta"))

#Detect edges    
if __name__ == '__main__':

    show(detect_edges(img,10))   

#Flip vertical    
if __name__ == '__main__':

    show(flip_vertical(img)) 

#Flip horizontal    
if __name__ == '__main__':

    show(flip_horizontal(img)) 

"""
#Remove docstring to test every function
test_contrast()
test_posterize()
test_sepia()
test_three_tone()
test_curve()
test_edge ()
test_flip_vertical()
test_horizontal()
"""