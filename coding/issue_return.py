import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
import mysql.connector as sql

class issuereturn():
    def window(self):
        root_issret = tk.Tk()
        root_issret.title("issue and return")
        root_issret.geometry('200x200')

        from issue import issue
        issubutton = ttk.Button(root_issret, text='issue', command=lambda: [root_issret.destroy(), issue.window(self)])
        issubutton.pack(padx=10, pady=5, anchor=tk.CENTER)

        retbutton = ttk.Button(root_issret, text='return', command=lambda: [])
        retbutton.pack(padx=10, pady=5, anchor=tk.CENTER)

        from options import options
        backbutton = ttk.Button(root_issret, text='back', command=lambda: [root_issret.destroy(), options.window(self)])
        backbutton.pack(padx=10, pady=5, anchor=tk.CENTER)
        root_issret.mainloop()