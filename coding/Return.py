import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
import sqlite3
from datetime import datetime

class Return():
    def window(self):
        root_return = tk.Tk()
        root_return.title("return")
        window_width = 300
        window_height = 130

        screen_width = root_return.winfo_screenwidth()
        screen_height = root_return.winfo_screenheight()

        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        root_return.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        root_return.columnconfigure(0, weight = 1)
        root_return.columnconfigure(1, weight=1)
        root_return.columnconfigure(2, weight=1)

        name_label = ttk.Label(root_return, text="Name: ")
        name_label.grid(column = 0, row = 0, sticky = tk.W, padx = 5, pady = 10)

        self.name = tk.Text(root_return, height=1, width=20)
        self.name.grid(column=1, row=0, sticky=tk.W, padx=5, pady=10)
        self.name["state"] = 'disabled'

        name_button = ttk.Button(root_return, text="Scan", command=lambda: [Return.facescan(self)])
        name_button.grid(column=2, row=0, sticky=tk.W, padx=5, pady=10)

        id_label = ttk.Label(root_return, text="Book ID: ")
        id_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=10)

        self.id = tk.Text(root_return, height = 1, width= 20)
        self.id.grid(column=1, row=1, sticky=tk.W, padx=5, pady=10)
        self.id["state"] = 'disabled'

        id_button = ttk.Button(root_return, text="Scan", command=lambda: [Return.idscan(self)])
        id_button.grid(column=2, row=1, sticky=tk.W, padx=5, pady=10)

        from issue_return import issuereturn
        ok_button = ttk.Button(root_return, text="Ok", command=lambda:[Return.addtodatabase(self), root_return.destroy(), issuereturn.window(self)])
        ok_button.grid(column=2, row=2, sticky=tk.W, padx=5, pady=10)

        from issue_return import issuereturn
        back_button = ttk.Button(root_return, text="back", command=lambda: [root_return.destroy(), issuereturn.window(self)])
        back_button.grid(column=0, row=2, sticky=tk.W, padx=5, pady=10)
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
            date = datetime.today().strftime('%Y-%m-%d')
            if(len(info) > 0):
                mycursor.execute('insert into returned_books values("{}", "{}", "{}")'.format(bookid, name, date))
                mycursor.execute('delete from issued_books where book_id = ("{}")'.format(bookid))
            elif(len(info) == 0):
                    showerror("error", "book not issued")
            mydb.commit()
            mydb.close()
        except:
            showerror("error", "error")