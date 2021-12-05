from tkinter import *
from Login_window import enter
from Reception import create


# CREATE OPENLY WINDOW
def open_app():
    root = Tk()

    root.geometry('250x100')
    root.title('Welcome DataBase')

    lbl_welcome = Label(root, text='Welcome to a DB')
    lbl_welcome.pack(side=TOP, pady=10)
    btn1_welcome = Button(root, text='I have account', command=lambda: enter())
    btn1_welcome.pack(side=LEFT, padx=10)
    btn2_welcome = Button(root, text='Create account', command=lambda: create())
    btn2_welcome.pack(side=RIGHT, padx=10)

    root.mainloop()


open_app()
