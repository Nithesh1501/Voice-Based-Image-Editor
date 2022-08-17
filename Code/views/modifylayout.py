from tkinter import *
from PIL import ImageTk, Image
import speech_recognition as sr
from controllers.modifycontroller import modifycontroller
import time
import threading

class modifylayout:
    
    def modifyview(self):
        mc = modifycontroller()

        self.modify = Tk()
        self.modify.title('modifyview')

        self.modify.resizable(0, 0)   
        self.modify['background']='black'
        w = 900
        h = 750
        ws = self.modify.winfo_screenwidth() 
        hs = self.modify.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        self.modify.geometry('%dx%d+%d+%d' % (w, h, x, y))

        l0 = Label(self.modify,text  = "-----Modify Window-----",fg="Antiquewhite3", bg="black",font=('Times', 28))
        l0.grid(row=2, column=25, padx=260, pady=15)
        l1 = Label(self.modify,text = "1.Resize",fg="Orange", bg="black",font=('Courier', 20))
        l1.grid(row=4, column=25, padx=260, pady=10)
        l2 = Label(self.modify,text = "2.Rotate",fg="Orange", bg="black",font=("Courier", 20))
        l2.grid(row=6, column=25, padx=260, pady=10)
        l2 = Label(self.modify,text = "3.Flip",fg="Orange", bg="black",font=("Courier", 20))
        l2.grid(row=8, column=25, padx=260, pady=10)
        l3 = Label(self.modify,text = "4.Crop",fg="Orange", bg="black",font=("Courier", 20))
        l3.grid(row=10, column=25, padx=260, pady=10)
        l5 = Label(self.modify,text = "",fg="Orange", bg="black",font=("Courier", 14))
        l5.grid(row=14, column=25, padx=260, pady=10)
        l7 = Label(self.modify,text = "enter the dimensions before selcting crop function ",fg="Orange", bg="black",font=("Times", 14))
        l7.grid(row=16, column=25, padx=230, pady=10)


        var1= StringVar()
        var2= StringVar()
        var3= StringVar()
        var4= StringVar()

        mc=modifycontroller()
    
        left = Entry(self.modify, textvariable=var1,width=6,fg="black", bg="white",font=("Times", 14))
        left.grid(row=28, column=25,padx=260, pady=8)
        left.insert(0,'left')
        left.configure(state=DISABLED)
        def on_click(event):
            left.configure(state=NORMAL)
            left.delete(0, END)
        

        on_click_id = left.bind('<Button-1>', on_click)
    
        top = Entry(self.modify,textvariable=var2 ,width=6,fg="black", bg="white",font=("Times", 14))
        top.grid(row=29, column=25,padx=260, pady=8)
        top.insert(0,'top')
        top.configure(state=DISABLED)
        def on_click(event):
            top.configure(state=NORMAL)
            top.delete(0, END)
        

        on_click_id = top.bind('<Button-1>', on_click)


        right = Entry(self.modify,textvariable=var3,width=6,fg="black", bg="white",font=("Times", 14))
        right.grid(row=30, column=25,padx=260, pady=8)
        right.insert(0,'right')
        right.configure(state=DISABLED)
        def on_click(event):
            right.configure(state=NORMAL)
            right.delete(0, END)
        

        on_click_id = right.bind('<Button-1>', on_click)
    
        bottom= Entry(self.modify, textvariable=var4,width=6,fg="black", bg="white",font=("Times", 14))
        bottom.grid(row=31, column=25,padx=260, pady=8)
        bottom.insert(0,'bottom')
        bottom.configure(state=DISABLED)
        def on_click(event):
            bottom.configure(state=NORMAL)
            bottom.delete(0, END)
        

        on_click_id = bottom.bind('<Button-1>', on_click)
        
        def button2():
            r2=sr.Recognizer()
            with sr.Microphone() as source:
                print('waiting for the audio')
                try:
                    audio = r2.listen(source,phrase_time_limit=4)
                    #l5.config(text="waiting for the command")
                    text=r2.recognize_google(audio)
                    im = Image.open("image.jpg")
                    if text == 'resize':
                        a = l5.config(text="image resized")
                        t = threading.Thread(target=a,args=())
                        t.start()
                        time.sleep(4)
                        mc.resize()
                    if text =='rotate':
                        a = l5.config(text="angle:")
                        t = threading.Thread(target=a,args=())
                        t.start()
                        time.sleep(10)
                        mc.rotate()
                    if text =='flip':
                        a = l5.config(text="Image flipped")
                        t = threading.Thread(target=a,args=())
                        t.start()
                        time.sleep(4)
                        mc.flip()
                    if text == 'crop':
                        a = l5.config(text="image cropped")
                        t = threading.Thread(target=a,args=())
                        t.start()
                        print(left.get())
                        l=int(left.get())
                        t=int(top.get())
                        r=int(right.get())
                        b=int(bottom.get())
                        border=((l,t,r,b))
                        mc.crop(border)
                    if text == 'exit':
                        a = l5.config(text="redirecting back to menu")
                        t = threading.Thread(target=a,args=())
                        t.start()
                        time.sleep(4)
                        self.modify.destroy()
                                            
                except  sr.UnknownValueError:
                    l5.config(text="voice is not audible.try again")
                    print('voice is not audible')


        b1 = Button(self.modify,text="Click here to speak",fg="OrangeRed3", bg="black",bd = 5,highlightthickness=4,font=("Times", 18),command=button2)
        b1.grid(row=26, column=25, padx=12, pady=10)


