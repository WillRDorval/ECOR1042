from Cimpl import choose_file, load_image, copy, create_color, set_color,\
                  show, Image, get_color, create_image

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

def check_equal(description: str, outcome, expected) -> None:
    """
    Print a "passed" message if outcome and expected have same type and
    are equal (as determined by the == operator); otherwise, print a 
    "fail" message.
    
    Parameter description should provide information that will help us
    interpret the test results; e.g., the call expression that yields
    outcome.
    
    Parameters outcome and expected are typically the actual value returned
    by a call expression and the value we expect a correct implementation
    of the function to return, respectively. Both parameters must have the same
    type, which must be a type for which == is used to determine if two values
    are equal. Don't use this function to check if floats, lists of floats,
    tuples of floats, etc. are equal. 
    """    
    outcome_type = type(outcome)
    expected_type = type(expected)
    if outcome_type != expected_type:

        # The format method is explained on pages 119-122 of 
        # 'Practical Programming', 3rd ed.

        print("{0} FAILED: expected ({1}) has type {2}, " \
              "but outcome ({3}) has type {4}".
              format(description, expected, str(expected_type).strip('<class> '), 
                      outcome, str(outcome_type).strip('<class> ')))
    elif outcome != expected:
        print("{0} FAILED: expected {1}, got {2}".
              format(description, expected, outcome))
    else:
        print("{0} PASSED".format(description))
    print("------")

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

test_blue_channel()