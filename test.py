from PIL import Image
from PIL import ImageFilter
import os

img = Image.open('1.png')

def preprocess_image(region):
    for y in xrange(0, region.size[1]):
        for x in xrange(0, region.size[0]):
            (r, g, b, a)=region.getpixel((x,y))
            if a < 192:
                region.putpixel((x,y),(255, 255, 255, 255))
            else:
                region.putpixel((x,y),(0, 0, 0, 255))
    region = region.resize((region.size[0]*5, region.size[1]*5))
    region = region.filter(ImageFilter.SHARPEN)
    return region

new_region = preprocess_image(img)
new_region.save('img2.tif', 'TIFF')

os.popen('tesseract  img2.tif  img2 digits')
text = file('img2.txt').read().strip()
