"""
Submission by T099

William Dorval 101187466
Raunaq Hoqie 101180524
Chaelan Murray 101180990
Mohammad Saud 101195172

Submitted on: 2021-02-07
"""

import typing

import numpy as np

from Cimpl import get_height, get_width, Image, set_color, create_color, load_image, choose_file, \
    show, copy, get_color


# Extreme Contrast
def extreme_contrast(input_image: Image) -> Image:
    """ Returns a copy of an image with the contrast between the pixels being maximized. 
    >>> original_image = load_image(choose_file())
    >>> extreme_image = extreme_contrast(original_image)
    >>> show(extreme_image)
    By Chaelan Murray 101180990
    """
    new_image = copy(input_image)
    for x, y, (r, g, b) in input_image:
        col = [r, g, b]
        for t in range(3):
            if col[t] >= 128:
                col[t] = 255
            else:
                col[t] = 0
        extreme = create_color(*col)
        set_color(new_image, x, y, extreme)
    return new_image


# Color Names
def color_names(color: str) -> tuple:
    """
    This function will take the name of a color and returns a tuple containing 
    the RGB values of that color.
    
    >>> a = color_names("grey")
    >>> print(a)
    ... (128,128,128)
    
    Made by Mohammad Saud 101195172
    """
    color_str = ("black", "white", "blood", "green", "blue", "lemon", "cyan", "magenta", "gray")
    color_values = (
        (0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255),
        (128, 128, 128))

    for name in range(len(color_str)):
        if color == color_str[name]:
            return color_values[name]


# Three tone filter
def three_tone(org_img: Image, tone_1: str, tone_2: str, tone_3: str) -> Image:
    """
    This function will convert an image to a three tone image. The 3 tones will 
    be specified as their correct color names in lowercase.
    
    >>> input_image = load_image(choose_file())
    >>> new = three_tone(input_image, "black", "blood", "white")
    >>> show(new)
    
    Made by Mohammad Saud 101195172
    """

    r1, g1, b1 = color_names(tone_1)
    r2, g2, b2 = color_names(tone_2)
    r3, g3, b3 = color_names(tone_3)

    three_tone_image = copy(org_img)

    for x, y, (r, g, b) in three_tone_image:

        brightness = ((r + g + b) / 3)

        if brightness <= 84:
            pix_color = create_color(r1, g1, b1)
            set_color(three_tone_image, x, y, pix_color)
        elif (brightness >= 85) and (brightness <= 170):
            pix_color = create_color(r2, g2, b2)
            set_color(three_tone_image, x, y, pix_color)
        elif (brightness >= 171) and (brightness <= 255):
            pix_color = create_color(r3, g3, b3)
            set_color(three_tone_image, x, y, pix_color)

    return three_tone_image


# Helper function for posterize
def _adjust_component(r, g, b):
    """Return the midpoint of the rgb component from the 4 quadrants 
    (0..63, 64..127, 128..191, and 192..255).
    >>> _adjust_component (60, 120, 190) 
    >>> (31, 95, 159)
    By Raunaq Hoque 101180524
    """
    pixel_color = [r, g, b]
    for i in range(3):
        if pixel_color[i] <= 63:
            pixel_color[i] = 31
        elif pixel_color[i] <= 127:
            pixel_color[i] = 95
        elif pixel_color[i] <= 191:
            pixel_color[i] = 159
        elif pixel_color[i] <= 255:
            pixel_color[i] = 223
        pixel = create_color(*pixel_color)
    return pixel


# Posterize
def posterize(input_image: Image) -> Image:
    """Return the posterized copy of image.
    >>> loaded_image = load_image(choose_file())
    >>> posterize_image=posterize(loaded_image)
    >>> show(posterize_image)
    By Raunaq Hoque 101180524
    """
    new_image = copy(input_image)
    for x, y, (r, g, b) in input_image:
        color = _adjust_component(r, g, b)
        set_color(new_image, x, y, color)
    return new_image


# Sepia filter
def sepia(input_image: Image) -> Image:
    """
    Returns a sepia tone copy of the image
    >>> loaded_image = load_image(choose_file())
    >>> sepia_image = sepia(loaded_image)
    >>> show(sepia_image)

    By William Dorval 101187466
    """
    new_image = copy(grayscale(input_image))
    for x, y, (r, g, b) in new_image:
        if r < 63:
            set_color(new_image, x, y, create_color(1.1 * r, g, 0.9 * b))
        elif r <= 191:
            set_color(new_image, x, y, create_color(1.15 * r, g, 0.85 * b))
        else:
            set_color(new_image, x, y, create_color(1.08 * r, g, 0.93 * b))
    return new_image


# Helper function for draw_curve
def _regression(points: typing.List[typing.Tuple[int, int]]) -> typing.List[int]:
    """
    Finds the coefficients of the quadratic regression curve. Its argument is a 
    list of x,y and coordinate pairs. 
    
    >>>ex_points = [(2,20),(3,10),(4,30),(5,60)]
    >>>_regression(ex_points)
    ...[10.0,-56.0,91.0]
    
    >>>ex_points = [(1,1),(2,5),(3,8),(4,3)]
    >>>_regression(ex_points)
    ...[-2.25,12.15,-9.25]
    
    Made by Mohammad Saud 101195172
    Reviewed and improved by William Dorval
    """
    degree = 2
    x_sums = []
    for i in range(degree * 2 + 1):
        x_sums.append(sum(pt[0] ** i for pt in points))
    y_sums = []
    for i in range(degree + 1):
        y_sums.append(sum((pt[0] ** i) * pt[1] for pt in points))
    a = []
    for i in range(degree + 1):
        line = []
        for j in range(degree + 1):
            line.append(x_sums[-1 - (i + j)])
        a.append(line)
    b = []
    for i in range(degree + 1):
        b.append(y_sums[-1 - i])
    print(a)
    print(b)

    a_np = np.array(a)
    b_np = np.array(b)
    x = np.linalg.solve(a_np, b_np)

    coeff_list = []
    for i in x:
        coeff_list.append(i)
    return coeff_list


# Helper function for draw_curve
def _interpolation(point_set: typing.List[typing.Tuple[int, int]]) -> typing.List[float]:
    """
    Find the linear interpolation fitting coefficients or quadratic fitting 
    coefficients, depending on the number of points given. 
    
    >>>points = [(2,30),(30,100)]
    >>>_interpolation(points)
    ...[2.5,25]
    
    >>>points = [(2,10),(20,30),(120,60)]
    >>>_interpolation(points)
    ...[-0.0068738229755178895, 1.2623352165725046, 7.502824858757061]
    
    Made by Mohammad Saud 101195172
    """
    if len(point_set) == 2:  # Linear Interpolation
        y2 = (point_set[1])[1]
        y1 = (point_set[0])[1]
        x2 = (point_set[1])[0]
        x1 = (point_set[0])[0]
        a = ((y2 - y1) / (x2 - x1))
        b = (y2 - (x2 * a))
        return [a, b]

    elif len(point_set) == 3:  # Quadratic interpolation
        x1_1 = ((point_set[0])[0]) ** 2
        x2_1 = ((point_set[1])[0]) ** 2
        x3_1 = ((point_set[2])[0]) ** 2
        x1_2 = ((point_set[0])[0])
        x2_2 = ((point_set[1])[0])
        x3_2 = ((point_set[2])[0])
        y1 = ((point_set[0])[1])
        y2 = ((point_set[1])[1])
        y3 = ((point_set[2])[1])

        a = np.array([[x1_1, x1_2, 1], [x2_1, x2_2, 1], [x3_1, x3_2, 1]])
        b = np.array([y1, y2, y3])
        x = np.linalg.solve(a, b)
        coeff_list = []
        for i in x:
            coeff_list.append(i)
        return coeff_list

    else:
        pass


# Helper function for draw_curve
def _image_border_finding(size: typing.Tuple[int, int], coeffs: typing.List[float]) -> \
        typing.List[typing.Tuple[int, int]]:
    """
    Returns a list of x,y coordinate pairs in tuples that cross the border of 
    the images given the coefficients of the curve.
    
    Made by William Dorval 101187466
    """
    degrees = []
    for i in range(len(coeffs) - 1, -1, -1):
        degrees.append(i)

    x_intercepts = []
    drawing = False
    for x in range(size[0]):
        y_val = 0
        for j in range(len(coeffs)):
            y_val += (x ** degrees[j]) * coeffs[j]

        y_val = int(y_val)
        if (y_val > size[1] or y_val <= 0) and drawing:
            x_intercepts.append((x - 1, previous))
            drawing = False
        elif (size[1] > y_val >= 0) and not drawing:
            x_intercepts.append((x, y_val))
            drawing = True
        previous = y_val

    results = []
    for pt in x_intercepts:
        results.append(pt)

    results.sort(key=lambda point: point[0])

    return results


# Draw_curve filter
def draw_curve(img: Image, color: str, points: typing.List[typing.Tuple[int, int]] = None) -> Image:
    """
    Takes an image and a color as its arguments. The function then asks for a 
    number of points and draws a curve on the image using the specified color.
    
    >>>loaded_image = load_image(choose_file())
    >>>show(draw_curve(loaded_image, "magenta"))
    
    Made by Mohammad Saud 101195172
    Reviewed and improved by William Dorval 101187466
    """

    curve_image = copy(img)

    r1, g1, b1 = color_names(color)
    pix_color = create_color(r1, g1, b1)

    all_points = []
    curve_image_height = get_height(curve_image)
    curve_image_width = get_width(curve_image)
    if points is None:
        while True:
            point_num = int(input("How many points would you like to enter? "))
            if point_num < 2:
                print("There must be atleast 2 points")
            else:
                break

        print("The image maximum x value is " + str(curve_image_width))
        print("The image maximum y value is " + str(curve_image_height))

        for i in range(1, point_num + 1):
            x_cor = int(input("Please input x coordinate for point " + str(i) + ": "))
            y_cor = int(input("Please input y coordinate for point " + str(i) + ": "))
            point = (x_cor, y_cor)
            all_points.append(point)
    else:
        all_points = points
        point_num = len(points)

    all_points.sort()

    if point_num <= 3:
        coeff = _interpolation(all_points)
    else:
        coeff = _regression(all_points)

    print(coeff)
    border_points = _image_border_finding((curve_image_width, curve_image_height), coeff)
    print(border_points)

    drawing = False
    leaving = False
    if point_num == 2:
        previous = int(((-1) * (coeff[0])) + coeff[1])
    else:
        previous = int((((-1) ** 2) * coeff[0]) + ((-1) * (coeff[1])) + coeff[2])
    for x in range(curve_image_width):

        if point_num == 2:
            y_pnt = int((x * (coeff[0])) + coeff[1])
        else:
            y_pnt = int(((x ** 2) * coeff[0]) + (x * (coeff[1])) + coeff[2])

        try:
            direction = int((previous - y_pnt) / abs(previous - y_pnt))
        except ZeroDivisionError:
            direction = 0

        if (x, y_pnt) in border_points:
            border_points.remove((x, y_pnt))
            leaving = drawing
            drawing = True

        if drawing:
            for i in range(-2, 3):
                if 0 <= y_pnt + i < curve_image_height:
                    set_color(curve_image, x, y_pnt + i, pix_color)

        if drawing and direction != 0:
            for i in range(y_pnt + direction, previous - direction, direction):
                if 0 <= i < curve_image_height:
                    set_color(curve_image, x, i, pix_color)

        if leaving:
            y = y_pnt - (2 * direction)
            while 0 <= y < curve_image_height:
                set_color(curve_image, x + 1, y, pix_color)
                y -= direction
            drawing = False

        if (x, y_pnt) in border_points:
            border_points.remove((x, y_pnt))
            drawing = not drawing

        previous = y_pnt
        leaving = False

    return curve_image


# Helper function for detect_edges
def grayscale(input_image: Image) -> Image:
    result = copy(input_image)
    for x, y, (r, g, b) in input_image:
        gray = (r + g + b) / 3
        result.set_color(x, y, create_color(gray, gray, gray))

    return result


# Detect edges filter
def detect_edges(input_image: Image, threshold: int) -> Image:
    """
    Creates a new image with black on the edges and white everywhere else
    >>> loaded_image = load_image(choose_file())
    >>> edge_image = detect_edges(loaded_image, 20)
    >>> show(edge_image)

    Made by William Dorval 101187466
    """
    brightness = grayscale(input_image)
    result = Image(width=input_image.get_width(), height=input_image.get_height())
    for x, y, (r, _, _) in brightness:
        if abs(r - brightness.get_color(x, y - 1)[0]) > threshold:
            result.set_color(x, y, create_color(0, 0, 0))

    return result


# Flip_horizontal filter
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


# Flip_vertical filter
def flip_vertical(image: Image) -> Image:
    """  Returns a copy of the image, flipped along the middle horizontal line.
    >>> original_image = load_image(choose_file())
    >>> extreme_image = flip_vertical(original_image)
    >>> show(flip_vertical)

    By Chaelan Murray 101180990
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
