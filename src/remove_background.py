

import cv2
import numpy as np

def remove_background(denoised_image):


    # تبدیل تصویر به فضای رنگی HSV
    hsv = cv2.cvtColor(denoised_image, cv2.COLOR_BGR2HSV)

    # تعریف ماسک برای استفاده در GrabCut
    mask = np.zeros(denoised_image.shape[:2], np.uint8)

    # تنظیم پارامترهای GrabCut
    bgd_model = np.zeros((1, 65), np.float64)
    fgd_model = np.zeros((1, 65), np.float64)
    rect = (50, 50, denoised_image.shape[1] - 100, denoised_image.shape[0] - 100)

    # اعمال GrabCut
    cv2.grabCut(hsv, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)

    # استخراج ماسک پیش‌زمینه
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

    # اعمال ماسک به تصویر
    image_without_background = denoised_image * mask2[:, :, np.newaxis]

    return image_without_background