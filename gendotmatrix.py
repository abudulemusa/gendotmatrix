#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont

def get_pix(image):
    width, height = image.size
    print width
    print height
    for h in range(height):
        for w in range(width):
            # pix = image[w, h]
            pix = image.getpixel((w, h))
            print pix

def main():
    image = Image.new("RGB", (32, 16), (255, 255, 255))
    usr_font = ImageFont.truetype("/usr/share/fonts/truetype/wqy/wqy-microhei.ttc", 16)
    # usr_font = ImageFont.truetype("/usr/share/fonts/truetype/takao/TakaoPGothic.ttf", 25)
    d_usr = ImageDraw.Draw(image)
    d_usr.text((0, 0), u"汉字", (0,0,0), font=usr_font)
    image.save("test.jpg")
    get_pix(image)

if __name__ == '__main__':
    main()

