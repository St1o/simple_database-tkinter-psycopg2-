"""
USER WINDOW ALLOWS TO WATCH, ADD AND DELETE INFORMATION FROM DATABASE
"""
from tkinter import *
from Config import *
from Connections import connection, delete_data, add_data, observation_action_del, observation_action_add


# MAIN USER WINDOW
def window():
    root = Tk()

    root.geometry('1000x500')
    root.title('User`s DataBase')
    root['bg'] = '#8EAEC6'

    lbl_list = Label(root, text='Choose an action', bg='#8EAEC6')
    lbl_list.place(x=10, y=30)
    list_ = [var1[0], var2[0], var3[0], var4[0], var5[0], var6[0], var7[0], var8[0], var9[0]]
    scrollbar = Scrollbar(root)
    scrollbar.place(x=260, y=20)
    list_app = Listbox(root, selectmode=SINGLE, height=5, yscrollcommand=scrollbar.set)
    for i in list_:
        list_app.insert(END, i)
    list_app.place(x=140, y=20)
    btn_list = Button(root, text='Receive', width=10, command=lambda: update())
    btn_list.place(x=290, y=30)
    scrollbar.config(command=list_app.yview)
    lbl_data = Label(root, text='Data from database', bg='#8EAEC6')
    lbl_data.place(x=10, y=140)  #
    user_data_db = Text(root, width=101, height=20)
    user_data_db.place(x=140, y=140)  #
    btn_delete = Button(root, text='Delete', width=10, command=lambda: delete(in_entry.get()))
    btn_delete.place(x=500, y=20)
    btn_add = Button(root, text='Add', width=10, command=lambda: add(in_entry.get()))  # CHECK
    btn_add.place(x=500, y=50)
    in_entry = Entry(root, width=60)
    in_entry.place(x=590, y=35)
    lbl_info = Label(root,
                     text='Formats: for add - arg(1), arg(2),... arg(n)', bg='#8EAEC6')
    lbl_info.place(x=590, y=60)
    lbl_info2 = Label(root, text='for delete - chose id', bg='#8EAEC6')
    lbl_info2.place(x=639, y=79)

    # CLEAR LAST DATA AND ATTEMPT CHOSEN LISTBOX
    def update():
        user_data_db.delete(1.0, END)
        in_entry.delete(0, END)
        in_num = list_app.get(ACTIVE)
        out_num = circle(in_num)
        select(out_num)

    # CORRECT OUTPUT
    def select(out_num):
        s = connection(out_num)
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
                    # print(in_num)
                    return in_num

    def delete(in_entry):
        name_action = 'delete'
        in_num = list_app.get(ACTIVE)
        delete_var = circle(in_num)
        print(delete_var, '213')
        observation_action_del(name_action, in_entry, delete_var)  # new
        out = delete_data(delete_var, in_entry)
        update()

    def add(in_entry):
        name_action = 'add'
        in_num = list_app.get(ACTIVE)
        add_var = circle(in_num)
        print(in_entry, add_var)
        add_data(in_entry, add_var)
        observation_action_add(name_action, add_var)
        update()

    root.mainloop()
