"""
File: img_processing_2.py
Name:
-------------------------------
This file contains 2 image processing algorithms:
(1.) left_half_darken
(2.) gray_scale
"""


from simpleimage import SimpleImage


def main():
    """
    This file contains 2 image processing algorithms:
    left_half_darken and gray_scale
    """
    #img = SimpleImage('images/stop.png')
    #img.show()

    half_dark_img = left_half_darken('images/stop.png')
    half_dark_img.show()

    gray_scale_img = gray_scale('images/stop.png')
    gray_scale_img.show()


def left_half_darken(filepath):
    """
    :param filepath: str, the file path of the original image (with respect to current directory)
    :return img: SimpleImage, the image with half horizontal area darken
    """
    darken_img= SimpleImage(filepath)
    for x in range(darken_img.width):
        for y in range(darken_img.height):
            pixel = darken_img.get_pixel(x,y)
            if x < darken_img.width//2:
                pixel.red //=2
                pixel.green//=2
                pixel.blue//=2
            if y < darken_img.height//2:
                pixel.red //=2
                pixel.green //=2
                pixel.blue //=2
    return darken_img


def gray_scale(filepath):
    """
    :param filepath: str, the file path of the original image (with respect to current directory)
    :return: SimpleImage, gray scaled image
    """
    gray_img =SimpleImage(filepath)
    for pixel in gray_img:
        avg = (pixel.red+pixel.blue+pixel.green)//3
        pixel.red=pixel.red
        pixel.blue=pixel.red
        pixel.green=pixel.red
    return gray_img


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
