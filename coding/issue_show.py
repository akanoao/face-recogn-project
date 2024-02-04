import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
import sqlite3
from datetime import datetime

class issue_show():
    def window(self):
        root_issue_show = tk.Tk()
        root_issue_show.title("issued books")
        window_width = 625
        window_height = 290

        screen_width = root_issue_show.winfo_screenwidth()
        screen_height = root_issue_show.winfo_screenheight()

        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        root_issue_show.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        columns = ('name', 'book_id', 'date')
        tree = ttk.Treeview(root_issue_show, columns=columns, show='headings')
        tree.heading('name', text='Name')
        tree.heading('book_id', text='Book ID')
        tree.heading('date', text='Date of issue')
        infos = issue_show.display(self)
        print(infos)
        for info in infos:
            tree.insert('', tk.END, values=info)

        tree.grid(row=0, column=0, padx = 10, pady = 10)

        from issue import issue
        ttk.Button(root_issue_show, text='back', command=lambda: [root_issue_show.destroy(), issue.window(self)]).grid(row = 1, column = 0, sticky = tk.E, padx = 10, pady = 10)
        root_issue_show.mainloop()

    def display(self):
        try:
            mydb = sqlite3.connect('database.sqlite')
            mycursor = mydb.cursor()
            mycursor.execute('select * from issued_books')
            info = mycursor.fetchall()
            mydb.commit()
            mydb.close()
            return info
        except:
            showerror("error", "error")