"""
File: curb_repair.py
Name:
-------------------------------
This program shows how to detect red pixels
of curb and change them into gray scale, making
the curb area be considered as an available parking space!
"""


from simpleimage import SimpleImage



def main():
    img = SimpleImage("images/curb.png")
    img.show()
    for pixel in img:
        avg= (pixel.red+pixel.green+pixel.blue)//3
        if pixel.red > avg * 1.05:
            pixel.red =avg
            pixel.blue=avg
            pixel.green=avg
    img.show()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
