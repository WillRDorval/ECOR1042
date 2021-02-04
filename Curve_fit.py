"""
T099 

Code made by Mohammad Saud
"""

from Cimpl import get_height, get_width, Image, create_image, get_color, Color,\
                  set_color, create_color, save_as, load_image, choose_file, \
                  show, copy
from unit_testing import check_equal
import numpy as np 

def color_names(color: str) -> tuple:
    """
    This function will take the name of a color and returns a tuple containing 
    the RGB values of that color.
    
    >>> a = color_names("grey")
    >>> print(a)
    ... (128,128,128)
    
    Made by Mohammad Saud 101195172
    """
    color_str = ("black","white","blood","green","blue","lemon","cyan",\
                 "magenta","gray")
    color_values = ((0,0,0),(255,255,255),(255,0,0),(0,255,0),(0,0,255),\
                    (255,255,0),(0,255,255),(255,0,255),(128,128,128))
    
    for name in range(len(color_str)):
        if color == color_str[name]:
            return color_values[name]

def _regression(points: list) -> list:
    degree = 2
    x_sums = []
    for i in range(degree*2 + 1):
        x_sums.append(sum(pt[0]**i for pt in points))
    y_sums = []
    for i in range(degree+1):
        y_sums.append(sum((pt[0]**i) * pt[1] for pt in points))
    a = []
    for i in range(degree+1):
        line = []
        for j in range(degree+1):
            line.append(x_sums[-1 - (i+j)])
        a.append(line)
    b = []
    for i in range(degree+1):
        b.append(y_sums[-1 - i])
    print(a)
    print(b)

    a_np = np.array(a)
    b_np = np.array(b)
    x = np.linalg.solve(a, b)

    for i in x:
            coeff_list.append(i)
    return coeff_list
        

def _interpolation(point_set: list) -> list:
    
    if len(point_set) == 2: #Linear Interpolation
        y2 = (point_set[1])[1]
        y1 = (point_set[0])[1]
        x2 = (point_set[1])[0]
        x1 = (point_set[0])[0]
        a = ((y2-y1)/(x2-x1))
        b = (y2-(x2*a))
        return [a,b]
    
    elif len(point_set) == 3: #Quadratic interpolation
        x1_1 = ((point_set[0])[0])**2
        x2_1 = ((point_set[1])[0])**2
        x3_1 = ((point_set[2])[0])**2
        x1_2 = ((point_set[0])[0])
        x2_2 = ((point_set[1])[0])
        x3_2 = ((point_set[2])[0])
        y1 = ((point_set[0])[1])
        y2 = ((point_set[1])[1])
        y3 = ((point_set[2])[1])
        
        a = np.array([[x1_1,x1_2,1], [x2_1,x2_2,1], [x3_1,x3_2,1]])
        b = np.array([y1,y2,y3])
        x = np.linalg.solve(a,b)
        coeff_list = []
        for i in x:
            coeff_list.append(i)
        return coeff_list
    
    else:
        pass
        
def draw_curve(img: Image, color: str) -> Image:
    
    
    curve_image = copy(img)
    
    
    r1,g1,b1 = color_names(color)
    pix_color = create_color(r1,g1,b1)
    
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

    for i in range(1, point_num+1):
        point = []
        x_cor = int(input("Please input x coordinate for point " +str(i) +": "))
        y_cor = int(input("Please input y coordinate for point " +str(i) +": "))
        point = [x_cor,y_cor]
        all_points.append(point)

    all_points.sort()
    
    if len(all_points) <= 3:
        coeff = _interpolation(all_points)
    else:
        coeff = _regression(all_points)
    
    for x, y, (r,g,b) in curve_image:
        
        x1 = x + 1
        if len(all_points) == 2:
            y_pnt = ((x)*(coeff[0])) + coeff[1]
        else:
            y_pnt = (((x)**2)*coeff[0]) + ((x)*(coeff[1])) + coeff[2]
        
       
        
        if (y_pnt > 0) and (y_pnt < curve_image_height):
            set_color(curve_image, x, y_pnt, pix_color)
        else: 
            pass
        if ((x-1) >= 0) and ((y_pnt-1) >= 0):
            set_color(curve_image, (x-1), (y_pnt-1), pix_color)
        else: 
            pass
        if (x-2 >= 0) and (y_pnt-2 >= 0):
            set_color(curve_image, x-2, y_pnt-2, pix_color)
        else: 
            pass        
        if (x+1 < curve_image_width) and (y_pnt + 1 < curve_image_height):
            set_color(curve_image, x+1, y_pnt+1, pix_color)
        else: 
            pass 
        if (x+2 < curve_image_width) and (y_pnt + 2 < curve_image_height):
            set_color(curve_image, x+2, y_pnt+2, pix_color)
        else: 
            pass         
        
    return curve_image


img = load_image(choose_file())
show(draw_curve(img, "magenta"))
