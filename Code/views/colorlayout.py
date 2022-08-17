from tkinter import *
import speech_recognition as sr
from controllers.colorcontroller import colorcontroller
from PIL import Image

class colorlayout:

    def colorview(self):
        cc = colorcontroller()
        self.color = Tk()
        self.color.title('colorview')

        self.color.resizable(0, 0)   
        self.color['background']='black'
        w = 900
        h = 750
        ws = self.color.winfo_screenwidth() 
        hs = self.color.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        self.color.geometry('%dx%d+%d+%d' % (w, h, x, y))

        l0 = Label(self.color,text = "-----Color Window-----",fg="Antiquewhite3", bg="black",font=('Times', 28))
        l0.grid(row=2, column=25, padx=240, pady=15)
        l1 = Label(self.color,text = "1.Black and White",fg="Orange", bg="black",font=('Courier', 20))
        l1.grid(row=4, column=25, padx=240, pady=5)
        l2 = Label(self.color,text = "2.Grayscale",fg="Orange", bg="black",font=('Courier', 20))
        l2.grid(row=6, column=25, padx=240, pady=5)
        l3 = Label(self.color,text="",fg="Orange", bg="black",font=("Times", 12))
        l3.grid(row=8, column=25, padx=240, pady=5)
        l5 = Label(self.color,text = "",fg="Orange", bg="black",font=("Courier", 10))
        l5.grid(row=14, column=25, padx=260, pady=10)
    
        def button1():
                r1=sr.Recognizer()
                with sr.Microphone() as source:
                    try:
                        print('waiting for the audio')
                        audio = r1.listen(source,phrase_time_limit=4)
                        l3.config(text="waiting for the command")
                        text  =  r1.recognize_google(audio)
                        if text=='black and white':
                            l5.config(text="Image converted to black and white")
                            print("You said black and white")
                            cc.bw()
                        if text =='grayscale':
                            l5.config(text="Image converted to grayscale")
                            print("choosed grayscale")
                            cc.grayscale()
                        if text == 'exit':
                            self.color.destroy()
                             
                    except sr.UnknownValueError:
                        l3.config(text="voice is not audible.try again")
                        print('voice is not audible')
                        


        b1 = Button(self.color,text="Optimise the image: Click here to speak",fg="OrangeRed3", bg="black",bd = 5,highlightthickness=4,font=("Times", 18),command=button1)
        b1.grid(row=18, column=25, padx=240, pady=25)


