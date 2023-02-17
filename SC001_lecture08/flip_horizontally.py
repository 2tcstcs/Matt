"""
File: flip_horizontally.py
Name: 
------------------------------------
This program shows how to create an empty SimpleImage
as well as making a mirrored image of poppy.png by
replacing pixels on blank new canvas by ones on poppy.png
"""


from simpleimage import SimpleImage


def main():
    img = SimpleImage("images/poppy.png")
    img.show()
    b_img = SimpleImage.blank(img.width*2,img.height)
    b_img.show()

    for x in range(img.width):
        for y in range(img.height):
            img_p=img.get_pixel(x,y)
            b_img_p1 = b_img.get_pixel(x,y)

            b_img_p1.red = img_p.red
            b_img_p1.blue = img_p.blue
            b_img_p1.green = img_p.green

            b_img_p2 = b_img.get_pixel(b_img.width-1-x, y)
            b_img_p2.red = img_p.red
            b_img_p2.blue = img_p.blue
            b_img_p2.green = img_p.green
    b_img.show()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
