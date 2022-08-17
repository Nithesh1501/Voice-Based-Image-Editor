from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import os
from tkinter import messagebox 
from controllers.AuthController import AuthController

class AuthView:

    next  = None
    def load(self):
        self.window = Tk()
        self.window.resizable(0,0)
        self.window['background']='black'
        w = 900
        h = 750
        ws = self.window.winfo_screenwidth() 
        hs = self.window.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        black = "#000000"
        orange = "#FFA500"
        self.window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.style = ttk.Style()
        self.style.theme_create( "MyStyle", parent="alt", settings={"TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] },},"TNotebook.Tab": {"configure": {"padding": [10, 10],"background":black,"foreground":orange },}})
        self.style.theme_use("MyStyle")
        self.window.overrideredirect(True)
        self.window.title("Authorisation")
        tab_control = ttk.Notebook(self.window,width=900, height=750)
        ttk.Style().configure("TNotebook", background='black')


        self.login_tab = Frame(tab_control,bg="black",padx=20,pady=20)
        self.register_tab = Frame(tab_control,bg="black",padx=20,pady=20)

        tab_control.add(self.login_tab, text="Login")
        tab_control.add(self.register_tab, text = "Register")

        self.login()
        self.register()
        tab_control.grid()

        self.window.mainloop()

    def register(self):
        window = self.register_tab
        l0 = Label(window,text = "VOICE BASED IMAGE EDITOR APP",fg="Orange", bg="black",font=('Courier', 23))
        l0.grid(row=0, column=1, padx=1, pady=5)
        t1 = Label(window, text="---Authorisation window---\n Register Tab",fg="Orange", bg="black",font=("Times", 20))
        t1.grid(row=1, column=1,padx=1, pady=10)

        # Name label and entry
        nl = Label(window, text="Name",fg="Orange", bg="black",font=("Times", 18))
        nl.grid(row=2, column=0,padx=30, pady=10)

        ne = Entry(window, width=25,fg="black", bg="white",font=("Times", 15))
        ne.grid(row=2, column=1,padx=2, pady=10)

        # username label and entry
        ul = Label(window, text="Username",fg="Orange", bg="black",font=("Times", 18))
        ul.grid(row=3, column=0,padx=30, pady=10)

        ue = Entry(window, width=25,fg="black", bg="white",font=("Times", 15))
        ue.grid(row=3, column=1,padx=2, pady=10)

        #  password name and entry
        pl = Label(window, text="Password",fg="Orange", bg="black",font=("Times", 18))
        pl.grid(row=4, column=0,padx=30, pady=10)

        pe = Entry(window, show="*", width=25,fg="black", bg="white",font=("Times", 15))
        pe.grid(row=4, column=1,padx=2, pady=10)

        # email label and entry
        el = Label(window, text="Email",fg="Orange", bg="black",font=("Times", 18))
        el.grid(row=5, column=0,padx=30, pady=10)

        ee = Entry(window, width=25,fg="black", bg="white",font=("Times", 15))
        ee.grid(row=5, column=1,padx=2, pady=10)

        # Phone label and entry
        phl = Label(window,text="Phone",fg="Orange", bg="black",font=("Times", 18))
        phl.grid(row=6, column=0,padx=30, pady=10)

        phe = Entry(window, width=25,fg="black", bg="white",font=("Times", 15))
        phe.grid(row=6, column=1,padx=2, pady=10)

        b1 = Button(window, text="Register",fg="Orange",bd = 3,highlightthickness=4,bg="black",font=("Times", 18),command = lambda: self.registerControl(ne.get(),
                                                                              phe.get(),ee.get(),
                                                                              ue.get(),pe.get()
                                                                              ), padx=5,pady=5)
        b1.grid(row=7, column=1,padx=0,pady=5)

    def login(self):
        window = self.login_tab

        l0 = Label(window,text = "VOICE BASED IMAGE EDITOR APP",fg="Orange", bg="black",font=('Courier', 23))
        l0.grid(row=0, column=1, padx=1, pady=5)

        ti = Label(window, text="---Authorisation window---\n Login Tab",fg="Orange", bg="black",font=("Times", 20))
        ti.grid(row=1, column=1,padx=30, pady=10)

        ul = Label(window,text="Username",fg="Orange", bg="black",font=("Times", 18))
        ul.grid(row=2,column=0,padx=30, pady=10)

        ue = Entry(window,width=25,fg="black", bg="white",font=("Times", 15))
        ue.grid(row=2,column=1,padx=2, pady=10)

        pl = Label(window, text="Password",fg="Orange", bg="black",font=("Times", 18))
        pl.grid(row=3, column=0,padx=30, pady=10)

        pe = Entry(window, show="*", width=25,fg="black", bg="white",font=("Times", 15))
        pe.grid(row=3, column=1,padx=2, pady=10)

        b1 = Button(window,text="Login",fg="Orange", bg="black",bd = 3,highlightthickness=4,font=("Times", 18),command=lambda: self.loginControl( ue.get() ,pe.get()),  padx=5,pady=5)
        b1.grid(row=4,column=1,padx=30, pady=10)

        b2 = Button(window,text="Exit",fg="Orange", bg="black",bd = 3,highlightthickness=4,font=("Times", 18),command=lambda: self.exit(),padx=5,pady=5)
        b2.grid(row=5,column=1,padx=30, pady=10)

        linfo= Label(window,text ="Register and Login to acess the App",fg="Orange", bg="black",font=('Times', 16))
        linfo.grid(row=6, column=1, padx=0, pady=10)

        linfo1= Label(window,text ="Click the Register tab above to register",fg="Orange", bg="black",font=('Times', 16))
        linfo1.grid(row=7, column=1, padx=0, pady=10)

    def loginControl(self,username,password):
        ac = AuthController()
        message = ac.login(username,password)
        if message == 1:
            self.window.destroy()
            self.transfer_control()
            #self.next()
        else:
            messagebox.showinfo('Message',message)

    def registerControl(self,name,phone,email,username,password):

        ac = AuthController()
        message = ac.register(name,phone,email,username,password)
        messagebox.showinfo('Message', message)

    def exit(self):
        MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
        if MsgBox == 'yes':
            exit()
        else:
            messagebox.showinfo('Return','You will now return to the application screen') 

av = AuthView()


