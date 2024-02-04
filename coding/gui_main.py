import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
import sqlite3


class gui_main():
    def loginwindow(self):
        self.root = tk.Tk()
        self.root.title("hackathon project")
        window_width = 300
        window_height = 230

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        feilds = {}

        self.username = tk.StringVar()
        feilds["ID_label"] = ttk.Label(self.root, text = "ID: ")
        feilds["ID_entry"] = ttk.Entry(self.root, textvariable=self.username)

        self.password = tk.StringVar()
        feilds["password_label"] = ttk.Label(self.root, text = "password: ")
        feilds["password_entry"] = ttk.Entry(self.root, show="*", textvariable=self.password)

        for feild in feilds.values():
            feild.pack(anchor = tk.W, fill = tk.X, padx = 5, pady = 10)

        login_button = ttk.Button(text = "login", command=lambda: [gui_main.check(self)])
        login_button.pack(side = tk.RIGHT, padx = 5, pady = 10)

        from add_user import add_user
        add_button = ttk.Button(text = "add user", command=lambda: [self.root.destroy(), add_user.adduserwindow(self)])
        add_button.pack(side = tk.LEFT, padx = 5, pady = 10)
        self.root.mainloop()

    def check(self):
        username = self.username.get()
        password = self.password.get()
        try:
            mydb = sqlite3.connect('database.sqlite')
            mycursor = mydb.cursor()
            mycursor.execute('select * from login where id = ("{}")'.format(username))
            info = mycursor.fetchall()
            if(len(info) == 0):
                showerror("error", "id not found")
            elif(len(info) > 0):
                if(info[0][1] == password):
                    from options import options
                    self.root.destroy()
                    options.window(self)
                else:
                    showerror("error", "password is wrong")
            mydb.commit()
            mydb.close()

        except:
            showerror("error", "error")



gui = gui_main()
gui.loginwindow()