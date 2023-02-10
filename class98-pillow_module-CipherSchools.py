from PIL import Image
import os
img1 = Image.open("img1.jpg")
img1.save("img11.png")
img2 = Image.open("img11.png")
img2.show()

MAX_SIZE = (500,500) # it is used to resize the image.
img1.thumbnail(MAX_SIZE)
img1.save("img111.jpg")

for item in os.listdir():
    if item.endswith('.jpg'):
        img1 = Image.open(item)
        filename,extension = os.path.splitext(item)
        img1.save(f"{filename}.png")  # it is used to make all file with the extension .png

# now to enhance the image - sharpness,color,brightness,contrast,blur

from PIL import Image, ImageEnhance, ImageFilter

img2 = Image.open("img2.jpg")
enhancer = ImageEnhance.Sharpness(img2)
enhancer.enhance(3).save("img2edit.jpg")

img3 = Image.open("img3.jpg")
enhancer2 = ImageEnhance.Color(img3)
enhancer2.enhance(0).save("img3edit.jpg")

img4 = Image.open("img1.jpg")
enhancer3 = ImageEnhance.Brightness(img4)
enhancer3.enhance(3).save("img1edit.jpg")

# Brightness is same as Contrast.









