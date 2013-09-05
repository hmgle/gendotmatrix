#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
from bitarray import bitarray

def get_pix(image):
    pixel = image.load()
    width, height = image.size
    print width
    print height
    bitmap = bitarray()
    for h in range(height):
        for w in range(width):
            if int(sum(pixel[w, h])) > (255 * 3 / 2):
                bitmap.append(False)
            else:
                bitmap.append(True)
            # pix = image.getpixel((w, h))
            # print pix
    print bitmap

def main():
    image = Image.new("RGB", (16, 16), (255, 255, 255))
    usr_font = ImageFont.truetype("/usr/share/fonts/truetype/wqy/wqy-microhei.ttc", 16)
    # usr_font = ImageFont.truetype("/usr/share/fonts/truetype/takao/TakaoPGothic.ttf", 25)
    d_usr = ImageDraw.Draw(image)
    d_usr.text((0, 0), u"字", (0,0,0), font=usr_font)
    get_pix(image)
    image.save("test.jpg")

if __name__ == '__main__':
    main()
