#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import bitarray
from bitarray import bitarray
import getopt
import sys
import re

def get_pix(image):
    pixel = image.load()
    width, height = image.size
    bitmap = bitarray()
    for h in range(height):
        for w in range(width):
            # if int(sum(pixel[w, h])) > (255 * 3 / 2):
            if pixel[w, h] > 0:
                bitmap.append(False)
            else:
                bitmap.append(True)
    return bitmap

def get_gb2312_pix(gb2312_code, w, h, usr_font):
    # image = Image.new("RGB", (w, h), (255, 255, 255))
    image = Image.new("1", (w, h), (1))
    d_usr = ImageDraw.Draw(image)
    try:
        unicode_code = gb2312_code.decode('gb2312')
        # d_usr.text((0, 0), unicode_code, (0,0,0), font=usr_font)
        d_usr.text((0, 0), unicode_code, (0), font=usr_font)
    except:
        # d_usr.text((0, 0), u" ", (0,0,0), font=usr_font)
        d_usr.text((0, 0), u" ", (0), font=usr_font)
    return get_pix(image)

def main():
    help = 'Usage: %s [option] <truetype-file>' % sys.argv[0]
    help += '''\noption:
    -h | --help                                 display this information
    -s | --size geometry                        width and height of font
    -o | --output output-dot-matrix-font        specify output file
example:
    gendotmatrix.py -s 16x16 -o ubuntu-c.font "/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-C.ttf"
    '''
    short_opts = 'hi:s:o:'
    opts = ['help', 'size=', 'output=']
    try:
        opts, args = getopt.getopt(sys.argv[1:], short_opts, opts)
    except getopt.GetoptError as err:
        print(err)
        print(help)
        sys.exit(1)

    font_width = 16
    font_height = 16
    outfilename = 'dot_matrix.font'
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print(help)
            sys.exit()
        elif opt in ('-s', '--size'):
            fontsize = re.split(r'\D', arg)
            font_width = int(fontsize[0])
            font_height = int(fontsize[1])
        elif opt in ('-o', '--output'):
            outfilename = arg
        else:
            print(help)
            sys.exit(1)

    if len(args) > 0:
        truetypefile = args[0]
    else:
        print(help)
        sys.exit(1)
    usr_font = ImageFont.truetype(truetypefile, font_height)
    with open(outfilename, 'wb') as outfile:
        for i in range(0xA1, 0xF8):
            for j in range(0xA1, 0xFF):
                data = get_gb2312_pix(chr(i) + chr(j), font_width, font_height, usr_font)
                data.tofile(outfile)

if __name__ == '__main__':
    main()
