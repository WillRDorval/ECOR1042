"""
T099 

Code made by Mohammad Saud
"""

from Cimpl import get_height, get_width, Image, create_image, get_color, Color,\
                  set_color, create_color, save_as, load_image, choose_file, show, copy
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
    color_str = ("black","white","blood","green","blue","lemon","cyan","magenta","gray")
    color_values = ((0,0,0),(255,255,255),(255,0,0),(0,255,0),(0,0,255),(255,255,0),(0,255,255),(255,0,255),(128,128,128))
    
    for name in range(len(color_str)):
        if color == color_str[name]:
            return color_values[name]
        
        

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
        
def draw_curve(img: Image, color: str) -> Image:
    
    
    all_points = []
    point_num = int(input("How many points would you like to enter? "))
    for i in range(1, point_num+1):
        point = []
        x_cor = int(input(" Please input x coordinate for point " + str(i) + ": "))
        y_cor = int(input(" Please input y coordinate for point " + str(i) + ": "))
        point = [x_cor,y_cor]
        all_points.append(point)

    all_points.sort()

        
        
        
