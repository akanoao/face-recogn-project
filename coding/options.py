import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
import sqlite3
import mysql.connector as sql

class options():
    def window(self):
        root_opt = tk.Tk()
        root_opt.title("option")
        window_width = 300
        window_height = 100

        screen_width = root_opt.winfo_screenwidth()
        screen_height = root_opt.winfo_screenheight()

        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        root_opt.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        from issue_return import issuereturn
        libbutton = ttk.Button(root_opt, text='library', command=lambda: [root_opt.destroy(),issuereturn.window(self)])
        libbutton.pack(padx=10, pady=5, anchor=tk.CENTER)

        from attendance import attendance
        facebutton = ttk.Button(root_opt, text='attendance', command=lambda: [root_opt.destroy(), attendance.window(self)])
        facebutton.pack(padx=10, pady=5, anchor=tk.CENTER)

        secbutton = ttk.Button(root_opt, text='security', command=lambda: [])
        secbutton.pack(padx=10, pady=5, anchor=tk.CENTER)

        root_opt.mainloop()