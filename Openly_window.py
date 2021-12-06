from tkinter import *
from Login_window import enter
from Reception import create


# CREATE OPENLY WINDOW
def open_app():
    root = Tk()

    root.geometry('250x100')
    root.title('Welcome DataBase')
    root['bg'] = 'gray25'

    lbl_welcome = Label(root, text='Welcome to a DB', fg='#fff', bg='gray25', font=8)
    lbl_welcome.pack(side=TOP, pady=10)
    btn1_welcome = Button(root, text='I have account', command=lambda: way1())
    btn1_welcome.pack(side=LEFT, padx=10)
    btn2_welcome = Button(root, text='Create account', command=lambda: way2())
    btn2_welcome.pack(side=RIGHT, padx=10)

    def way1():
        root.destroy()
        enter()

    def way2():
        root.destroy()
        create()

    root.mainloop()


open_app()
