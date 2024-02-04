import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
import sqlite3
from datetime import datetime
import sqlite3

class show():
    def window(self):
        root_att = tk.Tk()
        root_att.resizable(False, True)
        root_att.title("show")
        window_width = 825
        window_height = 300

        screen_width = root_att.winfo_screenwidth()
        screen_height = root_att.winfo_screenheight()

        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        root_att.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        columns = ('name', 'status', 'start_time', 'end_time')
        tree = ttk.Treeview(root_att, columns=columns, show='headings')
        tree.heading('name', text='Student Name')
        tree.heading('status', text='P/A')
        tree.heading('start_time', text='Start Time')
        tree.heading('end_time', text='End Time')
        infos = show.get(self)
        for info in infos:
            tree.insert('', tk.END, values=info)

        tree.grid(row=0, column=0, padx=10, pady=10)

        scrollbar = ttk.Scrollbar(root_att, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        from notebook import notebook
        ttk.Button(root_att, text='back',command=lambda: [root_att.destroy(), notebook.window(self)]).grid(row=1, column=0, sticky=tk.E, padx=10, pady=10)
        root_att.mainloop()

    def get(self):
        try:
            mydb = sqlite3.connect('attendance_database.sqlite')
            mycursor = mydb.cursor()
            mycursor.execute('select * from attendance')
            info = mycursor.fetchall()
            return info
        except:
            showerror("error", "error")