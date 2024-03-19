

import cv2
import numpy as np

def sharpen_image(image_without_background):

    # تعریف کرنل شارپ کننده
    kernel_sharpening = np.array([[-1,-1,-1],
                                  [-1, 9,-1],
                                  [-1,-1,-1]])

    # اعمال کرنل بر روی تصویر
    sharpened_image = cv2.filter2D(image_without_background, -1, kernel_sharpening)

    return sharpened_image