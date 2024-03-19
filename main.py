
import cv2

from src.remove_noise import denoise_image
from src.remove_background import remove_background




def main():
    # مسیر تصویر
    image_path = "image/noisy_image.png"

    # حذف نویز از تصویر
    denoised_image = denoise_image(image_path)

    # ذخیره تصویر بدون نویز
    cv2.imwrite("image/denoised_image.png", denoised_image)


    # مسیر تصویر چهار کاناله
    four_channel_image_path = "image/denoised_image.png"

    # حذف بک‌گراند از تصویر چهار کاناله
    rgb_image = remove_background(four_channel_image_path)

    # ذخیره تصویر بدون کانال چهارم (بک‌گراند) در فایل min.py
    cv2.imwrite("image/remove_background.png", rgb_image)


if __name__ == "__main__":
    main()


