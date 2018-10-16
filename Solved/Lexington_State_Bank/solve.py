#!/usr/bin/env python3
from PIL import Image

image_filename = '664afe59e115a10214ee14b11dd4c39bb07a361cdb5df1791a4553d4eb9bcca8_LexingtonStateBank.png'
im = Image.open(image_filename)
im = im.convert('RGBA')
width, height = im.size

flag = ''
for y in range(height):
    for x in range(width):
        r, g, b, a = im.getpixel((x, y))
        flag += str(r & 1)
        flag += str(g & 1)
        flag += str(b & 1)
        flag += str(a & 1)
        # if a != 255: print(str(x).zfill(2), str(y).zfill(2), hex(a), bin(a))

size = 8
chars = [chr(int(flag[i:i+size], 2)) for i in range(0, len(flag), size)]
print("".join(chars))
