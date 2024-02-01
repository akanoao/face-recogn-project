import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
import mysql.connector as sql
import tkcalendar as tkc

class add_user():
    def adduserwindow(self):
        adduser_win = tk.Tk()
        adduser_win.title("add user")
        window_width = 300
        window_height = 300

        screen_width = adduser_win.winfo_screenwidth()
        screen_height = adduser_win.winfo_screenheight()

        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        adduser_win.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        feilds = {}

        self.ide = tk.StringVar()
        feilds["idlabel"] = ttk.Label(adduser_win, text="ID: ")
        feilds["identry"] = ttk.Entry(adduser_win, textvariable= self.ide)

        self.user = tk.StringVar()
        feilds["userlabel"] = ttk.Label(adduser_win, text="username: ")
        feilds["userentry"] = ttk.Entry(adduser_win, textvariable= self.user)

        self.password = tk.StringVar()
        feilds["passwordlabel"] = ttk.Label(adduser_win, text="password: ")
        feilds["passwordentry"] = ttk.Entry(adduser_win, textvariable= self.password)


        for feild in  feilds.values():
            feild.pack(anchor = tk.W, fill = tk.X, padx = 5, pady = 10)

        adduserbutton = ttk.Button(adduser_win, text="add user", command=lambda: [add_user.addindatabase(self), adduser_win.destroy(), add_user.guimain(self)])
        adduserbutton.pack(side = tk.RIGHT, padx = 5, pady = 10)

    def guimain(self):
        from gui_main import gui_main
        gui_main.loginwindow()

    def addindatabase(self):
        ide = self.ide.get()
        user = self.user.get()
        password = self.password.get()
        try:
            mydb = sql.connect(host='localhost', user='root', password='anurag11')
            mycursor = mydb.cursor()
            mycursor.execute('use project')
            mycursor.execute('select * from login where id = ("{}")'.format(ide))
            info = mycursor.fetchall()
            if(len(info) > 0):
                showerror("error", "id already exists")
            else:
                mycursor.execute('insert into login values ("{}", "{}", "{}")'.format(ide, user, password))
            mydb.commit()
            mydb.close()
        except:
            showerror("error", "error")
