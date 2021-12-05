"""
USER WINDOW ALLOWS TO WATCH INFORMATION FROM DATABASE. NO DELETE, NO ADD, JUST WATCH
"""
from tkinter import *
from Config import *
from Connection import connection


# MAIN USER WINDOW
def window():
    root = Tk()

    root.geometry('1000x500')
    root.title('User`s DataBase')

    lbl_list = Label(root, text='Choose an action')
    lbl_list.place(x=10, y=30)
    list_ = [var1[0], var2[0], var3[0], var4[0], var5[0], var6[0], var7[0], var8[0], var9[0]]
    list_app = Listbox(root, selectmode=SINGLE, height=3)
    for i in list_:
        list_app.insert(END, i)
    list_app.place(x=140, y=20)
    scrollbar = Scrollbar(root)
    scrollbar.place(x=260, y=20)
    btn_list = Button(root, text='Receive', width=10, command=lambda: update())
    btn_list.place(x=310, y=30)
    scrollbar.config(command=list_app.yview)
    lbl_data = Label(root, text='Data from database')
    lbl_data.place(x=10, y=100)
    user_data_db = Text(root, width=100, height=20)
    user_data_db.place(x=130, y=100)

    # DELETE LAST DATA AND ATTEMPT CHOSEN LISTBOX
    def update():
        user_data_db.delete(1.0, END)
        in_num = list_app.get(ACTIVE)
        out_num = circle(in_num)
        select(out_num)

    # CORRECT OUTPUT
    def select(out_num):
        s = connection(out_num)
        print(range(len(s)))
        list_db = ''
        for i in range(len(s)):
            if len(s[i]) != 1:
                list_db += '\n'
                for j in range(len(s[i])):
                    # FOR DATA
                    form_at = '{:<10}'.format(s[i][j])
                    if '<10' in form_at:
                        form_at = form_at.replace('<10', str(s[i][j]))
                    list_db += form_at + ' || '
            else:
                # FOR NAME COLUMNS
                form_at = '{:<10}'.format(str(s[i][0]))
                list_db += form_at + ' || '
        user_data_db.insert(1.0, list_db)
        print(list_db)

    # PREPARE DATA FROM CONFIG.file FOR SIMPLIFIED WORK
    def circle(in_num):
        for i in range(len(vars)):
            for j in range(len(vars[i])):
                if in_num == vars[i][j]:
                    j += 1
                    in_num = vars[i][j]
                    print(in_num)
                    return in_num

    root.mainloop()
