from PIL import Image
import numpy as np


def edit_photo(photo):
    im1 = Image.open(photo).convert("RGBA")
    pixes = im1.load()
    width, height = im1.size
    pixes_new = [[(255, 255, 255, 0)] * width for i in range(height)]
    for i in range(height):
        for j in range(width):
            r, g, b, a = pixes[j, i]
            if a > 250:
                pixes_new[i][j] = (r, g, b, a)

    height_top = 0
    height_bot = height
    width_top = 0
    width_bot = width

    for i in range(height - 1):
        empty = True
        for j in range(width - 1):
            r, g, b, a = pixes[j, i]
            if r < 100 and g < 100 and b < 100:
                empty = False
        if empty:
            height_top += 1
        else:
            break

    for i in range(height - 1, 0, -1):
        empty = True
        for j in range(width - 1, 0, -1):
            r, g, b, a = pixes[j, i]
            if r < 100 and g < 100 and b < 100:
                empty = False
        if empty:
            height_bot -= 1
        else:
            break

    for i in range(width - 1):
        empty = True
        for j in range(height - 1):
            r, g, b, a = pixes[i, j]
            if r < 100 and g < 100 and b < 100:
                empty = False
        if empty:
            width_top += 1
        else:
            break

    for i in range(width - 1, 0, -1):
        empty = True
        for j in range(height - 1, 0, -1):
            r, g, b, a = pixes[i, j]
            if r < 100 and g < 100 and b < 100:
                empty = False
        if empty:
            width_bot -= 1
        else:
            break

    array = np.array(pixes_new, dtype=np.uint8)
    new_image = Image.fromarray(array)
    new_image = new_image.crop((width_top, height_top, width_bot, height_bot))
    new_image.save("test.png", "PNG")
    return new_image
