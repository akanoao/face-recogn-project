import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
import sqlite3
from datetime import datetime

class Return():
    def window(self):
        root_return = tk.Tk()
        root_return.title("return")
        window_width = 400
        window_height = 300

        screen_width = root_return.winfo_screenwidth()
        screen_height = root_return.winfo_screenheight()

        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        root_return.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        root_return.columnconfigure(0, weight = 1)
        root_return.columnconfigure(1, weight=1)
        root_return.columnconfigure(2, weight=1)

        lf1 = ttk.LabelFrame(root_return, text='Return')
        lf1.grid(column=0, row=0, padx=15, pady=30)

        name_label = ttk.Label(lf1, text="Name: ")
        name_label.grid(column = 0, row = 0, sticky = tk.W, padx = 5, pady = 10)

        self.name = tk.Text(lf1, height=1, width=20)
        self.name.grid(column=1, row=0, sticky=tk.W, padx=5, pady=10)
        self.name["state"] = 'disabled'

        name_button = ttk.Button(lf1, text="Scan", command=lambda: [Return.facescan(self)])
        name_button.grid(column=2, row=0, sticky=tk.W, padx=5, pady=10)

        id_label = ttk.Label(lf1, text="Book ID: ")
        id_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=10)

        self.id = tk.Text(lf1, height = 1, width= 20)
        self.id.grid(column=1, row=1, sticky=tk.W, padx=5, pady=10)
        self.id["state"] = 'disabled'

        id_button = ttk.Button(lf1, text="Scan", command=lambda: [Return.idscan(self)])
        id_button.grid(column=2, row=1, sticky=tk.W, padx=5, pady=10)

        from notebook import notebook
        ok_button = ttk.Button(lf1, text="Ok", command=lambda:[Return.addtodatabase(self), root_return.destroy(), notebook.window(self)])
        ok_button.grid(column=2, row=2, sticky=tk.W, padx=5, pady=10)

        back_button = ttk.Button(lf1, text="back", command=lambda: [root_return.destroy(), notebook.window(self)])
        back_button.grid(column=0, row=2, sticky=tk.W, padx=5, pady=10)

        lf2 = ttk.LabelFrame(root_return, text='display')
        lf2.grid(column=0, row=1, padx=15, pady=30, sticky = tk.W)

        from return_show import return_show
        dis_button = ttk.Button(lf2, text="display", command=lambda: [root_return.destroy(), return_show.window(self)])
        dis_button.grid(column=0, row=0, sticky=tk.W, padx=5, pady=10)

        root_return.mainloop()

    def idscan(self):
        from main import scanner
        data = scanner.scan_issue(self)
        self.id["state"] = 'normal'
        self.id.insert('1.0', data)
        self.id["state"] = 'disabled'

    def facescan(self):
        from webcam import facrecognition
        faces = facrecognition.facerecognition(self)
        face = faces[0]
        self.name["state"] = 'normal'
        self.name.insert('1.0', face)
        self.name["state"] = 'disabled'

    def addtodatabase(self):
        bookid = self.id.get('1.0','end')
        name = self.name.get('1.0','end')
        try:
            mydb = sqlite3.connect('database.sqlite')
            mycursor = mydb.cursor()
            mycursor.execute('select * from issued_books where book_id = ("{}")'.format(bookid))
            info = mycursor.fetchall()
            print(info)
            date = datetime.today().strftime('%Y-%m-%d')
            if(len(info) > 0):
                mycursor.execute('insert into returned_books values("{}", "{}", "{}")'.format(name,bookid,  date))
                mycursor.execute('delete from issued_books where book_id = ("{}")'.format(bookid))
            elif(len(info) == 0):
                    showerror("error", "book not issued")
            mydb.commit()
            mydb.close()
        except:
            showerror("error", "error")