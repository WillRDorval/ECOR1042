"""
T099 

Code made by Mohammad Saud
"""

import typing

import numpy as np

from Cimpl import get_height, get_width, Image, set_color, create_color, load_image, choose_file, \
    show, copy, save_as


def color_names(color: str) -> tuple:
    """
    This function will take the name of a color and returns a tuple containing 
    the RGB values of that color.
    
    >>> a = color_names("grey")
    >>> print(a)
    ... (128,128,128)
    
    Made by Mohammad Saud 101195172
    """
    color_str = ("black", "white", "blood", "green", "blue", "lemon", "cyan",
                 "magenta", "gray")
    color_values = ((0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255),
                    (255, 255, 0), (0, 255, 255), (255, 0, 255), (128, 128, 128))

    for name in range(len(color_str)):
        if color == color_str[name]:
            return color_values[name]


def _regression(points: typing.List[typing.Tuple[int, int]]) -> typing.List[int]:
    """
    Finds the coefficients of the quadratic regression curve. Its argument is a 
    list of x,y and coordinate pairs. 
    
    >>>ex_points = [[2,20],[3,10],[4,30],[5,60]]
    >>>_regression(ex_points)
    ...[10.0,-56.0,91.0]
    
    >>>ex_points = [[1,1],[2,5],[3,8],[4,3]]
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


def _interpolation(point_set: typing.List[typing.Tuple[int, int]]) -> typing.List[int]:
    """
    Find the linear interpolation fitting coefficients or quadratic fitting 
    coefficients, depending on the number of points given. 
    
    >>>points = [[2,30],[30,100]]
    >>>_interpolation(points)
    ...[2.5,25]
    
    >>>points = [[2,10],[20,30],[120,60]
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


def _image_border_finding(size: typing.Tuple[int, int], coeffs: typing.List[float]) -> \
    typing.List[typing.Tuple[int, int]]:
    """
    Finds the points where a certain cruve will intersect the border.
    
    >>>_image_border_finding((image_width, image_height), coefficients)
    
    Made by William Dorval
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
        if (y_val > size[1] or y_val < 0) and drawing:
            x_intercepts.append((x - 1, previous))
            drawing = False
        elif (size[1] > y_val > 0) and not drawing:
            x_intercepts.append((x, y_val))
            drawing = True
        previous = y_val

    results = []
    for pt in x_intercepts:
        results.append(pt)

    results.sort(key=lambda point: point[0])

    return results


def draw_curve(img: Image, color: str) -> Image:
    """
    Takes an image and a color as its arguments. The function then asks for a 
    number of points and draws a curve on the image using the specified color.
    
    >>>img = load_image(choose_file())
    >>>show(draw_curve(img, "magenta"))
    
    Made by Mohammad Saud 101195172
    Reviewed and improved by William Dorval
    """

    curve_image = copy(img)

    r1, g1, b1 = color_names(color)
    pix_color = create_color(r1, g1, b1)

    all_points = []
    point_num = 0
    while True:
        point_num = int(input("How many points would you like to enter? "))
        if point_num < 2:
            print("There must be atleast 2 points")
        else:
            break

    curve_image_height = get_height(curve_image)
    curve_image_width = get_width(curve_image)

    print("The image maximum x value is " + str(curve_image_width))
    print("The image maximum y value is " + str(curve_image_height))

    for i in range(1, point_num + 1):
        point = []
        x_cor = int(input("Please input x coordinate for point " + str(i) + ": "))
        y_cor = int(input("Please input y coordinate for point " + str(i) + ": "))
        point = (x_cor, y_cor)
        all_points.append(point)

    all_points.sort()

    if point_num <= 3:
        coeff = _interpolation(all_points)
    else:
        coeff = _regression(all_points)

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
                if 0 <= y_pnt+i < curve_image_height:
                    set_color(curve_image, x, y_pnt+i, pix_color)

        if drawing and direction != 0:
            for i in range(y_pnt+direction, previous-direction, direction):
                if 0 <= i < curve_image_height:
                    set_color(curve_image, x, i, pix_color)

        if leaving:
            y = y_pnt - (2*direction)
            while 0 <= y < curve_image_height:
                set_color(curve_image, x+1, y, pix_color)
                y -= direction
            drawing = False

        if (x, y_pnt) in border_points:
            border_points.remove((x, y_pnt))
            drawing = not drawing

        previous = y_pnt
        leaving = False

    return curve_image


if __name__ == '__main__':
    img = load_image(choose_file())
    new_img = draw_curve(img, "magenta")
    show(new_img)
    save_as(new_img)
