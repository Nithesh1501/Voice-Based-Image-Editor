from PIL import Image
import pathlib

class colorcontroller:
    
    def grayscale(self):
        
        im = Image.open("image.jpg")
        print("converting to grayscale")
        gs = im.convert("L")
        gs.show()
        gs.save('grayscale.jpg')

    def bw(self):
        
        im = Image.open("image.jpg")
        print("converting to black and white")
        b = im.convert("1")
        b.show()
        b.save('blackwhite.jpg')

    
