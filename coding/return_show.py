import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
import sqlite3
from datetime import datetime

class return_show():
    def window(self):
        root_return_show = tk.Tk()
        root_return_show.title("Returned books")
        window_width = 625
        window_height = 290

        screen_width = root_return_show.winfo_screenwidth()
        screen_height = root_return_show.winfo_screenheight()

        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        root_return_show.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        columns = ('name', 'book_id', 'date')
        tree = ttk.Treeview(root_return_show, columns=columns, show='headings')
        tree.heading('name', text='Name')
        tree.heading('book_id', text='Book ID')
        tree.heading('date', text='Return Date')
        infos = return_show.display(self)
        print(infos)
        for info in infos:
            tree.insert('', tk.END, values=info)

        tree.grid(row=0, column=0, padx = 10, pady = 10)

        from issue import issue
        ttk.Button(root_return_show, text='back', command=lambda: [root_return_show.destroy(), issue.window(self)]).grid(row = 1, column = 0, sticky = tk.E, padx = 10, pady = 10)
        root_return_show.mainloop()

    def display(self):
        try:
            mydb = sqlite3.connect('database.sqlite')
            mycursor = mydb.cursor()
            mycursor.execute('select * from returned_books')
            info = mycursor.fetchall()
            mydb.commit()
            mydb.close()
            return info
        except:
            showerror("error", "error")