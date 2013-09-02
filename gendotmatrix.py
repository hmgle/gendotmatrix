#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cairo
import pango
import pangocairo
# import Image
import sys

def main():
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, 16, 16)
    context = cairo.Context(surf)
    context.rectangle(0, 0, 16, 16)
    context.set_source_rgb(1, 1, 1)
    context.fill()

    font_map = pangocairo.cairo_font_map_get_default()
    families = font_map.list_families()

    context.translate(0, 0)
    pangocairo_context = pangocairo.CairoContext(context)
    pangocairo_context.set_antialias(cairo.ANTIALIAS_SUBPIXEL)

    layout = pangocairo_context.create_layout()
    fontname = sys.argv[1] if len(sys.argv) >= 2 else "Sans"
    font = pango.FontDescription(fontname)
    layout.set_font_description(font)

    layout.set_text(u"o")
    context.set_source_rgb(0, 0, 0)
    pangocairo_context.update_layout(layout)
    pangocairo_context.show_layout(layout)

    with open("cairo_text.png", "wb") as image_file:
        surf.write_to_png(image_file)

if __name__ == '__main__':
    main()

