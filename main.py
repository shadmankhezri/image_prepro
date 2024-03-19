
import cv2

from src.remove_noise import denoise_image
from src.remove_background import remove_background
from src.sharpening import sharpen_image



def main():
    # مسیر تصویر
    image_path = "image/noisy_image.png"

    # حذف نویز از تصویر
    denoised_image = denoise_image(image_path)

    # ذخیره تصویر بدون نویز
    cv2.imwrite("image/denoised_image.png", denoised_image)



    # مسیر تصویر بدون نویز
    denoised_image_path = "image/denoised_image.png"

    # خواندن تصویر بدون نویز
    denoised_image = cv2.imread(denoised_image_path)

    # حذف بک‌گراند از تصویر
    image_without_background = remove_background(denoised_image)

    # ذخیره تصویر بدون بک‌گراند
    cv2.imwrite("image/image_without_background.png", image_without_background)



    # شارپ کردن تصویر بدون بک‌گراند
    sharpened_image = sharpen_image(image_without_background)

    # ذخیره تصویر شارپ شده
    cv2.imwrite("image/sharpen_image.jpg", sharpened_image)


if __name__ == "__main__":
    main()


