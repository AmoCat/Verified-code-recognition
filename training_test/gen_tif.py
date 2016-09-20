from PIL import Image
from PIL import ImageFilter
import os

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

for i in range(1,10):
    file_name = str(i)+'.png'
    img = Image.open(file_name)
    new_region = preprocess_image(img)
    tif_name = str(i)+'.tif'
    new_region.save(tif_name, 'TIFF')
    os.popen('tesseract  '+tif_name+' '+str(i)+' digits')
