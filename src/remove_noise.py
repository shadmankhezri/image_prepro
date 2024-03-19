
import cv2
import numpy as np

def denoise_image(image_path):
    """
    این تابع نویز را از تصویر با استفاده از فیلتر گاوسین حذف می‌کند.

    Args:
        image_path: مسیر تصویر ورودی

    Returns:
        تصویر بدون نویز
    """
    image = cv2.imread(image_path , cv2.IMREAD_UNCHANGED)
    denoised_image = cv2.GaussianBlur(image, (5, 5), 0)
    return denoised_image



