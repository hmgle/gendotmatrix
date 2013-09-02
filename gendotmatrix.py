#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont

def main():
    image = Image.new("RGBA", (32, 16), (255, 255, 255))
    usr_font = ImageFont.truetype("/usr/share/fonts/truetype/wqy/wqy-microhei.ttc", 16)
    d_usr = ImageDraw.Draw(image)
    d_usr.text((0, 0), u"汉字", (0,0,0), font=usr_font)
    image.save("test.jpg")

if __name__ == '__main__':
    main()

