from tkinter import *
from Connection import create_ac


# CREATE ACCOUNT WINDOW
def create():
    root = Tk()

    root.geometry('350x250')
    root.title('Reception')

    lbl1_new = Label(root, text='Create account')
    lbl1_new.place(x=120, y=10)
    lbl_new_login = Label(root, text='Create name:')
    lbl_new_login.place(x=5, y=80)
    new_login = Entry(root, width=35)
    new_login.place(x=80, y=80)
    lbl_new_password = Label(root, text='Create password:')
    lbl_new_password.place(x=5, y=120)
    new_password = Entry(root, width=32)
    new_password.place(x=98, y=120)
    btn_new = Button(root, text='Create', width=10, command=lambda: create_in_db(new_login.get(), new_password.get()))
    btn_new.place(x=135, y=180)

    root.mainloop()


# CREATE ACCOUNT IN DATABASE
def create_in_db(new_login, new_password):
    new = create_ac(new_login, new_password)
    print('[INFO] Account successfully created')
