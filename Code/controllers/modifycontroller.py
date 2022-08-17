from tkinter import *
from PIL import Image,ImageOps
import speech_recognition as sr

class modifycontroller:
    
    def rotate(self):
        im = Image.open("image.jpg")
        ro=sr.Recognizer()
        print("degrees:")
        with sr.Microphone() as source:
            print('waiting for the no of degrees')
            audio=ro.listen(source)
            angle = ro.recognize_google(audio)
            r = im.rotate(int(angle))
            r.show()
            r.save('rotated.jpg')
            angle = int(angle)
            print("Image rotated  to {} ".format(angle)) 
    
    def flip(self):
        im = Image.open("image.jpg")
        print("fliping image")
        f = ImageOps.flip(im)
        f.show()
        f.save('fliped.jpg')

    def resize(self):
        im = Image.open("image.jpg")
        print(im.format, im.size)
        print("resizing image")
        re = im.resize((round(im.size[0]*.5), round(im.size[1]*.5)))
        re.show()
        re.save('resized.jpg')
        print(re.format, re.size)

    def crop(self,border):
        im = Image.open("image.jpg")
        print("cropping image")
        print("enter left, up, right, bottom")
        ci = im.crop(border)
        ci.show()
        ci.save('cropped.jpg')


