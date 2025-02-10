import numpy as np
import cv2


def get_limits(color):
    
    c = np.uint8([[color]])
    hsv_color = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    hue = hsv_color[0][0][0]
    lower_limit = ((hue - 10) % 180, 100, 100)
    upper_limit = ((hue + 10) % 180, 255, 255)

    lower_limit = np.array(lower_limit,dtype=np.uint8)
    upper_limit = np.array(upper_limit,dtype=np.uint8)
    
    return lower_limit, upper_limit



