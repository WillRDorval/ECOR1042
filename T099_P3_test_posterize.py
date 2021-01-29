



def test_posterize() -> None:
    """ Test the green_channel function.
    >>> test_green_channel()
    """
    original = create_image(5, 1) 
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(0, 128, 0))
    set_color(original, 2, 0,  create_color(127, 0, 127))
    set_color(original, 3, 0,  create_color(125, 22, 224))
    set_color(original, 4, 0,  create_color(255, 255, 255)) 
  
    expected = create_image(5, 1) 
    set_color(expected, 0, 0,  create_color(31, 31, 31))
    set_color(expected, 1, 0,  create_color(31, 159, 0))
    set_color(expected, 2, 0,  create_color(95, 0, 95))
    set_color(expected, 3, 0,  create_color(95, 31, 223))
    set_color(expected, 4, 0,  create_color(223, 223, 223)) 
  
    post_test_image = posterize(original)
    
    for x, y, col in green_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')', col, get_color(expected, x, y))