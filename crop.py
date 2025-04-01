import os
import numpy as np
import cv2

def input_image_path():
        
    img_path = os.listdir("Test")
    return img_path

print(input_image_path())
print(len(input_image_path()))