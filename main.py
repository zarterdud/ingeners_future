from PIL import Image


im1 = Image.open("photo1.png").convert("RGBA")
pix = im1.load()
width, height = im1.size
img = Image.new("RGBA", (1000, 500), (255, 0, 0, 255))
pixes_new = img.load()
len_width = width
while len_width > 0:
    img.paste(im1)

# img.save("test.png", "PNG")
