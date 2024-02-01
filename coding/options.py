import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
import mysql.connector as sql

class options():
    def window(self):
        root_opt = tk.Tk()
        root_opt.title("option")
        root_opt.geometry('100x100')

        from issue_return import issuereturn
        libbutton = ttk.Button(root_opt, text='library', command=lambda: [root_opt.destroy(),issuereturn.window(self)])
        libbutton.pack(padx=10, pady=5, anchor=tk.CENTER)

        facebutton = ttk.Button(root_opt, text='face recognition', command=lambda: [])
        facebutton.pack(padx=10, pady=5, anchor=tk.CENTER)

        root_opt.mainloop()