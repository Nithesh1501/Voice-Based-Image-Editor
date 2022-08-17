from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import speech_recognition as sr
import time
import threading
from views.colorlayout import colorlayout
from views.modifylayout import modifylayout
from views.AuthView import AuthView

class MyApp:

    def load(self):
         av = AuthView()
         av.transfer_control = self.mainlayout
         av.load()

    def mainlayout(self):
        cl = colorlayout()
        ml = modifylayout()
        self.main = Tk()
        self.main.title("Main View")
        self.main.resizable(0,0)   
        self.main['background']='black'
        w = 900
        h = 750
        ws = self.main.winfo_screenwidth() 
        hs = self.main.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        self.main.geometry('%dx%d+%d+%d' % (w, h, x, y))


        l0 = Label(self.main,text = "VOICE BASED IMAGE EDITOR APP",fg="Orange", bg="black",font=('Courier', 20))
        l0.grid(row=2, column=5, padx=170, pady=15)
        l1 = Label(self.main,text = "1.COLOR WINDOW",fg="Orange", bg="black",font=("Courier", 18))
        l1.grid(row=4, column=5, padx=110, pady=5)
        l2 = Label(self.main,text = "2.MODIFY WINDOW",fg="Orange", bg="black",font=("Courier", 18))
        l2.grid(row=6, column=5, padx=110, pady=5)
        r=sr.Recognizer()
        l3 = Label(self.main,text="after loading the image,click the below button\nsay color to open color view and modify to open modify view\n say logout to logout the application.",fg="Orange", bg="black",font=("Times", 12))
        l3.grid(row=14, column=5, padx=110, pady=5)
        l4 = Label(self.main,text = "Enter the image path below to load the image\nClick the button and say load.",fg="OrangeRed3", bg="black",font=('Times', 12))
        l4.grid(row=8, column=5, padx=110, pady=5)
        var1= StringVar()
        e1 = Entry(self.main,width=50,textvariable=var1).grid(row = 10,column = 5,padx=110, pady=5)

        def button():
            with sr.Microphone() as source:
                try:
                    audio=r.listen(source,phrase_time_limit=3)
                    #a=l3.config(text="waiting for the command")
                    # tc = threading.Thread(target=a,args=())
                    # tc.start()
                    text = r.recognize_google(audio)
                    if text == 'colour':
                        a = l3.config(text="Recent window opened: color window.")
                        t = threading.Thread(target=a,args=())
                        t.start()
                        cl.colorview()
                    elif text == 'modify':
                        a = l3.config(text="Recent window opened: modify window.")
                        t = threading.Thread(target=a,args=())
                        t.start()
                        ml.modifyview()
                    elif text == 'logout':
                        MsgBox = messagebox.askquestion ('Logout Application','Are you sure you want to Logout the application',icon = 'warning')
                        if MsgBox == 'yes':
                            self.main.destroy()
                            exit()
                        else:
                            messagebox.showinfo('Return','You will now return to the application screen') 
                    else:
                        raise sr.UnknownValueError

                except sr.UnknownValueError:
                    l3.config(text="voice is not audible.try again")
                    print('voice is not audible')

                    

        def button2():
            r1=sr.Recognizer()
            with sr.Microphone() as source:
                try:
                    print('waiting for the command')
                    audio = r1.listen(source,phrase_time_limit=5)
                    text  =  r1.recognize_google(audio)
                    if text=='load':
                        a = l4.config(text="uploading the image")
                        t = threading.Thread(target=a,args=())
                        t.start()
                        time.sleep(4)
                        im = Image.open((str(var1.get())))
                        print("image loaded")
                        im.save("image.jpg")
                        b = l4.config(text="image uploaded")
                        t1 = threading.Thread(target=b,args=())
                        t1.start()
                    else:
                        raise sr.UnknownValueError

                except sr.UnknownValueError:
                    l3.config(text="voice is not audible.Try again")
                    print('voice is not audible')
                
                    

        b2 = Button(self.main,text="Load the image: click here and say load.",fg="OrangeRed3", bg="black",bd = 3,highlightthickness=4,font=("Times", 14),command=button2)
        b2.grid(row=12, column=5, padx=110, pady=5)

        b = Button(self.main,text="Click this button",fg="Orange", font=("Times", 14),bg="black",bd = 3,highlightthickness=4,command=button)
        b.grid(row=16, column=5, padx=110, pady=5)

        path = "mainpic.png"
        img = ImageTk.PhotoImage(Image.open(path))
        panel = Label(self.main, image=img,width=600,height=300)
        panel.photo = img
        panel.grid(row=18, column=5, padx=160, pady=15)

app = MyApp()
app.load()