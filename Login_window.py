from tkinter import *
from Connections import check, g
from User_app import window
from Admin_app import admin_window


# CREATE LOGIN WINDOW
def enter():
    eroot = Tk()

    eroot.geometry('350x250')
    eroot.title('Login')
    eroot['bg'] = 'gray22'

    lbl1_enter = Label(eroot, text='Input your data', fg='#fff', bg='gray21', font=8)
    lbl1_enter.place(x=120, y=10)
    lbl_entry_login = Label(eroot, text='Input name:', fg='#000', bg='#5997c6')
    lbl_entry_login.place(x=5, y=80)
    entry_login = Entry(eroot, width=35)
    entry_login.place(x=80, y=80)
    lbl_entry_password = Label(eroot, text='Input password:', fg='#000', bg='#5997c6')
    lbl_entry_password.place(x=5, y=120)
    entry_password = Entry(eroot, width=32)
    entry_password.place(x=98, y=120)
    btn_login = Button(eroot, text='Enter', width=10, command=lambda: input1(entry_login.get(), entry_password.get()))
    btn_login.place(x=135, y=180)

    eroot.mainloop()


# SEND DATA IN BASE AND CHECK
def input1(entry_login, entry_password):
    come = check(entry_login, entry_password)
    print(come[0], come[1])
    if entry_password == 'admin':
        if entry_login == 'admin':
            print(f'Admin: [INFO ({g})] Logged in DataBase')
            admin_window()
        else:
            pass
    elif come[0] and come[1] == True:
        print(f'[INFO ({g})] Logged in DataBase')
        window()
    else:
        print(f'[INFO ({g})] Incorrect login or password')
